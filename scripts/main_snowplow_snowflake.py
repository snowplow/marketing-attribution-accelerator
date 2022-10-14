# coding=utf-8
# Copyright 2022 Google LLC..
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Loads the data into Snowflake needed to run Fractribution."""

import os
import re
from typing import Any, Dict, List, Mapping, Optional, Tuple
from absl import app
from absl.flags import argparse_flags
import fractribution

from snowflake.snowpark import Session # snowflake support


connection_parameters = {
    "account": os.environ["snowflake_account"],
    "user": os.environ["snowflake_user"],
    "password": os.environ["snowflake_password"],
    "role": os.environ["snowflake_user_role"],
    "warehouse": os.environ["snowflake_warehouse"],
    "database": os.environ["snowflake_database"],
    "schema": os.environ["snowflake_schema"]

}


_OUTPUT_TABLES = ['path_summary_table', 'report_table']

VALID_CHANNEL_NAME_PATTERN = re.compile(r'^[a-zA-Z_]\w+$', re.ASCII) # TODO: does this need to be enforced?

def _is_valid_column_name(column_name: str) -> bool:
  """Returns True if the column_name is a valid Snowflake column name."""
  # TODO: can this be done in dbt (maybe with a macro?)
  return (len(column_name) <= 255 and
          VALID_CHANNEL_NAME_PATTERN.match(column_name) is not None)

def _extract_channels(
    client, params: Mapping[str, Any]) -> List[str]:
  """Returns the list of names by running extract_channels.sql.

  Args:
    client: Client.
    params: Mapping of template parameter names to values.
  Returns:
    List of channel names.
  Raises:
    ValueError: User-formatted error if channel is not a valid Snowflake column. 
  """

  channels = [
      row.CHANNEL for row in client]
  if fractribution.UNMATCHED_CHANNEL not in channels:
    channels.append(fractribution.UNMATCHED_CHANNEL)
  for channel in channels:
    if not _is_valid_column_name(channel):
      raise ValueError('Channel is not a legal Snowflake column name: ', channel)
  return channels


def parse_args(argv):
    ap=argparse_flags.ArgumentParser()
    model = ap.add_argument_group(title="Attribution model")
    model.add_argument(
        "--attribution_model",
        type=str,
        help="Attribution model. One of: 'shapley', 'first_touch', 'last_touch', 'position_based', 'linear'",
        default="shapley"
    )
    
    window = ap.add_argument_group(title="Conversion window")
    window.add_argument(
        "--conversion_window_start_date",
        type=str,
        required=True,
        help="Start date of the window for conversions"
    )
    window.add_argument(
        "--conversion_window_end_date",
        type=str,
        required=True,
        help="End date of the window for conversions"
    )
    args=ap.parse_args(argv[1:])
    if args.attribution_model not in fractribution.Fractribution.ATTRIBUTION_MODELS:
        raise ValueError(
        f'Unknown attribution_model. Use one of: {list(fractribution.Fractribution.ATTRIBUTION_MODELS.keys())}')
    
    return args
    
def get_channels(session):
    """Enumerates all possible channels."""
    query = """SELECT DISTINCT channel FROM s_channel_counts"""
    # todo: put s_channel_counts in a variable
    return session.sql(query).collect()

def get_path_summary_data(session):
    query = """
        SELECT transformedPath, conversions, nonConversions, revenue
        FROM s_path_summary
        """ # TODO: add s_path_summary as a variable instead

    return session.sql(query).collect()

def create_attribution_report_table(session):
    query = f"""
        CREATE OR REPLACE TABLE report_table AS
        SELECT
            *,
            DIV0(revenue, spend) AS roas
        FROM
            channel_attribution
            LEFT JOIN
            s_channel_spend USING (channel)
    """

    return session.sql(query).collect()


def run_fractribution(params: Mapping[str, Any]) -> None:
  """Runs fractribution on the extract_fractribution_input_data Snowflake tables.

  Args:
    params: Mapping of all template parameter names to values.
  """

  # TODO: get the results of this query?

  session = Session.builder.configs(connection_parameters).create()

  path_summary = get_path_summary_data(session)
  
  # Step 1: Extract the paths from the path_summary_table.
  frac = fractribution.Fractribution(path_summary)

  frac.run_fractribution(params['attribution_model']) 

  frac.normalize_channel_to_attribution_names()


  # max override
  path_list = frac._path_summary_to_list()
  print('path list:', path_list)

  paths = session.create_dataframe(path_list)

  # now save this to a table...
  paths.write.mode("overwrite").save_as_table("path_summary")

  conversion_window_start_date = params["conversion_window_start_date"]
  conversion_window_end_date = params["conversion_window_end_date"]

  channel_to_attribution = frac._get_channel_to_attribution()
  channel_to_revenue = frac._get_channel_to_revenue()
  rows = []
  for channel, attribution in channel_to_attribution.items():
        row = {'conversionWindowStartDate': conversion_window_start_date,
                'conversionWindowEndDate': conversion_window_end_date,
                'channel': channel,
                'conversions': attribution,
                'revenue': channel_to_revenue.get(channel, 0.0)
                }
        rows.append(row)

  # create a new dataframe

  channel_attribution = session.create_dataframe(rows)
  channel_attribution.write.mode("overwrite").save_as_table("channel_attribution")

# Create the report table in snowflake
  report = create_attribution_report_table(session)
  print(report)
  
  session.close()


def run(input_params: Mapping[str, Any]) -> int:
  """Main entry point to run Fractribution with the given input_params.

  Args:
    input_params: Mapping from input parameter names to values.
  Returns:
    0 on success and non-zero otherwise
  """
  params = input_params # standard

  # assumes that the dataset already exists
  params['channel_counts_table'] = 'channel_counts'

  session = Session.builder.configs(connection_parameters).create()

  # get the results from Snowflake and ensure they can be iterated
  # over.

  channels = get_channels(session)
  session.close()
  # Extract the channel definitions into params for use in later queries.
  # this can potentially be dbt-ified

  params['channels'] = _extract_channels(channels, None)

  # this is required but could be significantly simplified
  # and possibly put into a variable?


  # this is the real meat and potatoes of the script
  run_fractribution(params)

  return 0


def standalone_main(args):
    input_params = {
        "attribution_model": args.attribution_model,
        "conversion_window_start_date": args.conversion_window_start_date,
        "conversion_window_end_date": args.conversion_window_end_date
    }
    run(input_params)

if __name__ == '__main__':
  app.run(standalone_main, flags_parser=parse_args)

+++
title= "Set-up and run fractribution package"
weight = 3
post = ""
+++

The snowplow_web_page_views (created by the snowplow_web package) and sample_events_fractribution tables will be used to demonstrate how to set-up and run the snowplow_fractribution dbt package to create the tables needed for fractional attribution.

***

#### **Step 1:** Set-up Variables

The snowplow_fractribution dbt package comes with a list of variables specified with a default value that you may need to overwrite in your own dbt project `dbt_project.yml` file. For details you can have a look at the installed package's default variables which can be found at `[dbt_project_name]/dbt_packages/snowplow_fractribution/dbt_project.yml`.

For the sake of simplicity we have selected the variables that you will most likely need to overwrite, the rest can be changed at a later stage if and when it is needed.

- `conversion_window_start_date`: The start date in UTC for the window of conversions to include
- `conversion_window_end_date`: The end date in UTC for the window of conversions to include
- `conversion_hosts`: url_hosts to consider
- `path_lookback_steps`: The limit for the number of marketing channels to look at before the conversion (default is 0 = unlimited)
- `path_lookback_days`: Restrict the model to marketing channels within this many days of the conversion (values of 30, 14 or 7 are recommended)
- `path_transforms`: An array of path transforms and their arguments (see below section **Path Transform Options**)
- `consider_intrasession_channels`: Boolean. If false, only considers the channel at the start of the session (i.e. first page view). If true, considers multiple channels in the conversion session as well as historically.

The default source schemas and tables used by the snowplow_fractribution package are:
- *atomic_derived.snowplow_web_page_views* for the page_views data (page_views_source)
- *atomic.events* for the Snowplow event data (conversions_source)

If either of these differ in your warehouse, set the correct names as variables in your own dbt_project.yml, e.g.:
-  `page_views_source`: `custom_schema_derived.snowplow_web_page_views`
-  `conversions_source`: `custom_schema_derived.snowplow_ecommerce_transaction_interactions`

For example, if you do not wish the package to query your `atomic.events` table to get the conversion value data, the `conversions_source` variable can point to a different table, such as the derived table `snowplow_ecommerce_transaction_interactions` created by the ecommerce model. **(TODO: Add link)**
Another option would be to create your own incremental data model for transaction/conversion events, and add a reference to that model as the conversions_source variable, e.g. `conversions_source: {{ ref('custom_conversions_model') }}`

You only need to set the variables for those that differ from the default.

Below is an example snippet of these variables in your `dbt_project.yml`:

```yml
vars:
  conversion_window_start_date: '2022-06-03'
  conversion_window_end_date: '2022-08-01'
  conversion_hosts: ['poplindata.com']
  path_lookback_steps: 0
  path_lookback_days: 30
  path_transforms: [['Exposure', null]]
  consider_intrasession_channels: false
  conversions_source: 'atomic.sample_events_fractribution'
```

**Path Transform Options**

Paths to conversion are often similar, but not identical. As such, path transforms reduce unnecessary complexity in similar paths before running the attribution algorithm.

There are five path transform options available:
- Exposure (default in this package): the same events in succession are reduced to one: A -> A -> B becomes A -> B. A compromise between first and unique.
- Unique: all events in a path are treated as unique (no reduction of complexity). Best for smaller datasets (small lookback window) without a lot of retargeting.
- First: keep only the first occurrence of any event: A -> B -> A becomes A -> B. Best for brand awareness marketing.
- Frequency: keep a count of the events' frequency: A -> A -> B becomes A(2) -> B. Best when there is a lot of retargeting.
- Recency: time bucket events depending on when they occurred before the conversion and collapse those in the same bucket (square braces indicate minutes before conversion event): A[15-30] -> B[1-5] -> A[1-5] -> B[1-5] becomes A[15-30] -> B[1-5] -> A[1-5]. Best for larger lookback windows.

#### **Step 2:** Configure macros

**Configure the conversion_clause macro**

The conversion_macro specifies how to filter Snowplow events to only conversion events. How this is filtered will depend on your definition of a conversion. The default is filtering to events where `tr_total > 0`, but this could instead filter on `event_name = 'checkout'`, for example. If you are using the ecommerce model, you will still need to set this for the fractribution code to run (even though all events are conversions in the ecommerce model), just change it to `transaction_revenue > 0`.

If you wish to change this filter, copy the `conversion_clause.sql` file from the macros folder in the snowplow_fractribution package (at `[dbt_project_name]/dbt_packages/snowplow_fractribution/macros/conversion_clause.sql`) and add it to the macros folder of your own dbt project. Update the filter and save the file.


**Configure the conversion_value macro**

The conversion_value macro specifies either a single column or a calculated value that represents the value associated with that conversion. The default is `tr_total`, but `revenue` or a calculation using `revenue` and `discount_amount` from the default ecommerce schema, for example, could similarly be used.

If you wish to change this value, copy the `conversion_value.sql` file from the macros folder in the snowplow_fractribution package (at `[dbt_project_name]/dbt_packages/snowplow_fractribution/macros/conversion_value.sql`) and add it to the macros folder of your own dbt project. Update the value and save the file.

**Configure the default channel_classification macro**

The channel_classification macro is used to perform channel classifications. This can be altered to generate your expected channels if they differ from the channels generated in the default macro. It is highly recommended that you examine and configure this macro when using your own data, as the default values will not consider any custom marketing parameters.

If you wish to change the channel classification macro, copy the `channel_classification.sql` file from the macros folder in the snowplow_fractribution package (at `[dbt_project_name]/dbt_packages/snowplow_fractribution/macros/channel_classification.sql`) and add it to the macros folder of your own dbt project. Update the SQL and save the file.
 
***

#### **Step 3:** Run the model

Execute the following either through your CLI or from within dbt Cloud

```
dbt run --select snowplow_fractribution
```

This should take a couple of minutes to run.

***

#### **Step 4:** Check the output schema
Head to the SQL editor of your choice (e.g.: Snowflake Web UI) to check the model's output. You should be able to see the data under the _derived schema.

***

#### **Step 5:** Explore the data created by your dbt models

Take some time to familiarise yourself with the derived tables. These tables are used in the next step to fractionally attribute revenue to channels. Tables output by the snowplow_fractribution dbt package are:

- `snowplow_fractribution_channel_counts`: Number of events grouped by channel, campaign, source and medium.
- `snowplow_fractribution_channel_spend`: Spend on each channel, used in ROAS calculations.
- `snowplow_fractribution_conversions_by_customer_id`: Conversion revenue for each conversion, along with the associated customerid.
- `snowplow_fractribution_path_summary`: Summary of different path combinations and associated conversion/non-conversions.
- `snowplow_fractribution_paths_to_conversion`: Path combinations leading to conversion.
- `snowplow_fractribution_paths_to_non_conversion`: Path combinations leading to non-conversion.
- `snowplow_fractribution_sessions_by_customer_id`: Channel information by session timestamp, where an event timestamp is considered as the session start.

***

Next we will run a Python script to create the actual Fractribution table.

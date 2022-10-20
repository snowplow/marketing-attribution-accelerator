+++
title= "Set up and run dbt Package"
weight = 2
post = ""
+++

The snowplow_web_page_views (created by the snowplow_web package) and sample_events (data provided in the [web accelerator](https://docs.snowplow.io/accelerators/web/upload/upload_1/)) tables will be used to demonstrate how to set up and run the fractribution dbt package to create the tables needed for fractional attribution.

***

#### **Step 1:** Set-up Variables

The fractribution dbt package comes with a list of variables specified with a default value that you may need to overwrite in your own dbt project `dbt_project.yml` file. For details you can have a look at the installed package's default variables which can be found at `[dbt_project_name]/dbt_packages/fractribution/dbt_project.yml`.

For the sake of simplicity we have selected the variables that you will most likely need to overwrite, the rest can be changed at a later stage if and when it is needed.

- `conversion_window_start_date`: The start date in UTC for the window of conversions to include
- `conversion_window_end_date`: The end date in UTC for the window of conversions to include
- `conversion_hosts`: url_hosts to consider
- `path_lookback_steps`: The limit for the number of marketing channels to look at before the conversion (default is 0 = unlimited)
- `path_lookback_days`: Restrict the model to marketing channels within this many days of the conversion (values of 30, 14 or 7 are recommended)
- `path_transforms`: An array of path transforms and their arguments (see below section **Path Transform Options**)
- `consider_intrasession_channels`: Boolean. If false, only considers the channel at the start of the session (i.e. first page view). If true, considers multiple channels in the conversion session as well as historically.

The default source schemas and tables used by the fractribution package are:
- *atomic.events* for the Snowplow event data 
- *atomic_derived.snowplow_web_page_views* for the page_views data

If any of these differ in your warehouse, set the correct names as variables in your dbt_project.yml, e.g.:
- `snowflake__atomic_schema`: 'test_atomic'
- `snowflake__events_table`: 'sample_events'
- `snowflake__page_views_schema`: 'test_atomic_derived'
- `snowflake__page_views_table`: 'snowplow_web_page_views_scratch'

You only need to set the variables for those that differ from the default.

Below is an example snippet of these variables in your `dbt_project.yml`:

```yml
vars:
  conversion_window_start_date: '2022-07-03'
  conversion_window_end_date: '2022-08-01'
  conversion_hosts: ['exampleurl.com']
  path_lookback_steps: 0
  path_lookback_days: 30
  path_transforms: [['Exposure', null]]
  consider_intrasession_channels: false
  snowflake__events_table: 'sample_events'
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

The conversion_macro specifies how to filter Snowplow events to only conversion events. How this is filtered will depend on your definition of a conversion. The default is filtering to events where `tr_total > 0`, but this could instead filter on `event_name = 'checkout'`, for example. 

If you wish to change this filter, copy the `conversion_clause.sql` file from the macros folder in the fractribution package (at `[dbt_project_name]/dbt_packages/fractribution/macros/conversion_clause.sql`) and add it to the macros folder of your own dbt project. Update the filter and save the file.


**Configure the conversion_value macro**

The conversion_value macro specifies either a single column (or a calculated value) that represents the value associated with that conversion. The default is `tr_total`, but `revenue` or a calculation using `revenue` and `discount_amount` from the default ecommerce schema, for example, could similarly be used.

If you wish to change this value, copy the `conversion_value.sql` file from the macros folder in the fractribution package (at `[dbt_project_name]/dbt_packages/fractribution/macros/conversion_value.sql`) and add it to the macros folder of your own dbt project. Update the value and save the file.

**Configure the default channel_classification macro**

The channel_classification macro is used to perform channel classifications. This can be altered to generate your expected channels if they differ from the channels generated in the default macro. It is highly recommended that you examine and configure this macro, as the default values will not consider any custom marketing parameters.

If you wish to change the channel classification macro, copy the `channel_classification.sql` file from the macros folder in the fractribution package (at `[dbt_project_name]/dbt_packages/fractribution/macros/channel_classification.sql`) and add it to the macros folder of your own dbt project. Update the SQL and save the file.
 
 
If you have added one or more of these macros to your own project's macros folder, the next step is to add the following to your dbt_project.yml file (replacing `your_project_name` with the name of your project, found at the top of the dbt_project.yml file after `name:`):

```yml
dispatch:
  - macro_namespace: fractribution_snowplow
    search_order: ['your_project_name', 'fractribution_snowplow']
```

This instructs dbt to look for files in your macros folder first before looking in the fractribution package's macros folder.
***

#### **Step 3:** Run the model

Execute the following either through your CLI or from within dbt Cloud

```
dbt run --select fractribution
```

This should take a couple of minutes to run.

***

#### **Step 4:** Check the output schema
Head to the SQL editor of your choice (e.g.: Snowflake Web UI) to check the model's output. You should be able to see the data under the schema specified in your profiles.yml.

***

#### **Step 5:** Explore the data created by your dbt models

Take some time to familiarise yourself with the derived tables. These tables are used in the next step to fractionally attribute revenue to channels. Tables output by the fractribution dbt package are:

- `channel_counts`: Number of events grouped by channel, campaign, source and medium.
- `channel_spend`: Spend on each channel, used in ROAS calculations.
- `conversions_by_customer_id`: Conversion revenue for each conversion, along with the associated customerid.
- `path_summary`: Summary of different path combinations and associated conversion/non-conversions.
- `paths_to_conversion`: Path combinations leading to conversion.
- `paths_to_non_conversion`: Path combinations leading to non-conversion.
- `sessions_by_customer_id`: Channel information by session timestamp, where an event timestamp is considered as the session start.

***

Next we will run a Python script to create the actual Fractribution table.

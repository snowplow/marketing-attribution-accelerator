+++
title = "Run snowplow_web dbt package"
weight = 2
post = ""
+++

We will use the *snowplow_web_page_views* table created by the [snowplow-web](https://hub.getdbt.com/snowplow/snowplow_web/latest/) dbt package, as well as the Snowplow events table, to create an attribution report table. This table provides the marginal contribution of each channel to a user-level conversion event as well as the monetary value attributed to that channel from the conversion event. It will also contain spend information and calculated ROAS per channel.

As such, this tutorial assumes that you are already familiar with the `snowplow-web` dbt package. If not, detailed instructions can be found in the [Advanced Analytics for Web](https://docs.snowplow.io/accelerators/web) accelerator.


#### **Step 1:** Update variables for provided sample data
Ensure that snowplow_web specific variables are set in your dbt_project.yml file that are appropriate for the provided sample data, particularly:

```
snowplow__start_date: '2022-06-03'
snowplow__enable_iab: false
snowplow__enable_ua: false
snowplow__enable_yauaa: false
snowplow__events: 'atomic.sample_events_attribution'
```

#### **Step 2:** Run the package
It is important to ensure that the schemas and tables this will build into will not overwrite any tables you wish to keep.
You can change the schema in your profiles.yml if you wish to ensure nothing will be overwritten.

Run the snowplow_web package
```
dbt run --selector snowplow_web --full-refresh --vars 'snowplow__allow_refresh: true'
```

This should have created the table `<your_schema>_derived.snowplow_web_page_views`. This is the table that we will be using in the snowplow_fractribution package.

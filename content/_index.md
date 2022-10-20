+++
title = "Introduction"
menuTitle = "Introduction"
pre = "<i class='fas fa-rocket'></i> "
chapter = false
weight = 1
+++

!['logo-banner'](images/logo_banner_2.png)

Welcome to the **Fractribution** accelerator. This is a tutorial for a Snowplow accelerator that demonstrates how to run fractional attribution analysis on Snowplow data, coined 'Fractribution'. Fractional attribution allows you to attribute the value of a conversion to one or more channels depending on the conversion pathway. As a result, it becomes possible to determine the revenue per channel, as well as the return on advertising spend (ROAS) if you have spend data for each marketing channel. Once finished, you will be able to build a deeper understanding of customer behaviour on your website and use your data to influence business decisions.

Here you will learn to:

* Model and Visualise Snowplow data
  - using the [fractribution](https://hub.getdbt.com/snowplow/fractribution/latest/) dbt package and Python script
  - using our sample data for Snowflake (no need to have a working pipeline)
* Set-up Snowplow Tracking and Enrichment for fractribution
* Apply what you have learned on your own pipeline to gain insights
***

#### Who is this guide for?

- Data practitioners who would like to get familiar with further options for modelling Snowplow data.
- Data practitioners who want to learn how to use the fractribution dbt package, to gain insight into ROAS figures using fractional attribution as quickly as possible.

***

#### What you will learn

In approximately half a day (~5 hours) you can achieve the following:

- **Model -** Configure and run the snowplow-web data model
- **Visualise -** Visualise an example table output
- **Track -** Set-up and deploy tracking needed for fractribution to your website or single page application
- **Enrich -** Add an enrichment to your data
- **Next steps -** Gain value from your own pipeline data


{{<mermaid>}}
gantt
        dateFormat  HH-mm
        axisFormat %H:%M
        section 1. Model
        2h          :model, after upload, 2h
        section 2. Visualise
        10min          :visualise, after model, 10m
        section 3. Track
        1h          :track, after visualise, 1h
        section 4. Enrich
        1h          :enrich, after track, 1h
        section 5. Next steps
        1h          :next steps, after enrich, 1h

{{</mermaid >}}

***

#### Prerequisites

- It is assumed that you have either already run the [snowplow-web](https://hub.getdbt.com/snowplow/snowplow_web/latest/) dbt package, or have a snowplow_web_page_views and Snowplow events tables already in your data warehouse. If not, we recommend following the first two steps of the [Advanced Analytics for Web](https://docs.snowplow.io/accelerators/web) accelerator.

**Modeling**
- dbt CLI installed / dbt Cloud account available
  - New dbt project created and configured
- Python 3 Installed
- Snowflake account and a user with access to create schemas and tables

**Tracking and Enrichment**
- Snowplow pipeline
- Web app to implement tracking

{{% notice info %}}
Please note that Snowflake will be used for illustration. The snowplow-web dbt package also supports **BigQuery, Databricks, Postgres** and **Redshift**. Further adapter support for this accelerator will be added in future.
{{% /notice %}}

***

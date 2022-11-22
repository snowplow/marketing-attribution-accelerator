+++
title = "Introduction"
menuTitle = "Introduction"
pre = "<i class='fas fa-rocket'></i> "
chapter = false
weight = 1
+++

!['logo-banner'](images/logo_banner_2.png)

Welcome to the **Fractribution** accelerator. This is an accelerator to demonstrate and guide you on how to run fractional attribution analysis on Snowplow data, coined 'Fractribution'. Fractional attribution allows you to attribute the value of a conversion to one or more channels depending on the conversion pathway. As a result, it becomes possible to determine the revenue per channel, as well as ROAS<sup>*</sup> once you have cost data for each marketing channel. Once finished, you will be able to enhance your strategic marketing decisions, such as channel investment and focus, in a more data informed way.

Here you will learn to:

* Model and Visualise Snowplow data
  - using the [fractribution](https://hub.getdbt.com/snowplow/fractribution/latest/) dbt package and Python script
  - using our sample data for Snowflake (no need to have a working pipeline)
* Set-up Snowplow Tracking and Enrichment for fractribution
* Apply what you have learned on your own pipeline to gain insights
***

#### Who is this guide for?

- Data practitioners who would like to get familiar with further options for modeling Snowplow data.
- Data practitioners who want to learn how to use the fractribution dbt package, to gain insight into ROAS figures using fractional attribution as quickly as possible.

***

#### What you will learn

In approximately half a day (~5.5 hours) you can achieve the following:

- **Upload -** Upload some sample data
- **Model -** Configure and run the snowplow-web data model
- **Visualise -** Visualise an example table output
- **Track -** Set-up and deploy tracking needed for fractribution to your website or single page application
- **Enrich -** Add an enrichment to your data
- **Next steps -** Gain value from your own pipeline data


{{<mermaid>}}
gantt
        dateFormat  HH-mm
        axisFormat %H:%M
        section 1. Upload
        30min       :upload, 00-00, 30m
        section 2. Model
        2h          :model, after upload, 2h
        section 3. Visualise
        10min          :visualise, after model, 10m
        section 4. Track
        1h          :track, after visualise, 1h
        section 5. Enrich
        1h          :enrich, after track, 1h
        section 6. Next steps
        1h          :next steps, after enrich, 1h

{{</mermaid >}}
You can use the provided sample data to follow steps 1-3. If you have your own website or single page application, you can also follow steps 4-6 to run fractribution analysis on your own data. 
***

#### Prerequisites

- It is assumed that you are already familiar with the [snowplow-web](https://hub.getdbt.com/snowplow/snowplow_web/latest/) dbt package, or have a snowplow_web_page_views and Snowplow events table already in your data warehouse. If not, we recommend completing the [Advanced Analytics for Web](https://docs.snowplow.io/accelerators/web) accelerator.

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
<sup>*</sup>ROAS: The amount of revenue that is earned for every dollar spent on advertising
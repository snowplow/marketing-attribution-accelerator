+++
title = "Introduction"
menuTitle = "Introduction"
pre = "<i class='fas fa-rocket'></i> "
chapter = false
weight = 1
+++

### Attribution Modeling Accelerator

#### Introduction

This accelerator will show you how to perform attribution modeling on your Snowplow data, enabling you to attribute a portion of the value of a conversion to specific channels based on the conversion pathway. With this information, you can calculate the revenue per channel and Return on Advertising Spend (ROAS*) for each marketing channel, giving you a data-driven approach to making strategic marketing decisions such as channel investment and focus.

Here you will learn to:

* Model and Visualise Snowplow data
  - using the [snowplow_fractribution](https://hub.getdbt.com/snowplow/snowplow_fractribution/latest/) dbt package and Python script
  - using our sample data (no need to have a working pipeline)
* Set-up Snowplow Tracking and Enrichment to prepare your data sources
* Apply what you have learned on your own pipeline to gain insights
***

#### Who is this guide for?

- Data practitioners who would like to get familiar with further options for modeling Snowplow data.
- Data practitioners who want to learn how to use the snowplow_fractribution dbt package, to gain insight into ROAS figures using attribution modeling as quickly as possible.
- This accelerator currently supports Snowflake, BigQuery and Databricks

***

#### What you will learn

In an estimated minimum of half a day (~5.5 hours) you can achieve the following:

- **Upload -** Upload some sample data
- **Model -** Configure and run the snowplow-fractribution data model
- **Visualise -** Have a closer look at the Attribution Modeling report table to better understand the outcome of the analysis.
- **Track -** Set-up and deploy tracking needed for your website or single page application for being able to perform attribution modeling
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

{{% notice info %}}
You don't necessarily need to follow all the steps in order. You could choose to skip steps 1-3 where you would learn how to perform Attribution Modeling through the sample data. If you have your own website or single page application, you could follow steps 4-6 to run the analysis on your own data right away and go through the first sections afterwards.
{{% /notice %}}
***

#### Prerequisites

- It is assumed that you are already familiar with the [snowplow-web](https://hub.getdbt.com/snowplow/snowplow_web/latest/) dbt package, or have a snowplow_web_page_views and Snowplow events table already in your data warehouse. If not, we recommend completing the [Advanced Analytics for Web](https://docs.snowplow.io/accelerators/web) accelerator.
- It is preferable to be familiar with the [snowplow-ecommerce](https://hub.getdbt.com/snowplow/snowplow_ecommerce/latest/) dbt package, that you can use to process your transaction events which are needed for the conversion source for the `snowplow-fractribution` package to work.

**Modeling**
- dbt CLI installed / dbt Cloud account available
  - New dbt project created and configured
- Python 3 Installed
- Snowflake, Databricsks or BigQuery account and a user with access to create schemas and tables

**Tracking and Enrichment**
- Snowplow pipeline
- Web app to implement tracking

{{% notice info %}}
Snowplow Attribution Modeling is closely based on Google's Fractional Attribution - coined Fractribution. If you would like to learn more about how it works, please see these [slides](https://github.com/google/fractribution/blob/master/Fractribution_Slides.pdf) and this [document](https://support.google.com/analytics/answer/3191594?hl=en#algorithm)
{{% /notice %}}


***
<sup>*</sup>ROAS: The amount of revenue that is earned for every dollar spent on advertising

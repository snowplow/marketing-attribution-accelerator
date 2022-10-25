+++
title = "Modeling"
date = 2022-08-16T17:24:05+01:00
weight = 3
chapter = true
pre = "1. "
+++

<!-- ### Chapter 1 -->

# Modeling your Data

{{<mermaid>}}
flowchart LR
    id1(Model)-->id2(Visualise)-->id3(Track)-->id4(Enrich)-->id5(Next steps)
    style id1 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


In this chapter you will learn how to set-up and run the fractribution package and script to output a fractional attribution report using the sample data.

To create a fractional attribution table in your Snowflake warehouse, this tutorial uses the [fractribution](https://hub.getdbt.com/snowplow/fractribution/latest/) dbt package and also a Python script (or Docker container). 
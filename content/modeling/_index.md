+++
title = "Modeling"
date = 2022-08-16T17:24:05+01:00
weight = 3
chapter = true
pre = "2. "
+++

<!-- ### Chapter 1 -->

# Modeling your Data

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Model)-->id3(Visualize)-->id4(Track)-->id5(Enrich)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


In this chapter you will learn how to set-up and run the snowplow_fractribution package and script to output an attribution report using the sample data.

To create an attribution modeling table in your warehouse, this tutorial uses the [snowplow_fractribution](https://hub.getdbt.com/snowplow/snowplow_fractribution/latest/) dbt package and also a Python script (or Docker container).

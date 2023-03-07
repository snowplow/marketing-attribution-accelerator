+++
title = "Tracking"
chapter = true
weight = 5
pre = "4. "
post = ""
+++

<!-- ### Chapter 3 -->

# Tracking


{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Model)-->id3(Visualise)-->id4(Track)-->id5(Enrich)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}

Regardless if you followed steps 1-3 to learn how to perform Attribution Modeling using a sample dataset, from this section onwards (steps 4-6) you can learn how to create your data sources to be able to run the analysis for your own business.

Getting started with sending events using the JavaScript tracker is very similar to other web analytics vendors like Google Analytics and Adobe Analytics.

We will be setting up two key events that are needed for fractribution: page_views and conversions.

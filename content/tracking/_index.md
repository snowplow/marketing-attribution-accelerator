+++
title = "Tracking"
chapter = true
weight = 5
pre = "3. "
post = ""
+++

<!-- ### Chapter 3 -->

# Tracking


{{<mermaid>}}
flowchart LR
    id1(Model)-->id2(Visualise)-->id3(Track)-->id4(Enrich)-->id5(Next steps)
    style id3 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


Getting started with sending events using the JavaScript tracker is very similar to other web analytics vendors like Google Analytics and Adobe Analytics.

We will be setting up two key events that are needed for fractribution: page_views and conversions.

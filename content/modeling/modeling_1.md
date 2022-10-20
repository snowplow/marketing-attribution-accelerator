+++
title = "Install Fractribution dbt Package"
weight = 1
post = ""
+++

We will use the *snowplow_web_page_views* table created by the [snowplow-web](https://hub.getdbt.com/snowplow/snowplow_web/latest/) dbt package, as well as a Snowplow events table, to create a fractional attribution report table. This table provides the marginal contribution of each channel to a user-level conversion event as well as the monetary value attributed to that channel from the conversion event. It will also contain spend information and calculated ROAS per channel. 

As such, this tutorial assumes that you have already run the `snowplow-web` dbt package. If not, instructions can be found in the [Advanced Analytics for Web](https://docs.snowplow.io/accelerators/web) accelerator.


#### **Step 1:** Add fractribution package
Add the fractribution package to your packages.yml file. The latest version can be found [here](https://hub.getdbt.com/snowplow/fractribution/latest/). You should already have the snowplow_web package present in the packages.yml file.

```yml
packages:
  - package: snowplow/snowplow_web
    version: 0.9.2
  - package: snowplow/fractribution
    version: 0.0.1
```

***

#### **Step 2:** Install the package
Install the package by running:

```
dbt deps
```


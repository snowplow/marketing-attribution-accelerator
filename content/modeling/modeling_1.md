+++
title = "Install Fractribution dbt dackage"
weight = 1
post = ""
+++


#### **Step 1:** Add snowplow_fractribution package
Add the snowplow_fractribution package to your packages.yml file. You should already have the snowplow_web package present in the packages.yml file.

{{% notice info %}}
Please note that this accelerator currently only supports v0.1.0 of the snowplow_fractribution package.
{{% /notice %}}

```yml
packages:
  - package: snowplow/snowplow_fractribution
    version: 0.1.0
  - package: snowplow/snowplow_web
    version: {{<component name="snowplow_web_latest">}}
```

***

#### **Step 2:** Install the package
Install the package by running:

```
dbt deps
```


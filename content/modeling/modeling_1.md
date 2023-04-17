+++
title = "Install Fractribution dbt dackage"
weight = 1
post = ""
+++


#### **Step 1:** Add snowplow_fractribution package
Add the latest snowplow_fractribution package to your packages.yml file. You should already have the snowplow_web package present in the packages.yml file.


```yml
packages:
  - package: snowplow/snowplow_fractribution
    version: 0.2.0
  - package: snowplow/snowplow_web
    version: {{<component name="snowplow_web_latest">}}
```


***

#### **Step 2:** Install the package
Install the package by running:

```
dbt deps
```


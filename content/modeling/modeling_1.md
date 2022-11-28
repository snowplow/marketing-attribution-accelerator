+++
title = "Install Fractribution dbt dackage"
weight = 1
post = ""
+++


#### **Step 1:** Add snowplow_fractribution package
Add the snowplow_fractribution package to your packages.yml file. The latest version can be found [here](https://hub.getdbt.com/snowplow/snowplow_fractribution/latest/). You should already have the snowplow_web package present in the packages.yml file.

```yml
packages:
  - package: snowplow/snowplow_web
    version: 0.9.3
  - package: snowplow/snowplow_fractribution
    version: 0.0.1
```

***

#### **Step 2:** Install the package
Install the package by running:

```
dbt deps
```


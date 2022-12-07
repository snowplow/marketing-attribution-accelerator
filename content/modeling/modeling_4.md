+++
title= "Create Fractribution report table"
weight = 4
post = ""
+++

Data from the snowplow_fractribution dbt package should now be in your warehouse. Next we need to create the report table. There are two ways to to this - by pulling a Docker container image or with Python locally, using the scripts in the `utils` folder in the dbt package. 


***
{{< tabs groupId="modeling" >}}
{{% tab name="Docker" %}}
To run the fractribution script using Docker, make sure that you have [Docker](https://www.docker.com/products/docker-desktop/) installed.

Once you have docker installed, you can pull the image from the Docker Hub:

```
docker pull snowplow/snowplow_fractribution
```

***
You can optionally choose a specific attribution model from the following:
- shapley (default): Takes the weighted average of the marginal contributions of each channel to a conversion.
- first_touch: Assigns 100% attribution to the first channel in each path.
- last_touch: Assigns 100% attribution to the last channel in each path.
- position_based: The first and last channels get 40% of the credit each, with the remaining
    channels getting the leftover 20% distributed evenly.
- linear: Assigns attribution evenly between all channels on the path.

| ![Attribution models](../images/attribution_models.png) |
|:--:|
| Attribution Models |

***
Add your connection parameters to an environment file (e.g. configs.env). For example:
```
snowflake_account=my_account
snowflake_user=sf_user
snowflake_password=password
snowflake_user_role=special_role
snowflake_warehouse=warehouse_name
snowflake_database=database_name
snowflake_schema=schema_name
conversion_window_start_date='2022-06-03'
conversion_window_end_date='2022-08-01'
# Add a variable if you wish to change the attribution model, e.g.:
attribution_model=shapley
```

Then run the Docker image and pass in the filepath of the .env file:

```
docker run --rm --env-file /path/to/env/file/configs.env -it snowplow/snowplow_fractribution 
```
The output of the fractribution analysis will be built into the schema specified in your connection parameters. The table will be called report_table.

{{% /tab %}}
{{% tab name="Python" %}}


Python scripts and requirements.txt can be found at `[dbt_project_name]/dbt_packages/snowplow_fractribution/utils/`. To run the fractribution script locally in Python, we recommend using a virtual environment. If you have an Apple M1, please see section **M1 Instructions**.
Snowpark requires Python 3.8. To use conda:

```
conda create --name fractribution_env -c https://repo.anaconda.com/pkgs/snowflake python=3.8 absl-py
conda activate fractribution_env
```
***
**M1 Instructions**

There is an issue with running Snowpark on M1 chips. A workaround recommended by Snowflake is to set up a virtual environment that uses x86 Python:

```
CONDA_SUBDIR=osx-64 conda create -n fractribution_env python=3.8 absl-py -c https://repo.anaconda.com/pkgs/snowflake
conda activate fractribution_env
conda config --env --set subdir osx-64
```
***
To install snowpark in this environment (all computers):

```
conda install snowflake-snowpark-python
```

You now need to set the connection parameters to your Snowflake warehouse on the command line by replacing the values after the = signs:

```
export snowflake_account=my_account\
export snowflake_user=sf_user\
export snowflake_password=password\
export snowflake_user_role=special_role\
export snowflake_warehouse=warehouse_name\
export snowflake_database=database_name\
export snowflake_schema=schema_name
```
***
Now you can run the fractribution script. You can optionally choose a specific attribution model from the following:
- shapley (default): Takes the weighted average of the marginal contributions of each channel to a conversion
- first_touch: Assigns 100% attribution to the first channel in each path.
- last_touch: Assigns 100% attribution to the last channel in each path.
- position_based: The first and last channels get 40% of the credit each, with the remaining
    channels getting the leftover 20% distributed evenly.
- linear: Assigns attribution evenly between all channels on the path.

| ![Attribution models](../images/attribution_models.png) |
|:--:|
| Attribution Models |

If you wish to use the default (shapley), no model flag is needed. But you do need to specify the start and end dates for the conversion window:

```
python main_snowplow_snowflake.py --conversion_window_start_date '2022-06-03' --conversion_window_end_date '2022-08-01'
```

Otherwise you may add a flag indicating the attribution model to use, e.g.:

```
python main_snowplow_snowflake.py --conversion_window_start_date '2022-06-03' --conversion_window_end_date '2022-08-01' --attribution_model shapley
```
The output of the fractribution analysis will be built into the schema specified in your connection parameters. There are three tables that will be created are: 
- `snowplow_fractribution_report_table`: The main output table that shows conversions, revenue, spend and ROAS per channel.
- `snowplow_fractribution_channel_attribution`: The conversion and revenue attribution per channel (used to create the report table).
- `snowplow_fractribution_path_summary_with_channels`: An intermediate table that shows, for each unique path, a summary of conversions, non conversions and revenue, as well as which channels were assigned a contribution.

{{% /tab %}}
{{</tabs >}}

{{% notice info %}}
If you would like to learn more about Fractional Attribution works, please see these [slides](https://github.com/google/fractribution/blob/master/Fractribution_Slides.pdf) and this [document](https://support.google.com/analytics/answer/3191594?hl=en#algorithm)
{{% /notice %}}
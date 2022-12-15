+++
title = "Data upload"
weight = 1
post = ""
+++

There are a number of options to load the sample Snowplow data to your Snowflake warehouse. Select the most suitable for your project below.

{{% attachments style="blue" %}}
{{% /attachments %}}

{{< tabs groupId="select_upload_sf" >}}

{{% tab name="Snowflake Web Interface" %}}

Download the `upload.zip` folder which contains the `sample_events_fractribution.csv` and the `snowflake_upload.py` files. You will only need `sample_events_fractribution.csv` to load the sample data to the Snowflake warehouse using the `Snowflake Web Interface`.

For more details please check out the official [Snowflake documentation](https://docs.snowflake.com/en/user-guide/data-load-web-ui.html).

#### **Step 1:**  Create the ATOMIC schema
If the ATOMIC schema doesn't exist, create it in your target database.

```sql
CREATE SCHEMA IF NOT EXISTS TARGET_DB.ATOMIC
```

***

#### **Step 2:**  Create the SAMPLE_EVENTS_FRACTRIBUTION_BASE table
This is where you will load the sample data to. You will need to modify the TARGET_DB according to your own database.


```sql
  CREATE OR REPLACE TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION_BASE (

	APP_ID VARCHAR(255),
	PLATFORM VARCHAR(255),
	ETL_TSTAMP TIMESTAMP_NTZ(9),
	COLLECTOR_TSTAMP TIMESTAMP_NTZ(9) NOT NULL,
	DVCE_CREATED_TSTAMP TIMESTAMP_NTZ(9),
	EVENT VARCHAR(128),
	EVENT_ID VARCHAR(36) NOT NULL,
	TXN_ID NUMBER(38,0),
	NAME_TRACKER VARCHAR(128),
	V_TRACKER VARCHAR(100),
	V_COLLECTOR VARCHAR(100),
	V_ETL VARCHAR(100),
	USER_ID VARCHAR(255),
	USER_IPADDRESS VARCHAR(128),
	USER_FINGERPRINT VARCHAR(128),
	DOMAIN_USERID VARCHAR(128),
	DOMAIN_SESSIONIDX NUMBER(38,0),
	NETWORK_USERID VARCHAR(128),
	GEO_COUNTRY VARCHAR(2),
	GEO_REGION VARCHAR(3),
	GEO_CITY VARCHAR(75),
	GEO_ZIPCODE VARCHAR(15),
	GEO_LATITUDE FLOAT,
	GEO_LONGITUDE FLOAT,
	GEO_REGION_NAME VARCHAR(100),
	IP_ISP VARCHAR(100),
	IP_ORGANIZATION VARCHAR(128),
	IP_DOMAIN VARCHAR(128),
	IP_NETSPEED VARCHAR(100),
	PAGE_URL VARCHAR(4096),
	PAGE_TITLE VARCHAR(2000),
	PAGE_REFERRER VARCHAR(4096),
	PAGE_URLSCHEME VARCHAR(16),
	PAGE_URLHOST VARCHAR(255),
	PAGE_URLPORT NUMBER(38,0),
	PAGE_URLPATH VARCHAR(3000),
	PAGE_URLQUERY VARCHAR(6000),
	PAGE_URLFRAGMENT VARCHAR(3000),
	REFR_URLSCHEME VARCHAR(16),
	REFR_URLHOST VARCHAR(255),
	REFR_URLPORT NUMBER(38,0),
	REFR_URLPATH VARCHAR(6000),
	REFR_URLQUERY VARCHAR(6000),
	REFR_URLFRAGMENT VARCHAR(3000),
	REFR_MEDIUM VARCHAR(25),
	REFR_SOURCE VARCHAR(50),
	REFR_TERM VARCHAR(255),
	MKT_MEDIUM VARCHAR(255),
	MKT_SOURCE VARCHAR(255),
	MKT_TERM VARCHAR(255),
	MKT_CONTENT VARCHAR(500),
	MKT_CAMPAIGN VARCHAR(255),
	SE_CATEGORY VARCHAR(1000),
	SE_ACTION VARCHAR(1000),
	SE_LABEL VARCHAR(4096),
	SE_PROPERTY VARCHAR(1000),
	SE_VALUE FLOAT,
	TR_ORDERID VARCHAR(255),
	TR_AFFILIATION VARCHAR(255),
	TR_TOTAL NUMBER(18,2),
	TR_TAX NUMBER(18,2),
	TR_SHIPPING NUMBER(18,2),
	TR_CITY VARCHAR(255),
	TR_STATE VARCHAR(255),
	TR_COUNTRY VARCHAR(255),
	TI_ORDERID VARCHAR(255),
	TI_SKU VARCHAR(255),
	TI_NAME VARCHAR(255),
	TI_CATEGORY VARCHAR(255),
	TI_PRICE NUMBER(18,2),
	TI_QUANTITY NUMBER(38,0),
	PP_XOFFSET_MIN NUMBER(38,0),
	PP_XOFFSET_MAX NUMBER(38,0),
	PP_YOFFSET_MIN NUMBER(38,0),
	PP_YOFFSET_MAX NUMBER(38,0),
	USERAGENT VARCHAR(1000),
	BR_NAME VARCHAR(50),
	BR_FAMILY VARCHAR(50),
	BR_VERSION VARCHAR(50),
	BR_TYPE VARCHAR(50),
	BR_RENDERENGINE VARCHAR(50),
	BR_LANG VARCHAR(255),
	BR_FEATURES_PDF BOOLEAN,
	BR_FEATURES_FLASH BOOLEAN,
	BR_FEATURES_JAVA BOOLEAN,
	BR_FEATURES_DIRECTOR BOOLEAN,
	BR_FEATURES_QUICKTIME BOOLEAN,
	BR_FEATURES_REALPLAYER BOOLEAN,
	BR_FEATURES_WINDOWSMEDIA BOOLEAN,
	BR_FEATURES_GEARS BOOLEAN,
	BR_FEATURES_SILVERLIGHT BOOLEAN,
	BR_COOKIES BOOLEAN,
	BR_COLORDEPTH VARCHAR(12),
	BR_VIEWWIDTH NUMBER(38,0),
	BR_VIEWHEIGHT NUMBER(38,0),
	OS_NAME VARCHAR(50),
	OS_FAMILY VARCHAR(50),
	OS_MANUFACTURER VARCHAR(50),
	OS_TIMEZONE VARCHAR(255),
	DVCE_TYPE VARCHAR(50),
	DVCE_ISMOBILE BOOLEAN,
	DVCE_SCREENWIDTH NUMBER(38,0),
	DVCE_SCREENHEIGHT NUMBER(38,0),
	DOC_CHARSET VARCHAR(128),
	DOC_WIDTH NUMBER(38,0),
	DOC_HEIGHT NUMBER(38,0),
	TR_CURRENCY VARCHAR(3),
	TR_TOTAL_BASE NUMBER(18,2),
	TR_TAX_BASE NUMBER(18,2),
	TR_SHIPPING_BASE NUMBER(18,2),
	TI_CURRENCY VARCHAR(3),
	TI_PRICE_BASE NUMBER(18,2),
	BASE_CURRENCY VARCHAR(3),
	GEO_TIMEZONE VARCHAR(64),
	MKT_CLICKID VARCHAR(128),
	MKT_NETWORK VARCHAR(64),
	ETL_TAGS VARCHAR(500),
	DVCE_SENT_TSTAMP TIMESTAMP_NTZ(9),
	REFR_DOMAIN_USERID VARCHAR(128),
	REFR_DVCE_TSTAMP TIMESTAMP_NTZ(9),
	DOMAIN_SESSIONID VARCHAR(128),
	DERIVED_TSTAMP TIMESTAMP_NTZ(9),
	EVENT_VENDOR VARCHAR(1000),
	EVENT_NAME VARCHAR(1000),
	EVENT_FORMAT VARCHAR(128),
	EVENT_VERSION VARCHAR(128),
	EVENT_FINGERPRINT VARCHAR(128),
	TRUE_TSTAMP TIMESTAMP_NTZ(9),
	LOAD_TSTAMP TIMESTAMP_NTZ(9),
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1 VARIANT,
	constraint EVENT_ID_PK primary key (EVENT_ID)
);
```

***

#### **Step 3:** Load the data

{{% notice info %}}
Please note that the instructions are only valid when using the Snowflake Classic Console!
{{% /notice %}}

3.1 Log into your web interface and click on `Databases` tab.

3.2 Locate the **SAMPLE_EVENTS_FRACTRIBUTION_BASE** table that you just created and select it.

3.3 Click the `Load Data` button to open the Load Data wizard.

3.4 Select the relevant warehouse from the dropdown list. Click `Next`.

3.5 Within the `Source Files` section select `Load files from your computer` option and click the `Select Files` button. If you have not saved the sample file provided as an attachment above please do so.
Navigate to the **sample_events_fractribution.csv** file and click the `Upload` then the `Next` button.

3.6 Create a new File Format with the plus (+) symbol beside the dropdown list, give it a name and change the following settings of the default csv file formats:
- `Header lines to skip`= 1
- `Field optionally enclosed by`= Double Quote

3.7 Click the `Load` button (no need to alter the Load Options). Loading should take place within a couple of minutes.

For more details please check out the official [Snowflake documentation](https://docs.snowflake.com/en/user-guide/data-load-web-ui.html).

***

#### **Step 4:** Create the **ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION** table


```sql
CREATE OR REPLACE TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION AS (

SELECT
	APP_ID,
	PLATFORM,
	ETL_TSTAMP,
	COLLECTOR_TSTAMP,
	DVCE_CREATED_TSTAMP,
	EVENT,
	EVENT_ID,
	TXN_ID,
	NAME_TRACKER,
	V_TRACKER,
	V_COLLECTOR,
	V_ETL,
	USER_ID,
	USER_IPADDRESS,
	USER_FINGERPRINT,
	DOMAIN_USERID,
	DOMAIN_SESSIONIDX,
	NETWORK_USERID,
	GEO_COUNTRY,
	GEO_REGION,
	GEO_CITY,
	GEO_ZIPCODE,
	GEO_LATITUDE,
	GEO_LONGITUDE,
	GEO_REGION_NAME,
	IP_ISP,
	IP_ORGANIZATION,
	IP_DOMAIN,
	IP_NETSPEED,
	PAGE_URL,
	PAGE_TITLE,
	PAGE_REFERRER,
	PAGE_URLSCHEME,
	PAGE_URLHOST,
	PAGE_URLPORT,
	PAGE_URLPATH,
	PAGE_URLQUERY,
	PAGE_URLFRAGMENT,
	REFR_URLSCHEME,
	REFR_URLHOST,
	REFR_URLPORT,
	REFR_URLPATH,
	REFR_URLQUERY,
	REFR_URLFRAGMENT,
	REFR_MEDIUM,
	REFR_SOURCE,
	REFR_TERM,
	MKT_MEDIUM,
	MKT_SOURCE,
	MKT_TERM,
	MKT_CONTENT,
	MKT_CAMPAIGN,
	SE_CATEGORY,
	SE_ACTION,
	SE_LABEL,
	SE_PROPERTY,
	SE_VALUE,
	TR_ORDERID,
	TR_AFFILIATION,
	TR_TOTAL,
	TR_TAX,
	TR_SHIPPING,
	TR_CITY,
	TR_STATE,
	TR_COUNTRY,
	TI_ORDERID,
	TI_SKU,
	TI_NAME,
	TI_CATEGORY,
	TI_PRICE,
	TI_QUANTITY,
	PP_XOFFSET_MIN,
	PP_XOFFSET_MAX,
	PP_YOFFSET_MIN,
	PP_YOFFSET_MAX,
	REPLACE(USERAGENT, '\"', '') as USERAGENT,
	BR_NAME,
	BR_FAMILY,
	BR_VERSION,
	BR_TYPE,
	BR_RENDERENGINE,
	BR_LANG,
	BR_FEATURES_PDF,
	BR_FEATURES_FLASH,
	BR_FEATURES_JAVA,
	BR_FEATURES_DIRECTOR,
	BR_FEATURES_QUICKTIME,
	BR_FEATURES_REALPLAYER,
	BR_FEATURES_WINDOWSMEDIA,
	BR_FEATURES_GEARS,
	BR_FEATURES_SILVERLIGHT,
	BR_COOKIES,
	BR_COLORDEPTH,
	BR_VIEWWIDTH,
	BR_VIEWHEIGHT,
	OS_NAME,
	OS_FAMILY,
	OS_MANUFACTURER,
	OS_TIMEZONE,
	DVCE_TYPE,
	DVCE_ISMOBILE,
	DVCE_SCREENWIDTH,
	DVCE_SCREENHEIGHT,
	DOC_CHARSET,
	DOC_WIDTH,
	DOC_HEIGHT,
	TR_CURRENCY,
	TR_TOTAL_BASE,
	TR_TAX_BASE,
	TR_SHIPPING_BASE,
	TI_CURRENCY,
	TI_PRICE_BASE,
	BASE_CURRENCY,
	GEO_TIMEZONE,
	MKT_CLICKID,
	MKT_NETWORK,
	ETL_TAGS,
	DVCE_SENT_TSTAMP,
	REFR_DOMAIN_USERID,
	REFR_DVCE_TSTAMP,
	DOMAIN_SESSIONID,
	DERIVED_TSTAMP,
	EVENT_VENDOR,
	EVENT_NAME,
	EVENT_FORMAT,
	EVENT_VERSION,
	EVENT_FINGERPRINT,
	TRUE_TSTAMP,
	LOAD_TSTAMP,
	PARSE_JSON(REPLACE(REPLACE(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1,'\"', ''),'''','\"')) as CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1

FROM ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION_BASE )

```

***

#### **Step 5:**  Drop the **SAMPLE_EVENTS_FRACTRIBUTION_BASE** table

```sql
DROP TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION_BASE
```
You will now have the ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION created and loaded with sample data.

{{% /tab %}}

{{% tab name="Python" %}}

Download the `upload.zip` folder which contains the `sample_events_fractribution.csv` and the `snowflake_upload.py` files. You will need both to load the sample data to the Snowflake warehouse with Python.

#### **Step 1:**  Set up your environment

Set up a virtual environment (recommended) and install the [snowflake-connector-python](https://pypi.org/project/snowflake-connector-python/) package (tested with version 2.7.12).

Unzip the downloaded `upload.zip` file then navigate to the upload folder that contains the `snowflake_upload.py` script.

Create and activate the virtual environment, then install `snowflake-connector-python`:

```bash
pipenv shell
pipenv install snowflake-connector-python==2.7.12
```

#### **Step 2:** Change variables and connection details

Open the `snowflake_upload.py` file and edit the following variables.

##### 2.1 Connection details - update username, password and account
```python
user = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
account = 'YOUR_ACCOUNT'
```

##### 2.2 Variables to be modified - warehouse and database
```python
warehouse='YOUR_WAREHOUSE'
database = 'YOUR_DB
```
##### 2.3 Path to the sample_events_fractribution.csv
```python
csv_file = '/path/to/sample_events_fractribution.csv'
```

#### **Step 3:** Upload Data
Run `snowflake_upload.py`.
```bash
python3 snowflake_upload.py
```

It should finish execution within a minute. You should be alerted as soon as each intermediary step finishes:

```
Schema created
Staging table YOUR_DB.ATOMIC.SAMPLE_EVENTS_STAGED_FRACTRIBUTION is created
Stage dropped, if applicable
Stage created
File put to stage
Data loaded into staging table
Target table: YOUR_DB.ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION is created
Staging table: YOUR_DB.ATOMIC.SAMPLE_EVENTS_STAGED_FRACTRIBUTION is dropped
```
You will now have the ATOMIC.SAMPLE_EVENTS_FRACTRIBUTION created and loaded with sample data.

{{% /tab %}}
{{< /tabs >}}

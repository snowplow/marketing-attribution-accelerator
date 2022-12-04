+++
title = "Example Table and Visualisation"
post = ""
weight = 1
+++

Below is an example of a fractional attribution report table, which shows the calculated ROAS by attribution channel. 

| conversionWindowStartDate | conversionWindowEndDate | channel           | conversions | revenue | spend  | roas |
| ------------------------- | ----------------------- | ----------------- | ----------- | ------- | ------ | ---- |
| 2022-06-03                | 2022-08-01              | Direct            | 699.8       | 137050.5| 10000.0| 13.7 |
| 2022-06-03                | 2022-08-01              | Organic_Search    | 269.5       | 23292.3 | 10000.0| 2.33 |
| 2022-06-03                | 2022-08-01              | Paid_Search_Other | 50.4        | 4875.5  | 10000.0| 0.49 |
| 2022-06-03                | 2022-08-01              | Display_Other     | 21.3        | 2069.0  | 10000.0| 0.21 |
| 2022-06-03                | 2022-08-01              | Referral          | 12.4        | 653.3   | 10000.0| 0.07 |
| 2022-06-03                | 2022-08-01              | Unmatched_Channel | 4.08        | 544.6   | 10000.0| 0.05 |
| 2022-06-03                | 2022-08-01              | Video             | 1.5         | 29.5    | 10000.0| 0.003|

This table shows the ROAS figures for each channel during the conversion window specified. It also shows the conversions attributed to each channel, and the revenue associated with that channel. In our example we have a uniform spend ($10000) for each channel but you can substitute and join this to your own internal dataset to accurately account for spend and ROAS for your own marketing budgets, see [Next steps](/accelerators/fractribution/next_steps/next_steps_1/).

***

For comparison, below is an example of the output of running a traditional last-touch attribution model on the same sample data - [example instructions here](https://docs.snowplow.io/docs/tutorials/tutorial-first-and-last-touch-attribution/). The arrows beside the values indicate the direction of the difference in attribution calculated.

| conversionWindowStartDate | conversionWindowEndDate | channel           | conversions | revenue    | spend  | roas    |
| ------------------------- | ----------------------- | ----------------- | ----------- | ---------- | ------ | ------- |
| 2022-06-03                | 2022-08-01              | Direct            | (↓)  687     | (↓)  121247.1| 10000.0| (↓)  12.1 |
| 2022-06-03                | 2022-08-01              | Organic_Search    | (↑)  289     | (↑)  26409.3 | 10000.0| (↑)  2.64 |
| 2022-06-03                | 2022-08-01              | Paid_Search_Other | (↓)  44      | (↓)  3743.0  | 10000.0| (↓)  0.37 |
| 2022-06-03                | 2022-08-01              | Display_Other     | (↓)  18      | (↓)  1727.1  | 10000.0| (↓)  0.17 |
| 2022-06-03                | 2022-08-01              | Referral          | (↑)  14      | (↑)  788.8   | 10000.0| (↑)  0.08 |
| 2022-06-03                | 2022-08-01              | Unmatched_Channel | (↓)  4       | (↓)  517.7   | 10000.0| ()  0.05 |
| 2022-06-03                | 2022-08-01              | Video             | (↓)  1       | (↓)  8.49    | 10000.0| (↓)  0.001|

***

The above fractional attribution data can also be visualised, for example:
![conversions_and_roas](../images/conversions_roas_browser.png)
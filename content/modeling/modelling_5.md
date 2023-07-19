+++
title= "Using this package for non-value based conversions"
weight = 4
post = ""
+++

This package can also be used for non-value based conversions, however, the outputs may look somewhat strange.

For example, if you have a column in your events/conversions table with a 1 for a form submission, and a 0 for no submission, you can specify this field in the conversion_value macro (e.g. `form_submitted`) and add a clause in the conversion_clause macro (e.g. `form_submitted = 1`).

You can then run the attribution analysis using this column instead of a revenue column. An example output of the report table would look like this:

| conversion_window_start_date | conversion_window_end_date | channel           | conversions | revenue | spend   | roas    |
| ---------------------------- | -------------------------- | ----------------- | ----------- | ------- | ------- | ------- |
| 2022-06-03                   | 2022-08-01                 | Direct            | 699.8       | 699.8   | 10000.0 | 0.06997 |
| 2022-06-03                   | 2022-08-01                 | Organic_Search    | 269.5       | 269.5   | 10000.0 | 0.02695 |
| 2022-06-03                   | 2022-08-01                 | Paid_Search_Other | 50.4        | 50.4    | 10000.0 | 0.00504 |
| 2022-06-03                   | 2022-08-01                 | Display_Other     | 21.3        | 21.3    | 10000.0 | 0.00213 |
| 2022-06-03                   | 2022-08-01                 | Referral          | 12.4        | 12.4    | 10000.0 | 0.00123 |
| 2022-06-03                   | 2022-08-01                 | Unmatched_Channel | 4.08        | 4.08    | 10000.0 | 0.00040 |
| 2022-06-03                   | 2022-08-01                 | Video             | 1.5         | 1.5     | 10000.0 | 0.00014 |

Note that 'revenue' in this table is now being calculated based on the form_submitted column in the events/conversions table, where a conversion will only ever have a value of 1. This is why the values for conversions and revenue are identical.

You will notice that the values for ROAS in this example are extremely small. In a value-based calculation of ROAS, one conversion is generally associated with a value much greater than 1 (e.g. one conversion can have a purchase value of $100, etc.). When we calculate ROAS using one conversion equal to a value of 1, the ROAS figures can look very small depending on the number of conversions and the amount spent per channel.

+++
title = "Tracking Events"
weight = 2
+++

The trackers create data on user **actions** at a specific point in time. For example:

- Loading a web page
- Clicking a link
- Submitting a form

A number of tracking events are available out of the box. These include, but aren't limited to:

- Page views
- Heartbeats (Page Pings)
- Link clicks
- HTML form actions

***

#### Pageviews
In this section, we will implement page views.

#### **Step 1:** Track Page View
To track a page view, simply call `trackPageView'.

```javascript
snowplow('trackPageView')
```


#### Transaction event
In addition to pageviews, we need to track transactions in order to determine when a user has converted and how much they spent.

- **Transaction Tracking** - Captures transaction information including `transaction_id` and `revenue`.

####  **Step 2:** Perform Transaction Tracking
To perform transaction tracking, you call the `trackTransaction` method, e.g.

```javascript
snowplow('trackTransaction', {
    transaction_id: '1234',  // required
    revenue: 11.99,   // required
    payment_method: 'Credit Card', //required
    currency: 'USD', //required
    total_quantity: 1, //required
    tax: 1.29,
    shipping: 5.00
});
```

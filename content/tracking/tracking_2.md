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

{{< tabs groupId="select_js" >}}
{{% tab name="JavaScript API" %}}

#### Pageviews
In this section, we will implement page views.

#### **Step 1:** Track Page View
To track a page view, simply call `trackPageView'.

```javascript
snowplow('trackPageView')
```

#### Transaction event
In addition to pageviews, we need to track transactions in order to determine when a user has converted and how much they spent.

- **Transaction Tracking** - Captures transaction information including `orderId` and `total`.

####  **Step 2:** Perform Transaction Tracking
To perform transaction tracking, first you add an item for the transaction, create the transaction object with `addTrans`, and then call the `trackTrans` method, e.g.

```javascript
snowplow('addItem', {
    orderId: '1234',
    sku: 'P123',
    name: 'T-Shirt',      
    category: 'Green Medium',
    price: 11.99,
    quantity: 1,
    currency: 'USD'
});

snowplow('addTrans', {
    orderId: '1234',  // required
    total: 11.99,   // required
    affiliation: 'Acme Clothing', 
    tax: 1.29,
    shipping: 5,
    city: 'San Jose',
    state: 'California',
    country: 'USA',
    currency: 'USD'
});

snowplow('trackTrans');
```

For more information on the ecommerce tracking, you can take a look at the [documentation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v3/tracking-events/#ecommerce-tracking) for this plugin and its methods.

{{% /tab %}}
{{% tab name="Browser API" %}}

#### Pageviews
In this section, we will implement page views.

#### **Step 1:** Track Page View
To track a page view, simply call `trackPageView' when a new page is being shown to the user.

```javascript
import { newTracker, trackPageView, enableActivityTracking } from "@snowplow/browser-tracker";

trackPageView();
```

#### Transaction event
In addition to pageviews, we need to track transactions in order to determine when a user has converted and how much they spent.

- **Transaction Tracking** - Captures transaction information including `orderId` and `total`.

####  **Step 2:** Perform Transaction Tracking
To perform transaction tracking, first you add an item for the transaction, create the transaction object with `addTrans`, and then call the `trackTrans` method, e.g.

```javascript
import { addItem, addTrans, trackTrans } from '@snowplow/browser-plugin-ecommerce'

addItem({
    orderId: '1234',
    sku: 'P123',
    name: 'T-Shirt',      
    category: 'Green Medium',
    price: 11.99,
    quantity: 1,
    currency: 'USD'
});

addTrans({
    orderId: '1234', 
    total: 11.99,
    affiliation: 'Acme Clothing',
    tax: 1.29,
    shipping: 5,
    city: 'San Jose',
    state: 'California',
    country: 'USA',
    currency: 'USD'
});

trackTrans();
```

For more information on the ecommerce tracking, you can take a look at the [documentation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/tracking-events/#ecommerce-tracking) for this plugin and its methods.

{{% /tab %}}
{{< /tabs >}}
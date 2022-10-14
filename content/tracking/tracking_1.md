+++
title = "Setup your tracking"
weight = 1
+++
 
Follow the below steps to implement Snowplow tracking on your website or single page application.


#### **Step 1:** Download sp.js
Add the sp.js file to your project directory. The latest version can be found **[here](https://github.com/snowplow/snowplow-javascript-tracker/releases).**

***

#### **Step 2:** Add JS snippet
Add the below snippet to all of the pages you would like to track. **Make sure to update the {{Link to the sp.js file}} variable.**

Place the `<script>` tag into the `<head>` element of your page.

<!-- Typically this will be placed into the `<head>` element of your page or in a similar, suitable, location if using a Single Page Application framework. -->

```html
<script type="text/javascript" async=1 >
;(function (p, l, o, w, i, n, g) { if (!p[i]) { p.GlobalSnowplowNamespace = p.GlobalSnowplowNamespace || []; p.GlobalSnowplowNamespace.push(i); p[i] = function () { (p[i].q = p[i].q || []).push(arguments) }; p[i].q = p[i].q || []; n = l.createElement(o); g = l.getElementsByTagName(o)[0]; n.async = 1; n.src = w; g.parentNode.insertBefore(n, g) } }(window, document, "script", "{{Link to sp.js file}}", "snowplow"));
</script>
```

***

#### **Step 3:** Configure the Tracker
Call `newTracker` in the `<script>` tag, with the following arguments. This creates an instance of a basic tracker with an Ecommerce plugin that we will use on the next page.

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`

```javascript
window.snowplow('newTracker', 'sp', '{{Url for Collector}}', {
    plugins: [ EcommercePlugin() ],
})
```

<!-- **should we point the collector to mini/micro collector for testing??** -->

In addition to the basic tracker, add the below optional arguments to the tracker to make use of some of Snowplow's more advanced features.

<!-- **Optional Settings (JSON):** -->
  - `appId`: Identify events that occur on different applications
  - `platform`: Identify the platform the event occurred on, in this case `web`
  - `cookieSameSite`: Protects cookies from being accessed by third party domains

```javascript
window.snowplow('newTracker', 'sp', '{{Url for Collector}}', {
    plugins: [ EcommercePlugin() ],
    appId: 'appId',
    platform: 'web',
    cookieSameSite: 'Lax',
});
```

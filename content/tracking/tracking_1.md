+++
title = "Setup your tracking"
weight = 1
+++

Depending on your store's front-end infrastructure and Snowplow set-up, you can use either our JavaScript tracker for a `<script>` tag option or our Browser tracker for a more modern web development set-up.

In both options, the API is similar with only minor differences in the set-up and method calls.

{{< tabs groupId="package manager" >}}
{{% tab name="Script Tag" %}}
#### **Step 1:** Download sp.js
Add the sp.js file to your project directory. The latest version can be found **[here](https://github.com/snowplow/snowplow-javascript-tracker/releases).**

***

#### **Step 2:** Add JS snippet
Add the below snippet to all of the pages you would like to track. **Make sure to update the {{Link to the sp.js file}} variable.**

Place the `<script>` tag into the `<head>` element of your page.

<!-- Typically this will be placed into the `<head>` element of your page or in a similar, suitable, location if using a Single Page Application framework. -->

```html
<script type="text/javascript">
;(function (p, l, o, w, i, n, g) { if (!p[i]) { p.GlobalSnowplowNamespace = p.GlobalSnowplowNamespace || []; p.GlobalSnowplowNamespace.push(i); p[i] = function () { (p[i].q = p[i].q || []).push(arguments) }; p[i].q = p[i].q || []; n = l.createElement(o); g = l.getElementsByTagName(o)[0]; n.async = 1; n.src = w; g.parentNode.insertBefore(n, g) } }(window, document, "script", "{{Link to sp.js file}}", "snowplow"));
</script>
```

#### **Step 3:** Configure the Tracker
Call `newTracker` in the `<script>` tag, with the following arguments. This creates an instance of a basic tracker and enables some of Snowplow's more advanced features.

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`
- `appId`: Identify events that occur on different applications
- `platform`: Identify the platform the event occurred on, in this case `web`
- `cookieSameSite`: Protects cookies from being accessed by third party domains

```javascript
window.snowplow('newTracker', 'sp', '{{Url for Collector}}', {
    appId: 'appId',
    platform: 'web',
    cookieSameSite: 'Lax',
});
```

To start tracking ecommerce interactions, you need to load the `SnowplowEcommercePlugin` to your tracker. To add the plugin on the tracker and enable the usage of the e-commerce API, you should include it as shown below:

```js
window.snowplow(
  "addPlugin:sp",
  "https://cdn.jsdelivr.net/npm/@snowplow/browser-plugin-snowplow-ecommerce@3/dist/index.umd.min.js",
  ["snowplowEcommerceAccelerator", "SnowplowEcommercePlugin"]
);
```

Now the tracker has everything required to start collecting e-commerce action data. On the next step we are going to see how to use the available APIs.

{{% /tab %}}
{{% tab name="Package Manager" %}}

#### **Step 1:** Install browser-tracker package

Install the `@snowplow/browser-tracker` and `@snowplow/browser-plugin-snowplow-ecommerce` via npm, yarn or any other package manager of your choice. Example using `npm`:

```bash
npm install @snowplow/browser-tracker @snowplow/browser-plugin-snowplow-ecommerce
```

#### **Step 2:** Create the tracker

In your `src` folder, create a file called `tracker.js`. Inside it create the `tracker` object using the snippet below to use it anywhere in the application. We also provide additional options which enable some of Snowplow's more advanced features

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`
- `appId`: Identify events that occur on different applications
- `platform`: Identify the platform the event occurred on, in this case `web`
- `cookieSameSite`: Protects cookies from being accessed by third party domains

```javascript
import { newTracker } from "@snowplow/browser-tracker";

export const tracker = newTracker("sp", "{{Url for Collector}}", {
  appId: 'appId',
  platform: 'web',
  cookieSameSite: 'Lax',
});
```

#### **Step 3:** Configure the tracker to use the `SnowplowEcommercePlugin`

To allow the tracker to use e-commerce methods from the SnowplowEcommercePlugin, you need to include during the initialization of the tracker. By adding it on the plugins array, you gain access to the full functionality:

```javascript
import { newTracker } from "@snowplow/browser-tracker";
import { SnowplowEcommercePlugin } from "@snowplow/browser-plugin-snowplow-ecommerce";

export const tracker = newTracker("sp", "{{Url for Collector}}", {
  /* tracker options */
  plugins: [SnowplowEcommercePlugin()],
});
```

Now the tracker has everything required to start collecting e-commerce action data. On the next step we are going to see how to use the available APIs.

{{% /tab %}}
{{< /tabs >}}

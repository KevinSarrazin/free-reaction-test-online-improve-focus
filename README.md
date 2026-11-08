# Free reaction test online

Other languages: [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

A free reaction time test that runs in your browser, in a single HTML file.

Try it online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/

Wait for the panel to change color, then click, tap or press Space as fast as you can. After ten trials you get:

- **Mean**: your average time.
- **Median**: the middle value, which one slip moves less than the mean.
- **Fastest**: your best trial.
- **Spread**: the standard deviation. Lower means steadier.
- **False starts**: clicks before the color change. The trial is repeated.

The last ten series are kept in your browser's local storage. Nothing is sent anywhere: no tracking, no external script, no sign-up.

## Run it

Open `index.html` in any browser. No build step and no dependency.

## Reading the result

Most adults land between 200 and 300 ms on a simple visual test like this one. The screen, the mouse or touch screen and the browser each add a few milliseconds, so compare yourself with yourself, on the same device. Sleep, fatigue, caffeine and the time of day all shift the result.

This test measures a simple reaction time. It is not a diagnosis, and it is not a clinical attention test.

## Embed the test on your website

You can show the full reaction time test from upchin.app on your own page, free. It is available in 17 languages: set `data-lang` (or `lang=` in the frame address) to `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**With the script** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), which adjusts the height of the frame to its content:

```html
<div data-upchin-embed="reaction-time-test" data-lang="en">
  <p>Reaction time test by <a href="https://upchin.app/tools/reaction-time-test">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Without a script**, if your site only accepts HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=en" title="Reaction time test" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Reaction time test by <a href="https://upchin.app/tools/reaction-time-test">Upchin</a></p>
```

Please keep the credit line below the test. The script adds the frame next to it and never removes it.

## Full version

The [reaction time test on upchin.app](https://upchin.app/tools/reaction-time-test) is available in 17 languages. It keeps your history, explains each number and lets you share a result.

This test is made by the team behind Upchin. In the words of its website: “Your apps are designed to keep you scrolling. Upchin is designed to give you your time back.” The iPhone app uses Apple's Screen Time to help you [reduce screen time](https://upchin.app/), with friction at the right moment rather than a lecture.

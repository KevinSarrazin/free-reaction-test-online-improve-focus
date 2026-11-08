# मुफ़्त ऑनलाइन रिएक्शन टेस्ट

दूसरी भाषाएँ: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

आपके ब्राउज़र में चलने वाला मुफ़्त रिएक्शन टाइम टेस्ट, एक ही HTML फ़ाइल में।

ऑनलाइन आज़माएँ: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/hi/

पैनल का रंग बदलने तक इंतज़ार करें, फिर जितनी जल्दी हो सके क्लिक या टैप करें, या Space दबाएँ। दस प्रयासों के बाद आपको मिलता है:

- **औसत**: आपका औसत समय।
- **मीडियन**: बीच वाली वैल्यू, जिस पर एक चूक का असर औसत से कम होता है।
- **सबसे तेज़**: आपका सबसे अच्छा प्रयास।
- **उतार-चढ़ाव**: स्टैंडर्ड डेविएशन। जितना कम, उतना स्थिर।
- **फ़ॉल्स स्टार्ट**: रंग बदलने से पहले किए गए क्लिक। वह प्रयास दोबारा होता है।

आख़िरी दस सीरीज़ आपके ब्राउज़र के लोकल स्टोरेज में सेव रहती हैं। कुछ भी कहीं नहीं भेजा जाता: न ट्रैकिंग, न कोई बाहरी स्क्रिप्ट, न साइन-अप।

## चलाएँ

`index.html` को किसी भी ब्राउज़र में खोलें। न बिल्ड स्टेप, न कोई डिपेंडेंसी।

## नतीजा कैसे समझें

इस तरह के आसान विज़ुअल टेस्ट में ज़्यादातर वयस्क 200 से 300 ms के बीच रहते हैं। स्क्रीन, माउस या टच स्क्रीन, और ब्राउज़र, हर एक कुछ मिलीसेकंड जोड़ता है, इसलिए अपनी तुलना ख़ुद से ही करें, और उसी डिवाइस पर। नींद, थकान, कैफ़ीन और दिन का समय, सब नतीजे पर असर डालते हैं।

यह टेस्ट सिंपल रिएक्शन टाइम मापता है। यह कोई डायग्नोसिस नहीं है, और न ही ध्यान का कोई क्लिनिकल टेस्ट।

## इस टेस्ट को अपनी वेबसाइट पर जोड़ें

आप upchin.app का पूरा रिएक्शन टाइम टेस्ट अपने पेज पर मुफ़्त दिखा सकते हैं। यह 17 भाषाओं में उपलब्ध है: `data-lang` (या फ़्रेम के पते में `lang=`) में इनमें से कोई एक कोड डालें: `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`।

**स्क्रिप्ट के साथ** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), जो फ़्रेम की ऊँचाई उसके कंटेंट के हिसाब से अपने आप ठीक कर देती है:

```html
<div data-upchin-embed="reaction-time-test" data-lang="hi">
  <p><a href="https://upchin.app/hi/tools/reaction-time-test">Upchin</a> का रिएक्शन टाइम टेस्ट</p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**बिना स्क्रिप्ट के**, अगर आपकी साइट सिर्फ़ HTML स्वीकार करती है:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=hi" title="रिएक्शन टाइम टेस्ट" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p><a href="https://upchin.app/hi/tools/reaction-time-test">Upchin</a> का रिएक्शन टाइम टेस्ट</p>
```

कृपया टेस्ट के नीचे वाली क्रेडिट लाइन रहने दें। स्क्रिप्ट फ़्रेम को उसके बगल में जोड़ती है और उसे कभी नहीं हटाती।

## पूरा वर्ज़न

[upchin.app पर रिएक्शन टाइम टेस्ट](https://upchin.app/hi/tools/reaction-time-test) 17 भाषाओं में उपलब्ध है। यह आपकी हिस्ट्री सँभालकर रखता है, हर आँकड़े का मतलब समझाता है और नतीजा शेयर करने देता है।

यह टेस्ट Upchin की टीम ने बनाया है। उसकी वेबसाइट के शब्दों में: “आपकी ऐप इस तरह बनी हैं कि स्क्रॉल कभी न रुके। Upchin इसलिए बना है कि आपका समय आपको लौटा सके।” यह iPhone ऐप Apple के स्क्रीन टाइम फ़ीचर का इस्तेमाल करती है, ताकि आप [स्क्रीन टाइम कम कर सकें](https://upchin.app/hi): बिना उपदेश दिए, सही पल पर थोड़ी रुकावट के साथ।

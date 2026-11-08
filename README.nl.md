# Gratis reactietest online

Andere talen: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Een gratis reactietest die in je browser draait, in één HTML-bestand.

Probeer hem online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/nl/

Wacht tot het vlak van kleur verandert en klik, tik of druk dan zo snel als je kunt op de spatiebalk. Na tien pogingen krijg je:

- **Gemiddelde**: je gemiddelde tijd.
- **Mediaan**: de middelste waarde, die door één misser minder verschuift dan het gemiddelde.
- **Snelste**: je beste poging.
- **Regelmaat**: de standaardafwijking. Hoe lager, hoe regelmatiger.
- **Valse starts**: klikken vóór de kleurwissel. De poging wordt herhaald.

De laatste tien reeksen worden bewaard in de lokale opslag van je browser. Er wordt niets verstuurd: geen tracking, geen extern script, geen account.

## Starten

Open `index.html` in een willekeurige browser. Geen buildstap en geen afhankelijkheden.

## Het resultaat lezen

De meeste volwassenen komen bij een eenvoudige visuele test als deze uit tussen 200 en 300 ms. Het scherm, de muis of het touchscreen en de browser voegen elk een paar milliseconden toe, dus vergelijk jezelf met jezelf, op hetzelfde apparaat. Slaap, vermoeidheid, cafeïne en het tijdstip van de dag beïnvloeden allemaal het resultaat.

Deze test meet een eenvoudige reactietijd. Het is geen diagnose en geen klinische aandachtstest.

## Zet de test op je website

Je kunt de volledige reactietest van upchin.app gratis op je eigen pagina tonen. Hij is beschikbaar in 17 talen: zet `data-lang` (of `lang=` in het adres van het frame) op `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Met het script** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), dat de hoogte van het frame aan de inhoud aanpast:

```html
<div data-upchin-embed="reaction-time-test" data-lang="nl">
  <p>Reactietest door <a href="https://upchin.app/nl/tools/reactietest">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Zonder script**, als je site alleen HTML accepteert:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=nl" title="Reactietest" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Reactietest door <a href="https://upchin.app/nl/tools/reactietest">Upchin</a></p>
```

Laat de bronvermelding onder de test alsjeblieft staan. Het script plaatst het frame ernaast en haalt de vermelding nooit weg.

## Volledige versie

De [reactietest op upchin.app](https://upchin.app/nl/tools/reactietest) is beschikbaar in 17 talen. Hij bewaart je geschiedenis, legt elk getal uit en laat je een resultaat delen.

Deze test is gemaakt door het team achter Upchin. In de woorden van de website: ‘Apps zijn gemaakt om je te laten blijven scrollen. Upchin is gemaakt om je die tijd terug te geven.’ De iPhone-app gebruikt Schermtijd van Apple om je te helpen [je schermtijd te verminderen](https://upchin.app/nl), met frictie op het juiste moment in plaats van een opgeheven vingertje.

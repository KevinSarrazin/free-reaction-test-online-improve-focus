# Gratis reaktionstest online

Andre sprog: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

En gratis reaktionstest, der kører i din browser, i én enkelt HTML-fil.

Prøv den online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/da/

Vent, til feltet skifter farve, og klik, tryk på skærmen eller brug mellemrumstasten så hurtigt som muligt. Efter ti forsøg får du:

- **Gennemsnit**: din gennemsnitlige tid.
- **Median**: den midterste værdi, som et enkelt fejltrin flytter mindre end gennemsnittet.
- **Hurtigste**: dit bedste forsøg.
- **Stabilitet**: standardafvigelsen. Jo lavere, jo mere stabilt reagerer du.
- **Tyvstarter**: klik før farveskiftet. Forsøget bliver gentaget.

De sidste ti serier gemmes i browserens lokale lager. Intet bliver sendt videre: ingen sporing, intet eksternt script, ingen konto.

## Kør den

Åbn `index.html` i en hvilken som helst browser. Intet build-trin og ingen afhængigheder.

## Sådan læser du resultatet

De fleste voksne ligger mellem 200 og 300 ms i en enkel visuel test som denne. Skærmen, musen eller touchskærmen og browseren lægger hver et par millisekunder til, så sammenlign dig med dig selv, på den samme enhed. Søvn, træthed, koffein og tidspunktet på dagen påvirker alle resultatet.

Testen måler en simpel reaktionstid. Den er ikke en diagnose og heller ikke en klinisk opmærksomhedstest.

## Sæt testen på dit websted

Du kan gratis vise den fulde reaktionstest fra upchin.app på din egen side. Den findes på 17 sprog: sæt `data-lang` (eller `lang=` i rammens adresse) til `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Med scriptet** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), som tilpasser rammens højde til indholdet:

```html
<div data-upchin-embed="reaction-time-test" data-lang="da">
  <p>Reaktionstest fra <a href="https://upchin.app/da/vaerktoejer/reaktionstest">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Uden script**, hvis dit websted kun accepterer HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=da" title="Reaktionstest" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Reaktionstest fra <a href="https://upchin.app/da/vaerktoejer/reaktionstest">Upchin</a></p>
```

Lad venligst kildeangivelsen under testen blive stående. Scriptet sætter rammen ind ved siden af og fjerner aldrig kildeangivelsen.

## Fuld version

Den fulde [reaktionstest på upchin.app](https://upchin.app/da/vaerktoejer/reaktionstest) findes på 17 sprog. Den gemmer din historik, forklarer hvert tal og lader dig dele et resultat.

Testen er lavet af holdet bag Upchin. Med webstedets egne ord: »Dine apps er designet til at få dig til at scrolle. Upchin er designet til at give dig din tid tilbage.« Appen til iPhone bruger Apples Skærmtid til at hjælpe dig med at [skære ned på din skærmtid](https://upchin.app/da), med friktion på det rigtige tidspunkt i stedet for løftede pegefingre.

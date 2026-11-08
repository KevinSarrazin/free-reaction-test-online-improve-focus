# Gratis reaktionstest online

Andra språk: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Ett gratis reaktionstest som körs i webbläsaren, i en enda HTML-fil.

Testa online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/sv/

Vänta tills fältet byter färg och klicka, tryck på skärmen eller på mellanslag så snabbt du kan. Efter tio försök får du:

- **Genomsnitt**: din medeltid.
- **Median**: mittvärdet, som ett enstaka misstag flyttar mindre än genomsnittet.
- **Snabbast**: ditt bästa försök.
- **Spridning**: standardavvikelsen. Ju lägre, desto jämnare.
- **Tjuvstarter**: klick innan färgen ändras. Försöket görs om.

De tio senaste serierna sparas i webbläsarens lokala lagring. Inget skickas någonstans: ingen spårning, inga externa skript, inget konto.

## Kör testet

Öppna `index.html` i valfri webbläsare. Inget byggsteg och inga beroenden.

## Så tolkar du resultatet

De flesta vuxna hamnar mellan 200 och 300 ms i ett enkelt visuellt test som det här. Skärmen, musen eller pekskärmen och webbläsaren lägger till några millisekunder var, så jämför dig med dig själv, på samma enhet. Sömn, trötthet, koffein och tid på dygnet påverkar alla resultatet.

Testet mäter en enkel reaktionstid. Det är ingen diagnos och inget kliniskt test av uppmärksamheten.

## Bädda in testet på din webbplats

Du kan visa hela reaktionstestet från upchin.app på din egen sida, gratis. Det finns på 17 språk: sätt `data-lang` (eller `lang=` i ramens adress) till `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Med skriptet** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), som anpassar ramens höjd efter innehållet:

```html
<div data-upchin-embed="reaction-time-test" data-lang="sv">
  <p>Reaktionstest från <a href="https://upchin.app/sv/verktyg/reaktionstest">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Utan skript**, om din webbplats bara tillåter HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=sv" title="Reaktionstest" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Reaktionstest från <a href="https://upchin.app/sv/verktyg/reaktionstest">Upchin</a></p>
```

Låt gärna källhänvisningen under testet vara kvar. Skriptet lägger till ramen bredvid den och tar aldrig bort den.

## Fullständig version

Den fullständiga versionen, [reaktionstestet på upchin.app](https://upchin.app/sv/verktyg/reaktionstest), finns på 17 språk. Den sparar din historik, förklarar varje siffra och låter dig dela ett resultat.

Testet är gjort av teamet bakom Upchin. Med webbplatsens egna ord: ”Dina appar är gjorda för att få dig att scrolla. Upchin är gjord för att ge dig tiden tillbaka.” Appen för iPhone bygger på Apples Skärmtid och hjälper dig att [minska din skärmtid](https://upchin.app/sv) – med friktion i rätt ögonblick, utan pekpinnar.

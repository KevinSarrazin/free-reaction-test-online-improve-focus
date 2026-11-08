# Kostenloser Reaktionstest online

Andere Sprachen: [English](README.md) · [Français](README.fr.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Ein kostenloser Reaktionstest, der in deinem Browser läuft, in einer einzigen HTML-Datei.

Online ausprobieren: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/de/

Warte, bis das Feld die Farbe wechselt, dann klicke, tippe oder drücke die Leertaste, so schnell du kannst. Nach zehn Versuchen bekommst du:

- **Mittelwert**: deine durchschnittliche Zeit.
- **Median**: der mittlere Wert, den ein Ausrutscher weniger verschiebt als den Mittelwert.
- **Schnellste Zeit**: dein bester Versuch.
- **Gleichmäßigkeit**: die Standardabweichung. Je niedriger, desto gleichmäßiger.
- **Fehlstarts**: Klicks vor dem Farbwechsel. Der Versuch wird wiederholt.

Die letzten zehn Serien bleiben im lokalen Speicher deines Browsers. Nichts wird irgendwohin gesendet: kein Tracking, kein externes Skript, keine Anmeldung.

## Ausführen

Öffne `index.html` in einem beliebigen Browser. Kein Build-Schritt, keine Abhängigkeiten.

## Das Ergebnis lesen

Die meisten Erwachsenen liegen bei einem einfachen visuellen Test wie diesem zwischen 200 und 300 ms. Bildschirm, Maus oder Touchscreen und Browser kosten jeweils ein paar Millisekunden, vergleiche dich also mit dir selbst, auf demselben Gerät. Schlaf, Müdigkeit, Koffein und Tageszeit verschieben das Ergebnis.

Dieser Test misst eine einfache Reaktionszeit. Er ist keine Diagnose und kein klinischer Aufmerksamkeitstest.

## Binde den Test auf deiner Website ein

Du kannst den vollständigen Reaktionstest von upchin.app kostenlos auf deiner eigenen Seite zeigen. Er ist in 17 Sprachen verfügbar: Setze `data-lang` (oder `lang=` in der Adresse des Frames) auf `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Mit dem Skript** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), das die Höhe des Frames an seinen Inhalt anpasst:

```html
<div data-upchin-embed="reaction-time-test" data-lang="de">
  <p>Reaktionstest von <a href="https://upchin.app/de/tools/reaktionstest">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Ohne Skript**, wenn deine Website nur HTML zulässt:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=de" title="Reaktionstest" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Reaktionstest von <a href="https://upchin.app/de/tools/reaktionstest">Upchin</a></p>
```

Bitte lass die Quellenangabe unter dem Test stehen. Das Skript setzt den Frame daneben und entfernt sie nie.

## Vollständige Version

Der [Reaktionstest auf upchin.app](https://upchin.app/de/tools/reaktionstest) ist in 17 Sprachen verfügbar. Er speichert deinen Verlauf, erklärt jede Zahl und lässt dich ein Ergebnis teilen.

Dieser Test stammt vom Team hinter Upchin. Auf der Website heißt es: „Deine Apps sind dafür gebaut, dass du weiterscrollst. Upchin ist dafür gebaut, dir deine Zeit zurückzugeben.“ Die iPhone-App nutzt Apples Bildschirmzeit, um dir zu helfen, [deine Bildschirmzeit zu reduzieren](https://upchin.app/de) – mit einer Bremse im richtigen Moment statt mit erhobenem Zeigefinger.

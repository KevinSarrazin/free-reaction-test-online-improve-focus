# Darmowy test reakcji online

Inne języki: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Darmowy test czasu reakcji, który działa w przeglądarce, w jednym pliku HTML.

Wypróbuj online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/pl/

Poczekaj, aż pole zmieni kolor, i jak najszybciej kliknij, dotknij ekranu lub naciśnij spację. Po dziesięciu próbach dostajesz:

- **Średnia**: Twój przeciętny czas.
- **Mediana**: wartość środkowa, którą jedna wpadka przesuwa mniej niż średnią.
- **Najszybszy czas**: Twoja najlepsza próba.
- **Regularność**: odchylenie standardowe. Im niższe, tym równiej reagujesz.
- **Falstarty**: kliknięcia przed zmianą koloru. Próba jest powtarzana.

Ostatnie dziesięć serii zostaje w pamięci lokalnej przeglądarki. Nic nie jest nigdzie wysyłane: bez śledzenia, bez zewnętrznych skryptów, bez rejestracji.

## Uruchomienie

Otwórz `index.html` w dowolnej przeglądarce. Bez kompilacji i bez zależności.

## Jak odczytać wynik

Większość dorosłych osiąga od 200 do 300 ms w prostym teście wzrokowym takim jak ten. Ekran, mysz lub ekran dotykowy i przeglądarka dodają po kilka milisekund, więc porównuj własne wyniki, zawsze na tym samym urządzeniu. Sen, zmęczenie, kofeina i pora dnia wpływają na wynik.

Ten test mierzy prosty czas reakcji. To nie jest diagnoza ani kliniczny test uwagi.

## Umieść test na swojej stronie

Pełny test czasu reakcji z upchin.app możesz bezpłatnie pokazać na własnej stronie. Jest dostępny w 17 językach: ustaw `data-lang` (lub `lang=` w adresie ramki) na jeden z kodów: `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Ze skryptem** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), który dopasowuje wysokość ramki do treści:

```html
<div data-upchin-embed="reaction-time-test" data-lang="pl">
  <p>Test reakcji od <a href="https://upchin.app/pl/narzedzia/test-reakcji">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Bez skryptu**, jeśli Twoja strona przyjmuje tylko HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=pl" title="Test reakcji" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Test reakcji od <a href="https://upchin.app/pl/narzedzia/test-reakcji">Upchin</a></p>
```

Zostaw, proszę, informację o źródle pod testem. Skrypt dodaje ramkę obok niej i nigdy jej nie usuwa.

## Pełna wersja

Pełny [test czasu reakcji na upchin.app](https://upchin.app/pl/narzedzia/test-reakcji) jest dostępny w 17 językach. Zapisuje historię, objaśnia każdą liczbę i pozwala udostępnić wynik.

Ten test przygotował zespół Upchin. Jak głosi jego strona: „Aplikacje w telefonie są projektowane tak, by trzymać Cię przy przewijaniu. Upchin powstał, by oddać Ci czas.” Aplikacja na iPhone’a korzysta z funkcji Czas przed ekranem od Apple, by pomóc Ci [ograniczyć czas przed ekranem](https://upchin.app/pl) – z hamulcem we właściwej chwili zamiast moralizowania.

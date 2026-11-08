# Test de reacción gratis en línea

Otros idiomas: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Un test de tiempo de reacción gratis que funciona en tu navegador, en un solo archivo HTML.

Pruébalo en línea: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/es-MX/

Espera a que el panel cambie de color y luego haz clic, toca la pantalla o presiona Espacio lo más rápido que puedas. Después de diez intentos obtienes:

- **Promedio**: tu tiempo promedio.
- **Mediana**: el valor del medio, al que un error mueve menos que al promedio.
- **Más rápido**: tu mejor intento.
- **Regularidad**: la desviación estándar. Mientras más baja, más constantes son tus tiempos.
- **Salidas en falso**: clics antes del cambio de color. El intento se repite.

Las últimas diez series se guardan en el almacenamiento local de tu navegador. No se envía nada a ningún lado: sin rastreo, sin scripts externos, sin registro.

## Cómo usarlo

Abre `index.html` en cualquier navegador. Sin compilación y sin dependencias.

## Cómo leer el resultado

La mayoría de los adultos obtiene entre 200 y 300 ms en una prueba visual simple como esta. La pantalla, el mouse o la pantalla táctil y el navegador agregan unos milisegundos cada uno, así que compárate solo con tus propios resultados, en el mismo dispositivo. El sueño, el cansancio, la cafeína y la hora del día cambian el resultado.

Este test mide un tiempo de reacción simple. No es un diagnóstico ni una prueba clínica de atención.

## Agrega el test a tu sitio web

Puedes mostrar gratis el test de reacción completo de upchin.app en tu propia página. Está disponible en 17 idiomas: define `data-lang` (o `lang=` en la dirección del marco) como `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Con el script** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), que ajusta la altura del marco a su contenido:

```html
<div data-upchin-embed="reaction-time-test" data-lang="es-MX">
  <p>Test de reacción por <a href="https://upchin.app/es-MX/herramientas/test-de-reaccion">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Sin script**, si tu sitio solo acepta HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=es-MX" title="Test de reacción" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Test de reacción por <a href="https://upchin.app/es-MX/herramientas/test-de-reaccion">Upchin</a></p>
```

Por favor, conserva la línea de crédito debajo del test. El script agrega el marco junto a ella y nunca la quita.

## Versión completa

El [test de reacción en upchin.app](https://upchin.app/es-MX/herramientas/test-de-reaccion) está disponible en 17 idiomas. Guarda tu historial, explica cada número y te permite compartir un resultado.

Este test lo hace el equipo detrás de Upchin. En palabras de su sitio web: “Tus apps están diseñadas para que sigas haciendo scroll. Upchin está diseñada para devolverte tu tiempo.” La app para iPhone usa Tiempo en pantalla de Apple para ayudarte a [reducir tu tiempo en pantalla](https://upchin.app/es-MX), con fricción en el momento justo en lugar de sermones.

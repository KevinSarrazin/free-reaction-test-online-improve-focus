# Test di reazione gratuito online

Altre lingue: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Un test del tempo di reazione gratuito che funziona nel browser, in un solo file HTML.

Provalo online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/it/

Aspetta che il riquadro cambi colore, poi fai clic, tocca lo schermo o premi Spazio il più velocemente possibile. Dopo dieci tentativi ottieni:

- **Media**: il tuo tempo medio.
- **Mediana**: il valore centrale, che un passo falso sposta meno della media.
- **Tempo migliore**: il tuo tentativo più rapido.
- **Regolarità**: la deviazione standard. Più è bassa, più sei regolare.
- **False partenze**: clic prima del cambio di colore. Il tentativo viene ripetuto.

Le ultime dieci serie restano nell’archiviazione locale del browser. Nessun dato viene inviato: niente tracciamento, nessuno script esterno, nessun account.

## Come avviarlo

Apri `index.html` in qualsiasi browser. Nessuna compilazione, nessuna dipendenza.

## Leggere il risultato

La maggior parte degli adulti si colloca tra 200 e 300 ms in un semplice test visivo come questo. Lo schermo, il mouse o il touch screen e il browser aggiungono ciascuno qualche millisecondo, quindi confrontati con te stesso, sullo stesso dispositivo. Sonno, stanchezza, caffeina e ora del giorno influenzano il risultato.

Questo test misura un tempo di reazione semplice. Non è una diagnosi e non è un test clinico dell’attenzione.

## Inserisci il test sul tuo sito

Puoi mostrare gratis il test di reazione completo di upchin.app sulla tua pagina. È disponibile in 17 lingue: imposta `data-lang` (o `lang=` nell’indirizzo del frame) su `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Con lo script** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), che adatta l’altezza del frame al contenuto:

```html
<div data-upchin-embed="reaction-time-test" data-lang="it">
  <p>Test di reazione di <a href="https://upchin.app/it/strumenti/test-di-reazione">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Senza script**, se il tuo sito accetta solo HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=it" title="Test di reazione" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Test di reazione di <a href="https://upchin.app/it/strumenti/test-di-reazione">Upchin</a></p>
```

Per favore, lascia la riga di credito sotto il test. Lo script aggiunge il frame accanto e non la rimuove mai.

## Versione completa

Il [test di reazione su upchin.app](https://upchin.app/it/strumenti/test-di-reazione) è disponibile in 17 lingue. Conserva la cronologia, spiega ogni valore e ti permette di condividere un risultato.

Questo test è realizzato dal team di Upchin. Come si legge sul suo sito: «Le tue app sono progettate per farti scrollare. Upchin nasce per restituirti il tuo tempo.» L’app per iPhone usa Tempo di utilizzo di Apple per aiutarti a [ridurre il tempo sullo schermo](https://upchin.app/it), con un po’ di attrito al momento giusto, senza farti la morale.

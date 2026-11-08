# Test de réaction gratuit en ligne

Autres langues : [English](README.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Un test de temps de réaction gratuit qui tourne dans ton navigateur, en un seul fichier HTML.

Essaie-le en ligne : https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/fr/

Attends que le panneau change de couleur, puis clique, touche l’écran ou appuie sur Espace le plus vite possible. Après dix essais, tu obtiens :

- **Moyenne** : ton temps moyen.
- **Médiane** : la valeur du milieu, qu’un essai raté fait moins bouger que la moyenne.
- **Le plus rapide** : ton meilleur essai.
- **Régularité** : l’écart-type. Plus il est bas, plus tes temps sont réguliers.
- **Faux départs** : les clics avant le changement de couleur. L’essai est refait.

Les dix dernières séries sont conservées dans le stockage local de ton navigateur. Rien n’est envoyé nulle part : aucun pistage, aucun script externe, aucune inscription.

## Lancer en local

Ouvre `index.html` dans n’importe quel navigateur. Aucune compilation, aucune dépendance.

## Lire le résultat

La plupart des adultes se situent entre 200 et 300 ms sur un test visuel simple comme celui-ci. L’écran, la souris ou l’écran tactile et le navigateur ajoutent chacun quelques millisecondes : compare-toi donc à toi-même, sur le même appareil. Le sommeil, la fatigue, la caféine et l’heure de la journée font varier le résultat.

Ce test mesure un temps de réaction simple. Ce n’est pas un diagnostic, ni un test clinique de l’attention.

## Intègre le test sur ton site

Tu peux afficher gratuitement le test de réaction complet d’upchin.app sur ta propre page. Il existe en 17 langues : règle `data-lang` (ou `lang=` dans l’adresse du cadre) sur `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Avec le script** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), qui ajuste la hauteur du cadre à son contenu :

```html
<div data-upchin-embed="reaction-time-test" data-lang="fr">
  <p>Test de réaction par <a href="https://upchin.app/fr/outils/test-de-reaction">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Sans script**, si ton site n’accepte que du HTML :

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=fr" title="Test de réaction" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Test de réaction par <a href="https://upchin.app/fr/outils/test-de-reaction">Upchin</a></p>
```

Garde la ligne de crédit sous le test, s’il te plaît. Le script ajoute le cadre à côté d’elle et ne la retire jamais.

## Version complète

Le [test de réaction sur upchin.app](https://upchin.app/fr/outils/test-de-reaction) existe en 17 langues. Il garde ton historique, explique chaque chiffre et te permet de partager un résultat.

Ce test est réalisé par l’équipe d’Upchin. Comme le dit son site : « Tes apps sont conçues pour te faire scroller. Upchin est conçue pour te rendre ton temps. » L’app iPhone s’appuie sur le Temps d’écran d’Apple pour t’aider à [réduire ton temps d’écran](https://upchin.app/fr), avec de la friction au bon moment plutôt qu’une leçon de morale.

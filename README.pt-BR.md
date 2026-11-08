# Teste de reação grátis online

Outros idiomas: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

Um teste de tempo de reação grátis que roda no seu navegador, em um único arquivo HTML.

Experimente online: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/pt-BR/

Espere o painel mudar de cor e clique, toque ou pressione Espaço o mais rápido que puder. Depois de dez tentativas, você recebe:

- **Média**: seu tempo médio.
- **Mediana**: o valor do meio, em que um deslize mexe menos do que na média.
- **Mais rápido**: sua melhor tentativa.
- **Regularidade**: o desvio-padrão. Quanto mais baixo, mais regulares são seus tempos.
- **Largadas falsas**: cliques antes da mudança de cor. A tentativa é repetida.

As últimas dez séries ficam salvas no armazenamento local do seu navegador. Nada é enviado para lugar nenhum: sem rastreamento, sem script externo, sem cadastro.

## Como rodar

Abra o `index.html` em qualquer navegador. Sem etapa de build e sem dependências.

## Como interpretar o resultado

A maioria dos adultos fica entre 200 e 300 ms em um teste visual simples como este. A tela, o mouse ou a tela sensível ao toque e o navegador acrescentam alguns milissegundos cada um, por isso compare só os seus próprios resultados, no mesmo aparelho. Sono, cansaço, cafeína e a hora do dia mudam o resultado.

Este teste mede um tempo de reação simples. Não é um diagnóstico nem um teste clínico de atenção.

## Adicione o teste ao seu site

Você pode exibir de graça o teste de reação completo do upchin.app na sua própria página. Ele está disponível em 17 idiomas: defina `data-lang` (ou `lang=` no endereço do frame) como `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK`.

**Com o script** ([`reaction-time-test-embed.js`](reaction-time-test-embed.js)), que ajusta a altura do frame ao conteúdo:

```html
<div data-upchin-embed="reaction-time-test" data-lang="pt-BR">
  <p>Teste de reação por <a href="https://upchin.app/pt-BR/ferramentas/teste-de-reacao">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**Sem script**, se o seu site só aceita HTML:

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=pt-BR" title="Teste de reação" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>Teste de reação por <a href="https://upchin.app/pt-BR/ferramentas/teste-de-reacao">Upchin</a></p>
```

Por favor, mantenha a linha de crédito abaixo do teste. O script adiciona o frame ao lado dela e nunca a remove.

## Versão completa

O [teste de reação no upchin.app](https://upchin.app/pt-BR/ferramentas/teste-de-reacao) está disponível em 17 idiomas. Ele guarda seu histórico, explica cada número e permite compartilhar um resultado.

Este teste é feito pela equipe por trás do Upchin. Nas palavras do site: “Seus apps são feitos para você continuar rolando a tela. O Upchin é feito para devolver seu tempo a você.” O app para iPhone usa o Tempo de Uso da Apple para ajudar você a [reduzir seu tempo de tela](https://upchin.app/pt-BR), com atrito na hora certa em vez de sermão.

# 無料オンライン反応テスト

ほかの言語： [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

ブラウザで動く無料の反応時間テストです。HTMLファイル1つでできています。

オンラインで試す：https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/ja/

パネルの色が変わるのを待って、できるだけ速くクリックかタップをするか、スペースキーを押してください。10回終わると、次の値がわかります：

- **平均**：タイムの平均値です。
- **中央値**：真ん中の値です。1回ミスをしても、平均ほどは動きません。
- **最速**：いちばん速かった回のタイムです。
- **ばらつき**：標準偏差です。小さいほど反応が安定しています。
- **フライング**：色が変わる前にクリックした回数です。その回はやり直しになります。

直近10回分のテスト結果は、ブラウザのローカルストレージに保存されます。データはどこにも送信されません。トラッキングも、外部スクリプトも、登録もありません。

## 実行する

`index.html` をお好きなブラウザで開くだけです。ビルドも依存関係も必要ありません。

## 結果の見方

このようなシンプルな視覚テストでは、大人の多くが200〜300 msに収まります。画面、マウスやタッチスクリーン、ブラウザがそれぞれ数ミリ秒ずつ上乗せするので、比べるなら同じ端末で、自分自身の記録と比べましょう。睡眠、疲れ、カフェイン、時間帯によっても結果は変わります。

このテストが測るのは、単純な反応時間です。診断ではなく、臨床的な注意力の検査でもありません。

## このテストを自分のサイトに埋め込む

upchin.appの反応時間テスト（完全版）を、自分のページに無料で表示できます。17言語に対応しています。`data-lang`（またはフレームのアドレスの `lang=`）に、`en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK` のいずれかを指定してください。

**スクリプトを使う場合**（[`reaction-time-test-embed.js`](reaction-time-test-embed.js)）。フレームの高さを内容に合わせて調整します：

```html
<div data-upchin-embed="reaction-time-test" data-lang="ja">
  <p>反応時間テスト（提供：<a href="https://upchin.app/ja/tools/reaction-time-test">Upchin</a>）</p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**スクリプトを使わない場合**（HTMLしか使えないサイト向け）：

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=ja" title="反応時間テスト" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>反応時間テスト（提供：<a href="https://upchin.app/ja/tools/reaction-time-test">Upchin</a>）</p>
```

テストの下のクレジット表記は残してください。スクリプトはその横にフレームを追加するだけで、クレジットを消すことはありません。

## 完全版

[upchin.appの反応時間テスト](https://upchin.app/ja/tools/reaction-time-test)は17言語に対応しています。履歴が残り、それぞれの数値の解説があり、結果を共有することもできます。

このテストは、Upchinのチームが作りました。公式サイトにはこうあります。「スマホのアプリは、スクロールがやめられないように作られています。Upchinは逆に、その時間をあなたに返すためのアプリです。」このiPhoneアプリは、Appleのスクリーンタイム機能を使って[スクリーンタイムを減らす](https://upchin.app/ja)お手伝いをします。説教をするのではなく、ここぞというときに小さなブレーキをかける。それがUpchinのやり方です。

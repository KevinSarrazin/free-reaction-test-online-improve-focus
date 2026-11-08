# 免費網上反應測試

其他語言： [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md)

一個在瀏覽器裡運行的免費反應時間測試，只有一個 HTML 檔案。

網上試用：https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/zh-HK/

等面板變色，然後盡快點擊、輕觸螢幕或按空白鍵。測完 10 次後，你會得到：

- **平均值**：你的平均時間。
- **中位數**：居中的那個值，一次失誤對它的影響比對平均值小。
- **最快**：你最快的一次。
- **波動**：標準差。數值越小，反應越穩定。
- **搶跑**：顏色變化前就點擊。這一次會重做。

最近 10 輪的結果儲存在瀏覽器的本機儲存空間。任何資料都不會傳送出去：沒有追蹤，沒有外部腳本，也無需註冊。

## 運行

用任何瀏覽器開啟 `index.html` 即可。不用經過建構步驟，也沒有任何依賴項。

## 如何解讀結果

在這類簡單的視覺測試中，大多數成年人的反應時間在 200 至 300 ms 之間。螢幕、滑鼠或觸控式螢幕、瀏覽器都會各自增加幾毫秒，所以請在同一部裝置上，和自己比較。睡眠、疲勞、咖啡因和一天中的時段都會影響結果。

這個測試測的是簡單反應時間。它不是診斷，也不是臨床注意力測試。

## 把這個測試嵌入你的網站

你可以免費把 upchin.app 上完整的反應時間測試放到自己的網頁上。它支援 17 種語言：把 `data-lang`（或框架網址中的 `lang=`）設為 `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK` 其中之一即可。

**使用腳本**（[`reaction-time-test-embed.js`](reaction-time-test-embed.js)），它會根據內容自動調整框架高度：

```html
<div data-upchin-embed="reaction-time-test" data-lang="zh-HK">
  <p>反應時間測試，由 <a href="https://upchin.app/zh-HK/tools/reaction-time-test">Upchin</a> 提供</p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**不用腳本**，適合只接受 HTML 的網站：

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=zh-HK" title="反應時間測試" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>反應時間測試，由 <a href="https://upchin.app/zh-HK/tools/reaction-time-test">Upchin</a> 提供</p>
```

請保留測試下方的來源連結。腳本只會在它旁邊加入框架，絕不會把它移除。

## 完整版

[upchin.app 上的反應時間測試](https://upchin.app/zh-HK/tools/reaction-time-test)支援 17 種語言，會保留你的歷史記錄，解釋每個數值，還能分享結果。

這個測試由 Upchin 團隊打造。用其官網的話說：「手機裡的 App，生來就是為了讓你玩個不停；Upchin 反其道而行，把時間還給你。」這款 iPhone App 借助 Apple 的螢幕使用時間功能，幫你[減少螢幕時間](https://upchin.app/zh-HK)——不靠說教，而是在關鍵時刻踩一下剎車。

# 免费在线反应测试

其他语言： [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [繁體中文（香港）](README.zh-HK.md)

一个在浏览器里运行的免费反应时间测试，只有一个 HTML 文件。

在线试用：https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/zh-Hans/

等面板变色，然后尽快点击、轻点屏幕或按空格键。测完 10 次后，你会得到：

- **平均值**：你的平均时间。
- **中位数**：居中的那个值，一次失误对它的影响比对平均值小。
- **最快**：你最快的一次。
- **波动**：标准差。数值越小，反应越稳定。
- **抢跑**：颜色变化前就点击。这一次会重做。

最近 10 轮的结果保存在浏览器的本地存储里。任何数据都不会发送出去：没有追踪，没有外部脚本，也无需注册。

## 运行

用任意浏览器打开 `index.html` 即可。无需构建，也没有任何依赖。

## 如何解读结果

在这类简单的视觉测试中，大多数成年人的反应时间在 200 到 300 ms 之间。屏幕、鼠标或触摸屏、浏览器都会各自增加几毫秒，所以请在同一台设备上，和自己比较。睡眠、疲劳、咖啡因和一天中的时段都会影响结果。

这个测试测的是简单反应时间。它不是诊断，也不是临床注意力测试。

## 把这个测试嵌入你的网站

你可以免费把 upchin.app 上完整的反应时间测试放到自己的网页上。它支持 17 种语言：把 `data-lang`（或框架地址中的 `lang=`）设为 `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK` 之一即可。

**使用脚本**（[`reaction-time-test-embed.js`](reaction-time-test-embed.js)），它会根据内容自动调整框架高度：

```html
<div data-upchin-embed="reaction-time-test" data-lang="zh-Hans">
  <p>反应时间测试，由 <a href="https://upchin.app/zh-Hans/tools/reaction-time-test">Upchin</a> 提供</p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**不用脚本**，适合只接受 HTML 的网站：

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=zh-Hans" title="反应时间测试" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>反应时间测试，由 <a href="https://upchin.app/zh-Hans/tools/reaction-time-test">Upchin</a> 提供</p>
```

请保留测试下方的来源链接。脚本只会在它旁边加入框架，绝不会把它移除。

## 完整版

[upchin.app 上的反应时间测试](https://upchin.app/zh-Hans/tools/reaction-time-test)支持 17 种语言，会保存你的历史记录，解释每个数值，还能分享结果。

这个测试由 Upchin 团队打造。用其官网的话说：“手机里的应用，生来就是为了让你刷个不停；Upchin 反其道而行，把时间还给你。”这款 iPhone 应用借助 Apple 的屏幕使用时间功能，帮你[减少屏幕时间](https://upchin.app/zh-Hans)——不靠说教，而是在关键时刻踩一下刹车。

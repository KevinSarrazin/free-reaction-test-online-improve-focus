# 무료 온라인 반응 테스트

다른 언어: [English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español (México)](README.es-MX.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Polski](README.pl.md) · [Dansk](README.da.md) · [Svenska](README.sv.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [简体中文](README.zh-Hans.md) · [繁體中文（香港）](README.zh-HK.md)

브라우저에서 돌아가는 무료 반응 속도 테스트예요. HTML 파일 하나로 되어 있어요.

온라인에서 해 보기: https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/ko/

패널 색이 바뀔 때까지 기다렸다가 최대한 빨리 클릭하거나, 탭하거나, 스페이스 바를 누르세요. 10회를 마치면 다음 결과를 볼 수 있어요.

- **평균**: 평균 시간이에요.
- **중앙값**: 가운데 값이에요. 한 번 실수해도 평균보다 덜 흔들려요.
- **최고 기록**: 가장 빨랐던 회차의 시간이에요.
- **편차**: 표준편차예요. 낮을수록 반응이 고르다는 뜻이에요.
- **부정 출발**: 색이 바뀌기 전에 클릭한 횟수예요. 그 회차는 다시 해요.

최근 10번의 측정 결과는 브라우저의 로컬 저장소에 남아요. 어디로도 전송되지 않아요. 추적도, 외부 스크립트도, 가입도 없어요.

## 실행하기

`index.html` 파일을 아무 브라우저에서나 열면 돼요. 빌드 과정도, 의존성도 없어요.

## 결과 읽는 법

이런 단순한 시각 테스트에서 성인은 대부분 200~300 ms 사이에 들어와요. 화면, 마우스나 터치스크린, 브라우저가 각각 몇 밀리초씩 더하니까, 같은 기기에서 나 자신과 비교해 보세요. 수면, 피로, 카페인, 시간대에 따라서도 결과가 달라져요.

이 테스트는 단순 반응 시간을 재요. 진단이 아니고, 임상 주의력 검사도 아니에요.

## 이 테스트를 내 웹사이트에 넣기

upchin.app의 반응 속도 테스트 전체 버전을 내 페이지에 무료로 넣을 수 있어요. 17개 언어를 지원해요. `data-lang`(또는 프레임 주소의 `lang=`) 값을 `en`, `fr`, `de`, `es-MX`, `pt-BR`, `it`, `nl`, `pl`, `da`, `sv`, `ru`, `id`, `hi`, `ja`, `ko`, `zh-Hans`, `zh-HK` 중 하나로 정해 주세요.

**스크립트를 쓰는 방법**([`reaction-time-test-embed.js`](reaction-time-test-embed.js)). 프레임 높이를 내용에 맞게 조절해 줘요.

```html
<div data-upchin-embed="reaction-time-test" data-lang="ko">
  <p>반응 속도 테스트 · 제공: <a href="https://upchin.app/ko/tools/reaction-time-test">Upchin</a></p>
</div>
<script src="https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/reaction-time-test-embed.js" async></script>
```

**스크립트 없이 넣는 방법**. 사이트에 HTML만 넣을 수 있을 때 써요.

```html
<iframe src="https://upchin.app/embed/reaction-time-test?lang=ko" title="반응 속도 테스트" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>
<p>반응 속도 테스트 · 제공: <a href="https://upchin.app/ko/tools/reaction-time-test">Upchin</a></p>
```

테스트 아래의 출처 표시는 남겨 주세요. 스크립트는 그 옆에 프레임을 추가할 뿐, 출처 표시를 지우지 않아요.

## 전체 버전

17개 언어로 쓸 수 있는 [upchin.app의 반응 속도 테스트](https://upchin.app/ko/tools/reaction-time-test)에서는 기록이 남고, 각 수치를 설명해 주며, 결과를 공유할 수도 있어요.

이 테스트는 Upchin 팀이 만들었어요. 웹사이트에는 이렇게 쓰여 있어요. “휴대폰 속 앱은 계속 스크롤하도록 설계돼 있어요. Upchin은 반대로, 그 시간을 돌려주는 앱이에요.” 이 iPhone 앱은 Apple의 스크린 타임 기능을 활용해 [스크린 타임을 줄이도록](https://upchin.app/ko) 도와줘요. 잔소리하는 대신, 꼭 필요한 순간에 브레이크를 걸어 줘요.

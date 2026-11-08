"""Builds the page and the README of every language from i18n/strings/<lang>.json.

    python3 i18n/build.py        (run from the repository root)

English is served at the root (index.html, README.md); every other language in its
own folder (fr/index.html) with README.<lang>.md. Edit the strings or the template,
never the generated files.
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
I18N = ROOT / 'i18n'
BASE = 'https://kevinsarrazin.github.io/free-reaction-test-online-improve-focus/'
REPO = 'https://github.com/KevinSarrazin/free-reaction-test-online-improve-focus'
SCRIPT = BASE + 'reaction-time-test-embed.js'
ORDER = ['en', 'fr', 'de', 'es-MX', 'pt-BR', 'it', 'nl', 'pl', 'da', 'sv', 'ru', 'id', 'hi', 'ja', 'ko', 'zh-Hans', 'zh-HK']

# Strings the page script reads at run time (the rest is rendered in the HTML).
SCRIPT_KEYS = ['unit', 'stage_start', 'stage_start_hint', 'progress', 'history_empty', 'history_line', 'history_false',
               'waiting', 'now', 'spoken_wait', 'spoken_now', 'too_soon', 'too_soon_hint', 'spoken_too_soon',
               'next_hint', 'spoken_ms', 'finished_hint', 'spoken_finished']


def load():
    data = {}
    for code in ORDER:
        path = I18N / 'strings' / f'{code}.json'
        if path.exists():
            data[code] = json.loads(path.read_text(encoding='utf-8'))
    ref = data['en']
    for code, d in data.items():
        for part in ('_meta', 'page', 'readme'):
            missing = set(ref[part]) - set(d.get(part, {}))
            extra = set(d.get(part, {})) - set(ref[part])
            if missing or extra:
                sys.exit(f'{code}.{part}: missing {sorted(missing)} extra {sorted(extra)}')
            for key, value in d[part].items():
                for token in ('{n}', '{total}', '{mean}', '{median}', '{ms}', '{link}', '{upchin}', '{url}',
                              '{codes}', '{file}', '{quote}', '{anchor}'):
                    if (token in ref[part][key]) != (token in value):
                        sys.exit(f'{code}.{part}.{key}: placeholder {token} differs from English')
    return data


def folder(code):
    return '' if code == 'en' else code + '/'


def page(code, data):
    s = data[code]['page']
    meta = data[code]['_meta']
    esc = lambda v: html.escape(v, quote=True)
    out = (I18N / 'page.template.html').read_text(encoding='utf-8')

    alternates = '\n'.join(
        f'<link rel="alternate" hreflang="{c}" href="{BASE}{folder(c)}">' for c in data
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}">'
    up = '' if code == 'en' else '../'
    links = ''.join(
        f'<li><a href="{up}{folder(c) or "./"}" hreflang="{c}" lang="{c}"'
        + (' aria-current="page"' if c == code else '')
        + f'>{esc(data[c]["_meta"]["language_name"])}</a></li>'
        for c in data
    )
    cta_p1 = esc(s['cta_p1']).replace('{link}', f'<a href="{esc(meta["tool_url"])}">{esc(s["cta_link"])}</a>')
    cta_p2 = esc(s['cta_p2']).replace('{upchin}', f'<a href="{esc(meta["home_url"])}">Upchin</a>')
    strings = {k: s[k] for k in SCRIPT_KEYS}

    out = out.replace('{{lang}}', code)
    out = out.replace('{{alternates}}', alternates)
    out = out.replace('{{language_links}}', links)
    out = out.replace('{{cta_p1_html}}', cta_p1)
    out = out.replace('{{cta_p2_html}}', cta_p2)
    out = out.replace('{{strings_json}}', json.dumps(strings, ensure_ascii=False).replace('</', '<\\/'))
    for key, value in s.items():
        out = out.replace('{{page.' + key + '}}', esc(value))
    if '{{' in out:
        sys.exit(f'{code}: unreplaced placeholder near {out[out.index("{{"):out.index("{{") + 40]}')
    target = ROOT / folder(code) / 'index.html'
    target.parent.mkdir(exist_ok=True)
    target.write_text(out, encoding='utf-8')


def readme(code, data):
    r = data[code]['readme']
    meta = data[code]['_meta']
    name = 'README.md' if code == 'en' else f'README.{code}.md'
    others = ' · '.join(
        f'[{data[c]["_meta"]["language_name"]}]({"README.md" if c == "en" else f"README.{c}.md"})'
        for c in data if c != code
    )
    credit = r['embed_credit'].replace('{upchin}', f'<a href="{meta["tool_url"]}">Upchin</a>')
    codes = ', '.join(f'`{c}`' for c in ORDER)
    lines = [
        f'# {r["title"]}',
        '',
        f'{r["languages"]} {others}',
        '',
        r['intro'],
        '',
        r['try_online'].replace('{url}', BASE + folder(code)),
        '',
        r['how'],
        '',
        f'- {r["def_mean"]}',
        f'- {r["def_median"]}',
        f'- {r["def_fastest"]}',
        f'- {r["def_spread"]}',
        f'- {r["def_false"]}',
        '',
        r['storage'],
        '',
        f'## {r["run_title"]}',
        '',
        r['run'],
        '',
        f'## {r["reading_title"]}',
        '',
        r['reading_p1'],
        '',
        r['reading_p2'],
        '',
        f'## {r["embed_title"]}',
        '',
        r['embed_intro'].replace('{codes}', codes),
        '',
        r['embed_script'].replace('{file}', '[`reaction-time-test-embed.js`](reaction-time-test-embed.js)'),
        '',
        '```html',
        f'<div data-upchin-embed="reaction-time-test" data-lang="{code}">',
        f'  <p>{credit}</p>',
        '</div>',
        f'<script src="{SCRIPT}" async></script>',
        '```',
        '',
        r['embed_html'],
        '',
        '```html',
        f'<iframe src="https://upchin.app/embed/reaction-time-test?lang={code}" title="{html.escape(r["embed_frame_title"])}" width="100%" height="1450" style="border:0;max-width:100%" loading="lazy" allow="clipboard-write"></iframe>',
        f'<p>{credit}</p>',
        '```',
        '',
        r['embed_keep'],
        '',
        f'## {r["full_title"]}',
        '',
        r['full_p1'].replace('{link}', f'[{r["full_link"]}]({meta["tool_url"]})'),
        '',
        r['full_p2'].replace('{quote}', r['quote']).replace('{anchor}', f'[{r["anchor"]}]({meta["home_url"]})'),
        '',
    ]
    (ROOT / name).write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    data = load()
    for code in data:
        page(code, data)
        readme(code, data)
    print('built:', ', '.join(data))

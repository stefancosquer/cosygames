#!/usr/bin/env python3
"""Validate the generated site's translations and local links without dependencies."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'build/site'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.lang = None
        self.h1 = 0
        self.scripts = 0
        self.alternates = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'h1':
            self.h1 += 1
        if tag == 'script':
            self.scripts += 1
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'Duplicate HTML id'
            self.ids.add(attrs['id'])
        for attr in ('href', 'src'):
            if attr in attrs:
                self.links.append(attrs[attr])
        if tag == 'link' and attrs.get('rel') == 'alternate':
            self.alternates[attrs['hreflang']] = attrs['href']


def check():
    content = json.loads((ROOT/'_data/content.json').read_text())
    assert set(content) == {'en','fr','es'}
    for lang, text in content.items():
        assert text.keys() == content['en'].keys(), f'Missing translations: {lang}'
        assert len(text['games']) == 8
        assert len(text['features']) == 3
        assert len(text['privacy_sections']) == 9
    information = json.loads((ROOT/'_data/information.json').read_text())
    assert set(information) == set(content)
    for lang, kinds in information.items():
        assert set(kinds) == {'legal', 'support'}
        for kind, values in kinds.items():
            assert values.keys() == information['en'][kind].keys()
            assert [s['id'] for s in values['sections']] == [s['id'] for s in information['en'][kind]['sections']]
    pages = {}
    for path in OUTPUT.rglob('*.html'):
        page = Page()
        page.feed(path.read_text())
        assert page.lang in content and page.h1 == 1, path
        assert page.scripts == 0, path
        assert set(page.alternates) == {'en','fr','es','x-default'}, path
        pages[path.resolve()] = page
    assert len(pages) == 13, 'Twelve translated pages and one 404 required'
    for source, page in pages.items():
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (OUTPUT / unquote(parsed.path).lstrip('/') if parsed.path.startswith('/') else source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            assert target.is_relative_to(OUTPUT.resolve()), f'Escaped public folder: {link}'
            if target.is_dir():
                target /= 'index.html'
            assert target.exists(), f'Broken link: {source}: {link}'
            if parsed.fragment:
                assert parsed.fragment in pages[target].ids, f'Broken anchor: {link}'
    urls = ET.parse(OUTPUT/'sitemap.xml').findall('{*}url/{*}loc')
    assert len(urls) == 12
    for url in urls:
        assert (OUTPUT / urlsplit(url.text).path.lstrip('/') / 'index.html').exists()
    assert (OUTPUT/'CNAME').read_text().strip() == 'cosygames.app'
    print(f'OK: {len(pages)} HTML pages, FR/EN/ES, local links, anchors, sitemap and domain.')


if __name__ == '__main__':
    check()

"""Audit published links, metadata, and seller entries without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://lephron.github.io'
REQUIRED = {'index.html', 'privacy.html', 'support.html', 'delete-account.html', '404.html'}

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.h1_count = 0
        self.english = False
        self.viewport = False
        self.description = False
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.h1_count += tag == 'h1'
        self.english |= tag == 'html' and attrs.get('lang') == 'en'
        self.viewport |= tag == 'meta' and attrs.get('name') == 'viewport'
        self.description |= tag == 'meta' and attrs.get('name') == 'description' and bool(attrs.get('content'))
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'img' and 'alt' not in attrs:
            raise ValueError('Image is missing alt text')

def check():
    pages, errors = {}, []
    for name in sorted(REQUIRED):
        parser = Page()
        file = ROOT / name
        if not file.is_file():
            errors.append(f'Missing {name}')
            continue
        parser.feed(file.read_text())
        pages[name] = parser
        if parser.h1_count != 1 or not parser.english or not parser.viewport or not parser.description:
            errors.append(f'{name}: missing document metadata or a single heading')
        expected = BASE + ('/' if name == 'index.html' else '/' + name)
        if name != '404.html' and parser.canonical != expected:
            errors.append(f'{name}: canonical URL mismatch')
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme in ('https', 'http', 'mailto') or url.netloc:
                continue
            path = unquote(url.path).lstrip('/') or name
            if url.path == '/':
                path = 'index.html'
            if not (ROOT / path).is_file():
                errors.append(f'{name}: broken link {link}')
    for name, parser in pages.items():
        for link in parser.links:
            url = urlsplit(link)
            if not url.scheme and not url.netloc and url.fragment:
                target = 'index.html' if url.path == '/' else (unquote(url.path).lstrip('/') or name)
                if target in pages and unquote(url.fragment) not in pages[target].ids:
                    errors.append(f'{name}: missing fragment {link}')
    entries = [line.strip() for line in (ROOT / 'app-ads.txt').read_text().splitlines()
               if line.strip() and not line.lstrip().startswith('#')]
    for entry in entries:
        if not re.fullmatch(r'google\.com,\s*pub-\d{16},\s*DIRECT,\s*f08c47fec0942fa0', entry):
            errors.append('Unexpected seller entry: verify against the owner\'s AdMob snippet')
        if 'pub-0000000000000000' in entry or 'pub-3940256099942544' in entry:
            errors.append('Sample publisher ID cannot authorize live ads')
    if '--require-ads' in sys.argv and not entries:
        errors.append('AdMob activation blocked: no owner-supplied authorized seller entry')
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for node in ET.parse(ROOT / 'sitemap.xml').findall('s:url/s:loc', ns):
        if not node.text.startswith(BASE + '/'):
            errors.append('Sitemap contains an unexpected domain')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} HTML pages, local links/fragments, metadata, and sitemap')
    print('AdMob sellers: configured' if entries else 'AdMob sellers: pending (live ad verification incomplete)')

if __name__ == '__main__':
    check()

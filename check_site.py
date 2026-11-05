"""Check the generated book's links and controls without third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / 'dist'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.assets, self.controls = path, [], [], [], []
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('img', 'script') and 'src' in attrs:
            self.assets.append(attrs['src'])
        if tag == 'link' and 'href' in attrs:
            self.assets.append(attrs['href'])
        self.controls.extend(attrs.get('aria-controls', '').split())

def check():
    pages = {p.resolve(): Page(p) for p in ROOT.glob('*.html')}
    errors = []
    expected = ['index.html', 'about.html'] + [f'unit-{n}.html' for n in range(2, 16)]
    for name in expected:
        if not (ROOT / name).is_file():
            errors.append(f'Missing page: {name}')
    for path, page in pages.items():
        if len(page.ids) != len(set(page.ids)):
            errors.append(f'{path.name}: duplicate IDs')
        for control in page.controls:
            if control not in page.ids:
                errors.append(f'{path.name}: missing control target {control}')
        for reference in page.links + page.assets:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith('/'):
                errors.append(f'{path.name}: root-relative URL breaks project hosting: {reference}')
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT.resolve()):
                errors.append(f'{path.name}: path outside dist: {reference}')
            elif not target.is_file():
                errors.append(f'{path.name}: missing file {reference}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.name}: missing anchor {reference}')
        text = path.read_text(encoding='utf-8')
        if re.search(r'(?:/workspace/|terminal\.local|\.chatgpt\.site)', text):
            errors.append(f'{path.name}: previous hosting dependency')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'OK: {len(pages)} pages; local links, images, scripts and help controls checked.')
    print('External CDN availability and mathematical correctness of all content are not covered.')
    return 0

if __name__ == '__main__':
    raise SystemExit(check())

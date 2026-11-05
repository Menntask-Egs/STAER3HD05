"""Optional shared book footer; disable here to restore the footer-free layout."""
ENABLED = False
CSS = '''.book-footer{border-top:1px solid var(--line);margin:40px 0 0;padding:20px 0 28px;color:var(--muted);font-size:14px;line-height:1.65}.book-footer p{margin:0}.book-footer p+p{margin-top:4px}@media(max-width:600px){.book-footer{font-size:13px;margin-top:32px}}'''
HTML = '''<footer class="book-footer"><p>STÆR3HD05 · Heildun, deildajöfnur, runur og raðir</p><p>Menntaskólinn á Egilsstöðum · Vinnuútgáfa</p></footer>'''
def install(markup):
 if not ENABLED:return markup
 assert markup.count('</main>')==1
 return markup.replace('</main>',HTML+'</main>',1)

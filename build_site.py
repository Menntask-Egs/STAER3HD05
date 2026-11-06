"""Portable entry point for local builds and GitHub Actions (standard library only)."""
from pathlib import Path
import os
import runpy
import sys

ROOT = Path(__file__).resolve().parent
if __name__ == '__main__':
    os.chdir(ROOT)
    sys.path.insert(0, str(ROOT))
    sys.dont_write_bytecode = True
    (ROOT / 'dist').mkdir(exist_ok=True)
    runpy.run_path(str(ROOT / 'build_book.py'), run_name='__main__')
    from review_phase1 import apply
    apply(ROOT)
    from review_phase2 import apply as apply_second_review
    apply_second_review(ROOT)
    (ROOT / 'dist' / '.nojekyll').write_text('', encoding='utf-8')
    print('Ready: dist/index.html')

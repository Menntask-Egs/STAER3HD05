"""Number the authored units in their reading order without changing math or SVGs."""
import re
ORDER={2:2,7:3,3:4,4:5,5:6,6:7,8:8}
# Keep authored unit identities stable, translating their prose and links at build time.
def renumber_string(value):
 value=re.sub(r'unit-([3-7])\.html',lambda m:f'unit-{ORDER[int(m[1])]}.html',value)
 # Mathematical expressions, figures and tag attributes are not prose references.
 parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\)|<svg\b.*?</svg>|<[^>]+>)',value,flags=re.S)
 for i in range(0,len(parts),2):
  text=parts[i]
  text=re.sub(r'(?<![\d.])\b([3-7])\.(\d+)(\.\d+)?\b',lambda m:f'{ORDER[int(m[1])]}.{m[2]}{m[3] or ""}',text)
  text=re.sub(r'\b(eining(?:u|ar|um)?|kafl(?:a|i|anum)) ([3-7])\b',lambda m:f'{m[1]} {ORDER[int(m[2])]}',text,flags=re.I)
  text=text.replace('einingum 1–5','einingum 1–6')
  parts[i]=text
 return ''.join(parts)
def reorder(units):
 def visit(value):
  if isinstance(value,str):return renumber_string(value)
  if isinstance(value,tuple):return tuple(visit(x) for x in value)
  if isinstance(value,list):return [visit(x) for x in value]
  return value
 return {ORDER[n]:visit(units[n]) for n in ORDER}

#!/usr/bin/env python3
"""Emit a light quiz catalog and load tile metadata only on field entry."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
q=json.loads((root/'quiz-data.js').read_text().split('=',1)[1].strip().rstrip(';'))
folder=root/'slide-details';folder.mkdir(exist_ok=True)
for s in q:
 details={}
 for key in ['selectable20x','ultra']:
  g=s.get(key)
  if isinstance(g,dict) and 'tiles' in g:
   details[key]=g
   s[key]={k:v for k,v in g.items() if k not in ['tiles','parts']}
 if details:(folder/(s['id']+'.json')).write_text(json.dumps(details,ensure_ascii=False,separators=(',',':')))
(root/'quiz-runtime.js').write_text('window.QUIZ_DATA='+json.dumps(q,ensure_ascii=False,separators=(',',':'))+';\n')
print('Runtime bytes', (root/'quiz-runtime.js').stat().st_size)

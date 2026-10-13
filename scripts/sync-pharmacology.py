#!/usr/bin/env python3
"""Sync a reviewed standalone pharmacology HTML folder into the semester site."""
from pathlib import Path
import argparse,html,re
parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,required=True);args=parser.parse_args()
repo=Path(__file__).resolve().parents[1];semester='115-1';dest=repo/'pharmacology'/semester/'2';dest.mkdir(parents=True,exist_ok=True)
CSS=""":root{--ink:#2c2934;--muted:#6f6a78;--line:#e2dde7;--paper:#f8f6f2;--card:#fff;--purple:#665085;--deep:#30263e;--wash:#efeaf4}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 'Helvetica Neue',Helvetica,Arial,'PingFang TC',sans-serif}header{background:var(--deep);color:#fff;padding:18px 24px}header h1{font-size:23px;font-weight:500;margin:8px 0 2px}header p{color:#d8ccdf;font-size:13px;margin:0}nav{display:flex;gap:18px;flex-wrap:wrap;font-size:13px}nav a{color:#e5ddeb;text-decoration:none;min-height:28px}main{max-width:980px;margin:auto;padding:32px 24px 60px}h2{font-size:20px;font-weight:500;margin:0 0 20px}a{color:var(--purple);text-decoration:none}a:hover{text-decoration:underline}a:focus-visible{outline:3px solid #af99c6;outline-offset:4px}.rows{display:grid;gap:0}.row{padding:20px 0;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:18px}.row h3{font-size:20px;font-weight:500;margin:0 0 3px}.row p{font-size:14px;color:var(--muted);margin:0}.links{display:flex;gap:18px;flex-wrap:wrap}.pending{color:var(--muted);font-size:13px}.eyebrow{font-size:12px;color:var(--muted);margin:24px 0 10px}@media(max-width:600px){header{padding:16px}main{padding:24px 16px}.row{align-items:flex-start;flex-direction:column;gap:10px}.row h3{font-size:19px}}"""
def page(title,sub,content,nav):
 return '<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+CSS+'</style><header><nav>'+nav+'</nav><h1>'+html.escape(title)+'</h1><p>'+html.escape(sub)+'</p></header><main>'+content+'</main></html>'
def link(href,label):return '<a href="'+html.escape(href)+'">'+html.escape(label)+'</a>'
NAVCSS=""".site-nav{background:#30263e;color:#fff;display:flex;gap:20px;align-items:center;flex-wrap:wrap;padding:12px max(18px,calc((100vw - 1064px)/2));font:13px/1.6 'Helvetica Neue',Helvetica,Arial,sans-serif}.site-nav a{color:#e5ddeb;text-decoration:none}.site-nav a:hover{text-decoration:underline}.site-nav a:focus-visible{outline:3px solid #af99c6;outline-offset:3px}.embed .site-nav{display:none}"""
navbar='<div class="site-nav" aria-label="Site navigation">'+link('../../../115-1/','115-1')+link('../','Pharmacology')+link('./','Block 2')+link('../../../micro/115-1/','Pathology')+'</div><script>if(new URLSearchParams(location.search).get("embed")==="1")document.documentElement.classList.add("embed");</script>'
for src in args.source.glob('*.html'):
 if src.name=='開始複習.html':continue
 s=src.read_text();s=s.replace('</style>','\n'+NAVCSS+'</style>',1);s=s.replace('</style>','</style>'+navbar,1)
 (dest/src.name).write_text(s)
# Source notes are separate from the study UI. Local filesystem paths are not published.
notes=dest/'notes';notes.mkdir(exist_ok=True)
for src in args.source.glob('*來源*.md'):
 s=src.read_text();s=re.sub(r'/Users/[^\s；。，\n`]*','本機來源資料夾',s)
 (notes/src.name).write_text(s)
units=[('Autacoids · 自泌素','01-自泌素.html','01-自泌素-藥物速查.html'),('Antibiotics · 抗生素','02-抗生素.html','02-抗生素-藥物速查.html'),('NSAIDs & gout · 非類固醇抗炎與痛風','03-NSAIDs與痛風.html','03-NSAIDs與痛風-藥物速查.html'),('Adrenal corticosteroids · 腎上腺類固醇','04-腎上腺類固醇.html','04-腎上腺類固醇-藥物速查.html')]
rows=''.join('<div class="row"><div><h3>'+t+'</h3></div><div class="links">'+link(m,'Mechanisms · 機轉')+link(d,'Drug reference · 藥物速查')+'</div></div>' for t,m,d in units)
(dest/'index.html').write_text(page('Pharmacology · Block 2','115-1 藥理', '<div class="rows">'+rows+'</div>',link('../../../115-1/','115-1')+link('../','Pharmacology')+link('../../../micro/115-1/','Pathology')))
pharm=dest.parent
(pharm/'index.html').write_text(page('Pharmacology · 藥理','115-1', '<div class="rows"><div class="row"><div><h3>Block 1</h3><p>預留，之後補上</p></div>'+link('1/','Reserved · 預留')+'</div><div class="row"><div><h3>Block 2</h3><p>Mechanisms & drug reference · 機轉與藥物速查</p></div>'+link('2/','Open · 開始複習')+'</div></div>',link('../../115-1/','115-1')+link('../../micro/115-1/','Pathology')))
(pharm/'1').mkdir(exist_ok=True)
(pharm/'1/index.html').write_text(page('Pharmacology · Block 1','115-1 藥理','<h2>Reserved · 內容預留</h2><p class="pending">之後可補入本單元資料。</p>'+link('../2/','Go to Block 2'),link('../../../115-1/','115-1')+link('../','Pharmacology')))
hub=repo/'115-1';hub.mkdir(exist_ok=True)
(hub/'index.html').write_text(page('115-1 · Study workspace','課程複習', '<div class="rows"><div class="row"><div><h3>Pathology · 病理</h3><p>Micro · 切片複習</p></div>'+link('../micro/115-1/','Open · 開始複習')+'</div><div class="row"><div><h3>Pharmacology · 藥理</h3><p>Block 1 預留 · Block 2 已有內容</p></div>'+link('../pharmacology/115-1/','Open · 開始複習')+'</div><div class="row"><div><h3>Master tables · 總表</h3><p>之後加入跨科整合</p></div><span class="pending">Reserved · 預留</span></div></div>',link('../micro/115-1/','Pathology')+link('../pharmacology/115-1/','Pharmacology')))
micro=repo/'micro/115-1'
# Add the previously absent semester index; do not rewrite existing quiz pages.
rows=''.join('<div class="row"><div><h3>Micro 第'+str(i)+'次</h3><p>Pathology slide practice · 病理切片</p></div>'+link(str(i)+'/','Open · 開始複習')+'</div>' for i in [1,2,3])
(micro/'index.html').write_text(page('Pathology · 病理','115-1 · Micro', '<div class="rows">'+rows+'</div>',link('../../115-1/','115-1')+link('../../pharmacology/115-1/','Pharmacology')))
print('Synced',len(list(dest.glob('*.html'))),'pharmacology pages; semester hub and Micro index ready.')

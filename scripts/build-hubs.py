#!/usr/bin/env python3
"""Build the fixed Micro 115-1 main page and the redirects that point at it.

micro/115-1/ is the main page (its URL never changes). /pathology/, micro/ and
115-1/ forward to it or to notes; the old pharmacology copy forwards to notes.
"""
import json
from html import escape
from pathlib import Path

R = Path(__file__).resolve().parents[1]
NOTES = 'https://zi-yiii.github.io/notes/'
MAIN = 'https://zi-yiii.github.io/pathology/micro/115-1/'
EXAMS = [  # 依教學間表：10/08 考至感染系統、11/19 考至心血管、12/23
    (1, '2026-10-08', '細胞傷害、發炎、血行動力學與感染'),
    (2, '2026-11-19', '免疫疾病、兒童疾病、腫瘤與心血管'),
    (3, '2026-12-23', '呼吸、肝膽、頭頸、消化與胰臟'),
]
CSS = """*{box-sizing:border-box}[hidden]{display:none!important}body{margin:0;background:#fff;color:#263445;font:16px/1.7 -apple-system,BlinkMacSystemFont,'PingFang TC',sans-serif}main{max-width:980px;margin:auto;padding:24px 24px 64px}header{padding:18px 24px;border-bottom:1px solid #dde4e9}header>div{max-width:932px;margin:auto}nav{display:flex;gap:18px;flex-wrap:wrap;font-size:13px}a{color:#506e84;text-decoration:none}a:hover{text-decoration:underline}a:focus-visible{outline:3px solid #b6c6d2;outline-offset:3px}h1{font-size:27px;font-weight:550;margin:12px 0 3px}header p{font-size:14px;color:#617286;margin:0}.row{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:24px 0;border-bottom:1px solid #dde4e9}.row h2{display:flex;align-items:center;flex-wrap:wrap;gap:10px;font-size:21px;font-weight:550;margin:0 0 4px}.row p{color:#617286;font-size:14px;margin:0}.badge{font-size:12px;font-weight:600;line-height:1;padding:5px 9px;border-radius:999px;background:#e6edf1;color:#506e84}.badge.done{background:#f2f4f6;color:#8a95a1}.past h2{color:#617286}.actions{display:flex;gap:8px;flex:none}.actions a{display:inline-flex;align-items:center;justify-content:center;gap:4px;min-height:44px;padding:0 18px;border:1px solid #dde4e9;border-radius:8px;font-size:15px;white-space:nowrap}.actions a:hover{text-decoration:none;border-color:#506e84}.actions a.primary{background:#506e84;border-color:#506e84;color:#fff}.actions a.primary:hover{background:#435d70}.actions a.wrong{color:#617286}@media(max-width:600px){main{padding:12px 16px 48px}header{padding:16px}h1{font-size:24px}.row{flex-direction:column;align-items:stretch;gap:14px;padding:22px 0}.row h2{font-size:19px}.actions a{flex:1;padding:0 10px}}"""


def write(path, text):
    f = R / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text)


def alias(path, target):
    write(path, '<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
          f'<title>已搬到新位置</title><link rel="canonical" href="{escape(target)}"><p><a href="{escape(target)}">前往新位置</a></p>'
          f'<script>location.replace({json.dumps(target, ensure_ascii=False)}+location.search+location.hash)</script></html>')


quiz = json.loads((R / 'quiz-runtime.js').read_text().split('=', 1)[1].strip().rstrip(';'))
count = lambda e: sum(1 for s in quiz if s['exam'] == e or e in s.get('additionalExams', []))

rows = ''.join(
    f'<section class="row exam" data-exam="{n}" data-date="{day}"><div><h2>第 {n} 次切片考試<span class="badge" hidden></span></h2>'
    f'<p>{int(day[5:7]):02d}/{day[8:]} 考 · <span class="count">{count(n)}</span> 片 · {escape(topics)}</p></div>'
    f'<div class="actions"><a class="wrong" href="{n}/?practice=quiz&amp;mode=wrong" hidden>錯題 <span></span></a>'
    f'<a href="{n}/?practice=learn">學習</a><a class="primary" href="{n}/?practice=quiz">刷題 →</a></div></section>'
    for n, day, topics in EXAMS)
rows += ('<section class="row"><div><h2>切片導讀</h2><p>正常構造與病變對照，看片前先讀</p></div>'
         '<div class="actions"><a href="../../guide/">開啟導讀 →</a></div></section>')

# 考試狀態（已考／下一場）與各次錯題數；資料讀不到時保留建置時的片數
SCRIPT = """<script>
(()=>{const today=new Date().toLocaleDateString('sv');let next=false;
for(const r of document.querySelectorAll('.exam')){const b=r.querySelector('.badge');if(r.dataset.date<today){b.textContent='已考';b.classList.add('done');r.classList.add('past');b.hidden=false}else if(!next){next=true;b.textContent='下一場';b.hidden=false}}
const s=document.createElement('script');s.src='../../quiz-runtime.js';s.onload=()=>{let rec={};try{rec=JSON.parse(localStorage.getItem('quiz:rec'))||{}}catch{}
for(const r of document.querySelectorAll('.exam')){const e=Number(r.dataset.exam),list=(window.QUIZ_DATA||[]).filter(x=>x.exam===e||(x.additionalExams||[]).includes(e));if(!list.length)continue;r.querySelector('.count').textContent=list.length;
const w=list.filter(x=>rec[x.id]?.pending??((rec[x.id]?.bad||0)>0)).length,a=r.querySelector('.wrong');a.hidden=!w;a.querySelector('span').textContent=w}};document.body.append(s)})();
</script>"""

write('micro/115-1/index.html',
      '<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>病理切片・115-1</title><style>{CSS}</style><body><header><div><nav aria-label="位置">'
      f'<a href="{NOTES}">筆記首頁</a><a href="{NOTES}pathology/">病理</a><a href="{NOTES}pathology/lab/">實驗</a></nav>'
      '<h1>病理切片・115-1</h1><p>Micro · 三次切片考試的學習、刷題與導讀</p></div></header>'
      f'<main>{rows}</main>{SCRIPT}</body></html>')

alias('index.html', 'micro/115-1/')
alias('micro/index.html', '115-1/')
alias('115-1/index.html', NOTES)
for page in sorted((R / 'pharmacology').rglob('*.html')):
    rel = page.relative_to(R).as_posix()
    target = NOTES + (rel[:-len('index.html')] if rel.endswith('index.html') else rel)
    alias(rel, target)
print('Main page and redirects ready:', MAIN)

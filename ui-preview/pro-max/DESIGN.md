# B · UI UX Pro Max: 專注刷題

獨立 UI 預覽，保留原版刷題流程與圓形視野。三次考試資料沿用正式資料；練習紀錄隔離，不覆寫正式紀錄。

## Design Read
醫學生用電腦與 iPad 進行認片複習；Redesign / Overhaul 視覺，Preserve 功能。
變化 5/10，動態 2/10，密度 6/10，真實影像依存 9/10，品牌忠實度 5/10。
敘事：操作工作桌；距離：筆電與平板；氣氛：精準克制；內容：既有看片與判讀表單。

## Design system

:root{--ink:#193d3b;--muted:#516767;--line:#d1e1de;--paper:#f0f6f5;--card:#fff;--purple:#146b60;--deep:#fff;--wash:#e0efea;--ok:#146b60;--bad:#a44238;--hl:#d2ab29}body{font-family:'Plus Jakarta Sans','PingFang TC',sans-serif}header{background:var(--card);color:var(--ink);padding:24px max(24px,calc((100vw - 1360px)/2));display:grid;grid-template-columns:240px 1fr;align-items:start;border-bottom:1px solid var(--line)}.exam-links{margin:12px 0 0}.controls{justify-content:flex-end}.stats{width:100%;text-align:right;margin-top:8px}main{max-width:1360px;padding:24px 28px 60px;display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:18px 28px}.qhead,#coverage-note,#qnote,.reveal{grid-column:1/-1}.qhead{margin:6px 0}.whole,#tiles,#full{grid-column:1}.whole{border-radius:16px;background:var(--card)}.answer-box{grid-column:2;grid-row:3 / span 3;display:flex;flex-direction:column;align-items:stretch;margin:0;padding:24px;border:1px solid var(--line);border-radius:16px;background:var(--card);align-self:start;position:sticky;top:24px}.answer-box::before{content:'你的判讀';font-size:20px;font-weight:700;margin-bottom:10px}.answer-box>div{width:100%;margin-bottom:10px}.answer-box button{margin-top:8px}#detailbox{border-radius:20px}.detail-grid{padding:24px;gap:24px}.reveal{max-width:none}.preview-nav{background:var(--card)}@media(max-width:1000px){header{grid-template-columns:1fr}.controls{justify-content:flex-start}.stats{text-align:left}}@media(max-width:760px){header{padding:20px 16px}main{display:block;padding:20px 16px}.answer-box{margin-top:20px}.qhead{margin:20px 0}.detail-grid{padding:10px}}


## 行為
最小觸控目標 44px；可見焦點；不在病理影像周圍持續動畫；reduced-motion 支援。沿用 keyboard / touch / wrong retry / local persistence。

## 參考
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
Stitch 版依 taste-design 規則手工實作，未使用 Stitch MCP 生成。

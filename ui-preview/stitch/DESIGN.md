# A · Stitch: 留白工作台

獨立 UI 預覽，保留原版刷題流程與圓形視野。三次考試資料沿用正式資料；練習紀錄隔離，不覆寫正式紀錄。

## Design Read
醫學生用電腦與 iPad 進行認片複習；Redesign / Overhaul 視覺，Preserve 功能。
變化 5/10，動態 2/10，密度 4/10，真實影像依存 9/10，品牌忠實度 5/10。
敘事：操作工作桌；距離：筆電與平板；氣氛：精準克制；內容：既有看片與判讀表單。

## Design system

:root{--ink:#242626;--muted:#626969;--line:#dfe3e2;--paper:#f8f9f8;--card:#fff;--purple:#276b5b;--deep:#f8f9f8;--wash:#e9f1ee;--ok:#276b5b;--bad:#a44238;--hl:#d2ab29}body{display:grid;grid-template-columns:280px minmax(0,1fr);font-family:'Avenir Next','PingFang TC',sans-serif}.preview-nav{grid-column:1/-1}header{display:block;background:var(--paper);color:var(--ink);padding:40px 26px;border-right:1px solid var(--line)}header h1{font-weight:600}.controls{display:grid;gap:12px}.controls select,.controls button{width:100%;text-align:left;border-radius:6px}.stats{padding-top:22px;border-top:1px solid var(--line)}main{width:100%;padding:38px clamp(20px,4vw,64px);max-width:1300px}.qhead{margin:24px 0}.whole{border:0;border-radius:0;padding:0;background:transparent}.whole .map{max-width:800px}.answer-box{border-top:1px solid var(--line);padding-top:24px;margin-top:28px}.answer-box input{border-radius:4px}.whole figcaption{padding:12px 0}#coverage-note{max-width:66ch}.detail-grid{grid-template-columns:.8fr 1.2fr;gap:32px;padding:28px}#detailbox{border-radius:8px}.detail-map{border-radius:4px}.reveal{border-radius:6px}@media(max-width:900px){body{grid-template-columns:220px minmax(0,1fr)}header{padding:28px 18px}}@media(max-width:760px){body{display:block}header{border-right:0;border-bottom:1px solid var(--line);padding:20px 16px}.controls{display:flex}.controls select,.controls button{width:auto}.stats{width:100%;padding-top:12px}.exam-links{margin:12px 0}main{padding:20px 16px}.detail-grid{grid-template-columns:1fr}}


## 行為
最小觸控目標 44px；可見焦點；不在病理影像周圍持續動畫；reduced-motion 支援。沿用 keyboard / touch / wrong retry / local persistence。

## 參考
https://github.com/google-labs-code/stitch-skills
Stitch 版依 taste-design 規則手工實作，未使用 Stitch MCP 生成。

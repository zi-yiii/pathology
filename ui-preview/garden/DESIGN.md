# C · Garden: 閱讀工作桌

獨立 UI 預覽，保留原版刷題流程與圓形視野。三次考試資料沿用正式資料；練習紀錄隔離，不覆寫正式紀錄。

## Design Read
醫學生用電腦與 iPad 進行認片複習；Redesign / Overhaul 視覺，Preserve 功能。
變化 7/10，動態 2/10，密度 4/10，真實影像依存 9/10，品牌忠實度 5/10。
敘事：操作工作桌；距離：筆電與平板；氣氛：安靜溫暖；內容：既有看片與判讀表單。

## Design system

:root{--ink:#3c382e;--muted:#746d60;--line:#e2dbce;--paper:#eeeae0;--card:#fbf9f3;--purple:#795039;--deep:#fbf9f3;--wash:#e9decd;--ok:#35694a;--bad:#a44238;--hl:#d2ab29}body{font-family:'Optima','PingFang TC',sans-serif}.preview-nav{background:var(--paper);border:0}header{max-width:1260px;margin:20px auto 0;background:transparent;color:var(--ink);padding:0 36px;display:block}header h1{font-size:36px;font-weight:500}.brand-row{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line);padding-bottom:18px}.exam-links{margin:0}.controls{padding:18px 0;border-bottom:1px solid var(--line);gap:10px}.controls select,.controls button{background:transparent;border-radius:24px;padding:8px 16px}.stats{margin-left:auto}main{max-width:1260px;padding:26px 36px 64px}.qhead{margin:26px 0 18px}.qhead h2{font-weight:500;font-size:32px}.whole{border:0;border-radius:24px;background:var(--card);padding:24px;box-shadow:0 12px 32px #65553c09}.whole .map{max-width:740px}.answer-box{margin:24px 0;grid-template-columns:1fr 1.6fr auto;gap:18px}.answer-box input{background:transparent;border:0;border-bottom:1px solid var(--muted);border-radius:0;padding-left:0}.answer-box button{border-radius:30px;padding:12px 28px}#detailbox{background:var(--card);border-radius:28px}.detail-grid{gap:28px;padding:24px}.modalbar{border-color:var(--line)}.detail-nav button{border-radius:24px}.reveal{background:var(--card);border:0;border-radius:24px;padding:28px}.preview-tag{letter-spacing:0}@media(max-width:760px){header{padding:0 16px;margin-top:12px}header h1{font-size:28px}.brand-row{align-items:flex-start}.stats{width:100%;margin-left:0}main{padding:18px 16px}.whole{padding:12px;border-radius:16px}.answer-box{display:grid;grid-template-columns:1fr}.detail-grid{padding:10px}}


## 行為
最小觸控目標 44px；可見焦點；不在病理影像周圍持續動畫；reduced-motion 支援。沿用 keyboard / touch / wrong retry / local persistence。

## 參考
https://github.com/ConardLi/garden-skills
Stitch 版依 taste-design 規則手工實作，未使用 Stitch MCP 生成。

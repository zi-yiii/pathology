/* 頂部工具列：刷題／學習、講次、進度直接放在上方；側欄仍保留完整設定。 */
(()=>{
 const nav=document.querySelector('.preview-nav'),practice=document.getElementById('practice-kind'),scope=document.getElementById('scope'),title=document.getElementById('qtitle'),form=document.querySelector('.beta-settings');
 if(!nav||!practice||!scope||!title)return;
 const bar=document.createElement('div');bar.className='quiz-toolbar';
 const sw=document.createElement('div');sw.className='toolbar-switch';sw.setAttribute('role','group');sw.setAttribute('aria-label','練習模式');
 const buttons=[['quiz','刷題'],['learn','學習']].map(([value,label])=>{const b=document.createElement('button');b.type='button';b.textContent=label;b.onclick=()=>{if(practice.value===value)return;practice.value=value;practice.dispatchEvent(new Event('change',{bubbles:true}))};sw.append(b);return [value,b]});
 const pick=document.createElement('select');pick.className='toolbar-scope';pick.setAttribute('aria-label','講次範圍');
 pick.replaceChildren(...[...scope.options].map(o=>new Option(o.text,o.value)));pick.value=scope.value;pick.hidden=scope.options.length<=1;
 pick.onchange=()=>{scope.value=pick.value;scope.dispatchEvent(new Event('change',{bubbles:true}));if(form?.elements.scope)form.elements.scope.value=pick.value};
 const progress=document.createElement('span');progress.className='toolbar-progress';
 bar.append(sw,pick,progress);nav.insertBefore(bar,nav.querySelector('.preview-tag'));
 // 手機只留「第 N 次」
 const tag=nav.querySelector('.preview-tag'),m=tag&&/^(.*· )(第 \d+ 次)$/.exec(tag.textContent);
 if(m){tag.replaceChildren();const long=document.createElement('span');long.className='tag-long';long.textContent=m[1];tag.append(long,m[2]);}
 function sync(){
  const learning=practice.value==='learn';
  buttons.forEach(([value,b])=>b.setAttribute('aria-pressed',String(value===practice.value)));
  if(form?.elements.practice)form.elements.practice.value=practice.value;
  if(pick.value!==scope.value)pick.value=scope.value;
  const p=/^第 (\d+) 輪 · (\d+) \/ (\d+)$/.exec(title.textContent);
  progress.hidden=learning||!p;if(p){progress.textContent=`${p[2]} / ${p[3]}`;progress.title=`第 ${p[1]} 輪`;}
  if(typeof cur!=='undefined'&&cur)window.Detail20x?.prefetch?.(cur);
 }
 practice.addEventListener('change',sync);new MutationObserver(sync).observe(title,{childList:true,characterData:true,subtree:true});sync();
})();

(()=>{
const s=window.TEST_SLIDE,g=s.selectable20x,h=s.ultra,$=id=>document.getElementById(id);
let mode=10, highItem,ready=false;
const viewer=OpenSeadragon({id:'viewer',showNavigationControl:false,showNavigator:false,animationTime:.18,blendTime:.12,imageLoaderLimit:6,maxImageCacheCount:120,minPixelRatio:.5,visibilityRatio:.1,constrainDuringPan:true,gestureSettingsMouse:{scrollToZoom:false,clickToZoom:false,dblClickToZoom:false},gestureSettingsTouch:{pinchToZoom:false,clickToZoom:false,dblClickToZoom:false},maxZoomPixelRatio:8});
function source(meta,base){const tiles=new Set(meta.tiles);return {width:meta.width,height:meta.height,tileSize:meta.tileSize,minLevel:0,maxLevel:0,getLevelScale:()=>1,getTileUrl:(level,x,y)=>`${base}/r${y}c${x}.jpg`,tileExists:(level,x,y)=>tiles.has(`${y},${x}`)};}
function status(){const pending=viewer.imageLoader.jobsInProgress||0;$('status').textContent=`${mode}× · 圓形直徑 ${mode===10?'1.80':'0.45'} mm · ${mode===10?'目前畫質':'高一層畫質'}${pending?' · 細節載入中…':''}`;}
function mark(){if(!ready)return;const c=viewer.viewport.getCenter(true),diam=(mode===10?1800:450)/(g.width*g.mpp);$('marker').style.cssText=`left:${c.x*100}%;top:${c.y/(g.height/g.width)*100}%;width:${diam*100}%;height:${diam/(g.height/g.width)*100}%`;status();}
function field(n,center){mode=n;highItem?.setOpacity(n===40?1:0);$('ten').setAttribute('aria-pressed',n===10);$('forty').setAttribute('aria-pressed',n===40);const c=center||viewer.viewport.getCenter();const w=(n===10?1800:450)/(g.width*g.mpp);viewer.viewport.fitBounds(new OpenSeadragon.Rect(c.x-w/2,c.y-w/2,w,w),true);$('scale').textContent=`100 µm = 圓形直徑的 ${n===10?'1/18':'2/9'}`;mark();}
viewer.addTiledImage({tileSource:source(g,s.hiBase),width:1,success:()=>{viewer.addTiledImage({tileSource:source(h,s.ultraBase),width:1,opacity:0,success:event=>{highItem=event.item;ready=true;field(10,new OpenSeadragon.Point(.4,.7*g.height/g.width));}})}});
viewer.addHandler('animation',mark);viewer.addHandler('tile-loaded',mark);viewer.addHandler('tile-drawn',mark);viewer.addHandler('tile-load-failed',()=>{$('status').textContent='部分細節未載入，請稍後重新整理';});
$('map').src=`${s.assetBase||'slides/'+s.id}/overview.jpg`;
$('map').onclick=e=>{if(!ready)return;const r=e.currentTarget.getBoundingClientRect();field(mode,new OpenSeadragon.Point((e.clientX-r.left)/r.width,(e.clientY-r.top)/r.height*g.height/g.width));};
$('ten').onclick=()=>ready&&field(10);$('forty').onclick=()=>ready&&field(40);$('reset').onclick=()=>ready&&field(mode,new OpenSeadragon.Point(.4,.7*g.height/g.width));
function move(dx,dy,speed=1){if(!ready)return;const step=(mode===10?1800:450)/(g.width*g.mpp)*.25*speed;viewer.viewport.panBy(new OpenSeadragon.Point(dx*step,dy*step));viewer.viewport.applyConstraints();}
for(const [id,dx,dy] of [['left',-1,0],['right',1,0],['up',0,-1],['down',0,1]])$(id).onclick=()=>move(dx,dy);
const keys={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]};document.addEventListener('keydown',e=>{if(e.altKey||e.ctrlKey||e.metaKey||!keys[e.key])return;e.preventDefault();move(...keys[e.key],e.shiftKey?2:1);});
})();

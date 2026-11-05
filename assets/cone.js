(()=>{
const lab=document.getElementById('cone-lab');if(!lab)return;
const $=id=>document.getElementById('cone-'+id),angle=$('angle'),slice=$('slice'),yaw=$('yaw'),pitch=$('pitch'),show=$('show'),canvas=$('space'),ctx=canvas.getContext('2d'),plane=$('plane');
const fmt=n=>Number(n.toFixed(2)).toString().replace('.',',');let playing=false,last=0,frame=0;
function project(p){const a=Number(yaw.value)*Math.PI/180,b=Number(pitch.value)*Math.PI/180;const X=p[0]-1,Y=p[1],Z=p[2];const h=Math.cos(a)*X-Math.sin(a)*Z,d=Math.sin(a)*X+Math.cos(a)*Z;return [h,Math.cos(b)*Y-Math.sin(b)*d,Math.sin(b)*Y+Math.cos(b)*d];}
function draw(){const theta=Number(angle.value)*Math.PI/180,t=Number(slice.value),visible=show.checked;
$('angle-value').textContent=angle.value+'°';$('slice-value').textContent='x = '+fmt(t);
$('readout').textContent='Við x = '+fmt(t)+' er geislinn '+fmt(t)+' og flatarmál fullrar skífu π · '+fmt(t)+'² ≈ '+fmt(Math.PI*t*t)+' ferningseiningar.';
$('progress').textContent='Sýndur snúningur: '+angle.value+'° af 360°. '+(Number(angle.value)===360?'Nú er keilan heil.':Number(angle.value)===0?'Svæðið er enn flatt.':'Opni hlutinn sýnir að snúningurinn er ólokinn.');
plane.innerHTML='<polygon points="50,280 270,280 270,60" fill="#dedede"/><path d="M30 280H305 M50 300V30 M50 280L270 60" fill="none" stroke="black" stroke-width="2"/><path d="M160 276V284 M270 276V284 M46 170H54 M46 60H54" stroke="black"/><g fill="black" font-size="16"><text x="33" y="302">0</text><text x="155" y="304">1</text><text x="265" y="304">2</text><text x="28" y="176">1</text><text x="28" y="66">2</text><text x="310" y="278">x</text><text x="57" y="26">y</text><text x="140" y="105">y = x</text></g>'+(visible?'<path d="M'+(50+t*110)+' 280V'+(280-t*110)+'" stroke="#175a4d" stroke-width="5"/><circle cx="'+(50+t*110)+'" cy="'+(280-t*110)+'" r="4" fill="#175a4d"/>':'');
plane.setAttribute('aria-label','Svæðið undir y=x á [0,2]. '+(visible?'Sneið við x='+fmt(t)+', geisli '+fmt(t)+'.':''));
const size=canvas.getBoundingClientRect().width||360,dpr=window.devicePixelRatio||1;canvas.width=Math.round(size*dpr);canvas.height=Math.round(size*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);ctx.fillStyle='white';ctx.fillRect(0,0,size,size);const scale=size/5.9,cx=size*.5,cy=size*.5;
const screen=p=>{const v=project(p);return [cx+v[0]*scale,cy-v[1]*scale,v[2]]};
function path(points,fill,stroke,width=1){const pp=points.map(screen);ctx.beginPath();pp.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));if(fill){ctx.closePath();ctx.fillStyle=fill;ctx.fill()}if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=width;ctx.stroke()}}
function text(p,label,color='black'){const q=screen(p);ctx.font='14px system-ui';ctx.fillStyle=color;ctx.fillText(label,q[0]+5,q[1]-5)}
path([[-.25,0,0],[2.55,0,0]],null,'#777');path([[0,-2.25,0],[0,2.35,0]],null,'#bbb');path([[0,0,-2.25],[0,0,2.35]],null,'#bbb');
const faces=[],segments=Math.max(1,Math.ceil(theta/(Math.PI/36))),point=(x,a)=>[x,x*Math.cos(a),x*Math.sin(a)];
function face(points,fill,stroke){faces.push({points,fill,stroke,depth:points.reduce((s,p)=>s+project(p)[2],0)/points.length})}
if(theta>0){for(let i=0;i<segments;i++){const a=theta*i/segments,b=theta*(i+1)/segments;face([[0,0,0],point(2,a),point(2,b)],'rgba(170,180,185,.32)','#c5cacc');face([[2,0,0],point(2,a),point(2,b)],'rgba(200,208,212,.25)',null)}if(theta<Math.PI*2-.001){face([[0,0,0],[2,0,0],point(2,0)],'rgba(225,230,232,.45)','#777');face([[0,0,0],[2,0,0],point(2,theta)],'rgba(215,225,230,.45)','#777')}
if(visible&&t>0){for(let i=0;i<segments;i++)face([[t,0,0],point(t,theta*i/segments),point(t,theta*(i+1)/segments)],'rgba(23,90,77,0.65)',null)}
faces.sort((a,b)=>a.depth-b.depth).forEach(f=>path(f.points,f.fill,f.stroke,.45));
// Sparse wireframe outlines make the curved surface visible without hiding the selected sector.
for(let k=1;k<=4;k++){const x=k*.5,pts=[];for(let i=0;i<=segments;i++)pts.push(point(x,theta*i/segments));path(pts,null,k===4?'#30383a':'rgba(50,60,65,.22)',k===4?1.5:.7)}
path([[0,0,0],point(2,0)],null,'#333',1.2);path([[0,0,0],point(2,theta)],null,'#333',1.2);
}else path([[0,0,0],[2,0,0],[2,2,0]],'#dedede','#333',1.5);
path([[-.15,0,0],[2.5,0,0]],null,'#222',1.4);text([2.5,0,0],'x');text([0,2.25,0],'y');text([0,0,2.25],'z');text([0,0,0],'0');text([2,0,0],'2');
if(visible){const arc=[];for(let i=0;i<=segments;i++)arc.push(point(t,theta*i/segments));path(arc,null,'#175a4d',2.5);path([[t,0,0],point(t,theta)],null,'#175a4d',3);text([t,t*.5*Math.cos(theta),t*.5*Math.sin(theta)],'R = '+fmt(t),'#175a4d');}
canvas.setAttribute('aria-label','Þrívíður snúningur svæðisins undir y=x um x-ás. Snúningur '+angle.value+' gráður. '+(visible?'Valin sneið við x='+fmt(t)+'.':''));
}
function stop(){playing=false;cancelAnimationFrame(frame);$('play').textContent='Spila snúning';last=0;}
// Retain fractional animation progress even though the range control uses whole degrees.
let progress=0;function tick(now){if(!playing)return;if(lab.closest('section').hidden){stop();return}if(last){progress=Math.min(360,progress+(now-last)*.06);angle.value=Math.round(progress);draw()}last=now;if(progress>=360){stop();return}frame=requestAnimationFrame(tick)}
$('play').addEventListener('click',()=>{if(playing){stop();return}if(Number(angle.value)>=360)angle.value=0;progress=Number(angle.value);playing=true;last=0;$('play').textContent='Gera hlé';frame=requestAnimationFrame(tick)});
angle.addEventListener('input',()=>{stop();draw()});[slice,yaw,pitch,show].forEach(c=>c.addEventListener('input',draw));$('reset').addEventListener('click',()=>{stop();angle.value=0;slice.value=1;show.checked=true;draw()});$('view-reset').addEventListener('click',()=>{yaw.value=-35;pitch.value=25;draw()});
let drag=null;canvas.addEventListener('pointerdown',e=>{drag=[e.clientX,e.clientY,Number(yaw.value),Number(pitch.value)];canvas.setPointerCapture(e.pointerId)});canvas.addEventListener('pointermove',e=>{if(!drag)return;yaw.value=Math.max(-160,Math.min(160,drag[2]+(e.clientX-drag[0])*.5));pitch.value=Math.max(10,Math.min(75,drag[3]+(e.clientY-drag[1])*.3));draw()});['pointerup','pointercancel','lostpointercapture'].forEach(k=>canvas.addEventListener(k,()=>drag=null));
new ResizeObserver(draw).observe(canvas);window.addEventListener('hashchange',()=>{if(lab.closest('section').hidden)stop()});draw();
})();

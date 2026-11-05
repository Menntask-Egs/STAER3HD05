(()=>{
const fmt=n=>Number(n.toFixed(2)).toString().replace('.',',');
const defs={
'cylinder':{axis:'x',a:0,b:3,ro:t=>2,ri:t=>0,xmax:3,ymax:2,lo:x=>0,hi:x=>2,formula:'V = π ∫₀³ 2² dx = 12π cm³.'},
'washer-x':{axis:'x',a:0,b:1,ro:t=>1,ri:t=>t*t,xmax:1,ymax:1,lo:x=>x*x,hi:x=>1,formula:'V = π ∫₀¹ (1 − x⁴) dx = 4π/5.'},
'paraboloid-y':{axis:'y',a:0,b:4,ro:t=>Math.sqrt(t),ri:t=>0,xmax:2,ymax:4,lo:x=>x*x,hi:x=>4,formula:'V = π ∫₀⁴ y dy = 8π.'},
'washer-y':{axis:'y',a:0,b:1,ro:t=>2*t,ri:t=>t,xmax:2,ymax:1,horizontal:true,left:y=>y,right:y=>2*y,formula:'V = π ∫₀¹ ((2y)² − y²) dy = π.'},
'shell-y':{axis:'y',a:0,b:1,ro:t=>Math.sqrt(t),ri:t=>0,xmax:1,ymax:1,lo:x=>x*x,hi:x=>1,sa:0,sb:1,bottom:r=>r*r,top:r=>1,formula:'V = 2π ∫₀¹ x(1 − x²) dx = π/2.'},
'shell-x':{axis:'x',a:0,b:1,ro:t=>1,ri:t=>t*t,xmax:1,ymax:1,lo:x=>x*x,hi:x=>1,sa:0,sb:1,bottom:r=>0,top:r=>Math.sqrt(r),formula:'V = 2π ∫₀¹ y√y dy = 4π/5.'}
};defs['compare-y']={...defs['shell-y'],formula:'Skífur: V = π ∫₀¹ y dy = π/2. Hólkar: V = 2π ∫₀¹ x(1 − x²) dx = π/2.'};
document.querySelectorAll('.solid-lab').forEach(lab=>{
const d=defs[lab.dataset.solid],$=p=>lab.querySelector('[data-part="'+p+'"]'),cv=$('space'),ctx=cv.getContext('2d');let running=false,frame=0,last=0,progress=0,drag=null;
function stop(){running=false;cancelAnimationFrame(frame);last=0;$('play').textContent='Spila snúning'}
function draw(){if(lab.closest('section').hidden)return;const alpha=Number($('angle').value)*Math.PI/180,shell=$('mode').value==='shell',q=Number($('slice').value)/100,t=shell?d.sa+q*(d.sb-d.sa):d.a+q*(d.b-d.a),R=shell?t:d.ro(t),r=shell?0:d.ri(t),low=shell?d.bottom(t):t,high=shell?d.top(t):t;
$('angle-value').textContent=$('angle').value+'°';$('slice-value').textContent=(shell?(d.axis==='y'?'x':'y'):d.axis)+' = '+fmt(t);
$('readout').textContent=shell?'Geisli ρ = '+fmt(t)+'. Hæð h = '+fmt(high-low)+'. Ummál × hæð = 2π · '+fmt(t)+' · '+fmt(high-low)+' ≈ '+fmt(2*Math.PI*t*(high-low))+'. Þetta er rúmmál á hverja þykktareiningu; sneiðin hefur líka litla þykkt.':'Ytri geisli R = '+fmt(R)+'. Innri geisli r = '+fmt(r)+'. Flatarmál fulls þversniðs π(R² − r²) ≈ '+fmt(Math.PI*(R*R-r*r))+'.';
$('progress').textContent='Snúið um '+d.axis+'-ás: '+$('angle').value+'°. '+(alpha===0?'Svæðið er enn flatt.':alpha>=2*Math.PI?'Snúningnum er lokið.':'Sneiðin hefur enn aðeins myndað hluta úr '+(shell?'hólkskel.':'þversniði.'));
// Original region and the corresponding slice, with equal axis units.
const max=Math.max(d.xmax,d.ymax),scale=260/max,ox=45,oy=310,pt=(x,y)=>[ox+x*scale,oy-y*scale],coord=p=>p.join(',');let region=[];
for(let i=0;i<=80;i++){if(d.horizontal){let y=d.ymax*i/80;region.push(pt(d.right(y),y))}else{let x=d.xmax*i/80;region.push(pt(x,d.hi(x)))}}
for(let i=80;i>=0;i--){if(d.horizontal){let y=d.ymax*i/80;region.push(pt(d.left(y),y))}else{let x=d.xmax*i/80;region.push(pt(x,d.lo(x)))}}
const vertical=shell?d.axis==='y':d.axis==='x';const A=vertical?pt(t,shell?low:r):pt(shell?low:r,t),B=vertical?pt(t,shell?high:R):pt(shell?high:R,t);let ticks='';for(let i=1;i<=d.xmax;i++)ticks+='<text x="'+pt(i,0)[0]+'" y="332" text-anchor="middle">'+i+'</text>';for(let i=1;i<=d.ymax;i++)ticks+='<text x="30" y="'+(pt(0,i)[1]+5)+'" text-anchor="end">'+i+'</text>';
$('plane').innerHTML='<polygon points="'+region.map(coord).join(' ')+'" fill="#dedede" stroke="black" stroke-width="1.7"/><path d="M25 310H330 M45 330V15" stroke="#777" fill="none"/><path d="'+(d.axis==='x'?'M25 310H330':'M45 330V15')+'" stroke="black" stroke-width="3"/><path d="M'+coord(A)+'L'+coord(B)+'" stroke="#175a4d" stroke-width="5"/><g fill="black" font-size="14"><text x="29" y="332">0</text><text x="335" y="307">x</text><text x="50" y="15">y</text>'+ticks+'</g>';
$('plane').setAttribute('aria-label','Skyggða svæðið. Snúningsás '+d.axis+'. '+(vertical?'Lóðrétt':'Lárétt')+' sneið við '+fmt(t)+'.');
const size=cv.getBoundingClientRect().width||360,pixel=window.devicePixelRatio||1;cv.width=size*pixel;cv.height=size*pixel;ctx.setTransform(pixel,0,0,pixel,0,0);ctx.fillStyle='white';ctx.fillRect(0,0,size,size);
const yaw=Number($('yaw').value)*Math.PI/180,pitch=Number($('pitch').value)*Math.PI/180,extent=Math.max(d.b-d.a,2*d.ro(d.b),2*d.ro(d.a)),sc=size/(extent*1.65),center=(d.a+d.b)/2;
function world(a,r,theta){return d.axis==='x'?[a,r*Math.cos(theta),r*Math.sin(theta)]:[r*Math.cos(theta),a,r*Math.sin(theta)]}
function project(p){const X=p[0]-(d.axis==='x'?center:0),Y=p[1]-(d.axis==='y'?center:0),Z=p[2],h=Math.cos(yaw)*X-Math.sin(yaw)*Z,depth=Math.sin(yaw)*X+Math.cos(yaw)*Z;return [size/2+h*sc,size/2-(Math.cos(pitch)*Y-Math.sin(pitch)*depth)*sc,Math.sin(pitch)*Y+Math.cos(pitch)*depth]}
function path(points,fill,stroke,width=1){const ps=points.map(project);ctx.beginPath();ps.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));if(fill){ctx.closePath();ctx.fillStyle=fill;ctx.fill()}if(stroke){ctx.lineWidth=width;ctx.strokeStyle=stroke;ctx.stroke()}}
const faces=[],N=Math.max(1,Math.ceil(alpha/(Math.PI/18))),M=14;function face(points,fill,stroke){faces.push({points,fill,stroke,z:points.reduce((s,p)=>s+project(p)[2],0)/points.length})}
if(alpha>0){for(let j=0;j<M;j++){const a=d.a+(d.b-d.a)*j/M,b=d.a+(d.b-d.a)*(j+1)/M;for(let k=0;k<N;k++){const u=alpha*k/N,v=alpha*(k+1)/N;face([world(a,d.ro(a),u),world(b,d.ro(b),u),world(b,d.ro(b),v),world(a,d.ro(a),v)],'rgba(160,175,185,.22)','#c7ced2');if(d.ri(a)||d.ri(b))face([world(a,d.ri(a),u),world(b,d.ri(b),u),world(b,d.ri(b),v),world(a,d.ri(a),v)],'rgba(130,145,155,.18)',null)}
if(alpha<2*Math.PI-.001)for(const th of [0,alpha])face([world(a,d.ri(a),th),world(b,d.ri(b),th),world(b,d.ro(b),th),world(a,d.ro(a),th)],'rgba(200,210,218,.28)','#999')}
for(const end of [d.a,d.b])for(let k=0;k<N;k++)face([world(end,d.ri(end),alpha*k/N),world(end,d.ro(end),alpha*k/N),world(end,d.ro(end),alpha*(k+1)/N),world(end,d.ri(end),alpha*(k+1)/N)],'rgba(190,200,210,.22)',null);
for(let k=0;k<N;k++){const u=alpha*k/N,v=alpha*(k+1)/N;face(shell?[world(low,t,u),world(high,t,u),world(high,t,v),world(low,t,v)]:[world(t,r,u),world(t,R,u),world(t,R,v),world(t,r,v)],'rgba(23,90,77,.62)',null)}
faces.sort((a,b)=>a.z-b.z).forEach(f=>path(f.points,f.fill,f.stroke,.4));
for(const a of [d.a,d.b])for(const radius of [d.ro(a),d.ri(a)]){let arc=[];for(let i=0;i<=N;i++)arc.push(world(a,radius,alpha*i/N));path(arc,null,'#465159',1.4)}
for(const a of shell?[low,high]:[t]){let arc=[];for(let i=0;i<=N;i++)arc.push(world(a,shell?t:R,alpha*i/N));path(arc,null,'#175a4d',2.5)}
}else path(region.map(p=>[(p[0]-ox)/scale,(oy-p[1])/scale,0]),'#dedede','#333',1.5);
const cross=Math.max(.5,d.ro(d.a),d.ro(d.b))*1.12;
const axes=[{name:'x',from:d.axis==='x'?[d.a-.15,0,0]:[-cross,0,0],to:d.axis==='x'?[d.b+.3,0,0]:[cross,0,0]},{name:'y',from:d.axis==='y'?[0,d.a-.15,0]:[0,-cross,0],to:d.axis==='y'?[0,d.b+.3,0]:[0,cross,0]},{name:'z',from:[0,0,-cross],to:[0,0,cross]}];
ctx.font='15px system-ui';for(const axis of axes){path([axis.from,axis.to],null,axis.name===d.axis?'#222':'#b3b3b3',axis.name===d.axis?1.7:1);const end=project(axis.to);ctx.fillStyle='#333';ctx.fillText(axis.name,end[0]+5,end[1]-5)}
cv.setAttribute('aria-label','Snúður um '+d.axis+'-ás. Snúningur '+$('angle').value+' gráður. '+(shell?'Hólkskel':'Þversnið')+' við '+fmt(t)+'.');
}
function tick(now){if(!running)return;if(lab.closest('section').hidden){stop();return}if(last){progress=Math.min(360,progress+(now-last)*.06);$('angle').value=Math.round(progress);draw()}last=now;if(progress>=360){stop();return}frame=requestAnimationFrame(tick)}
$('play').addEventListener('click',()=>{if(running){stop();return}progress=Number($('angle').value);if(progress>=360)progress=0;running=true;last=0;$('play').textContent='Gera hlé';frame=requestAnimationFrame(tick)});$('angle').addEventListener('input',()=>{stop();draw()});['slice','yaw','pitch','mode'].forEach(p=>$(p).addEventListener('input',draw));$('reset').addEventListener('click',()=>{stop();$('angle').value=0;$('slice').value=50;draw()});$('view').addEventListener('click',()=>{$('yaw').value=-35;$('pitch').value=25;draw()});cv.addEventListener('pointerdown',e=>{drag=[e.clientX,e.clientY,Number($('yaw').value),Number($('pitch').value)];cv.setPointerCapture(e.pointerId)});cv.addEventListener('pointermove',e=>{if(!drag)return;$('yaw').value=Math.max(-160,Math.min(160,drag[2]+(e.clientX-drag[0])*.5));$('pitch').value=Math.max(10,Math.min(75,drag[3]+(e.clientY-drag[1])*.3));draw()});['pointerup','pointercancel','lostpointercapture'].forEach(e=>cv.addEventListener(e,()=>drag=null));new ResizeObserver(draw).observe(cv);window.addEventListener('hashchange',()=>{stop();draw()});draw();
});
})();

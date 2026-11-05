(() => {
 const graph=document.getElementById('exp-graph');if(!graph)return;
 const aSlider=document.getElementById('exp-a'),cSlider=document.getElementById('exp-c');
 const fmt=n=>String(n).replace('-', '−').replace('.', ',');
 const px=x=>100+40*x,py=y=>300-40*y;
 function draw(){
  const a=Number(aSlider.value),c=Number(cSlider.value);
  let d='';
  for(let i=0;i<=300;i++){
   const x=-1.5+i*8/300,y=c*Math.exp(-a*x);
   d+=(i?'L':'M')+px(x).toFixed(2)+','+py(y).toFixed(2);
  }
  let picture='<defs><clipPath id="exp-clip"><rect x="35" y="30" width="355" height="450"/></clipPath></defs><g clip-path="url(#exp-clip)"><path d="'+d+'" stroke="black" stroke-width="3" fill="none"/></g><path d="M35 300H390 M100 480V30" stroke="black" fill="none"/>';
  for(let x=-1;x<=6;x++)if(x!==0)picture+='<path d="M'+px(x)+' 296v8" stroke="black"/><text x="'+px(x)+'" y="323" text-anchor="middle" font-size="15" fill="black">'+fmt(x)+'</text>';
  for(let y=-4;y<=6;y++)if(y!==0)picture+='<path d="M96 '+py(y)+'h8" stroke="black"/><text x="87" y="'+(py(y)+5)+'" text-anchor="end" font-size="15" fill="black">'+fmt(y)+'</text>';
  picture+='<text x="84" y="323" font-size="15" fill="black">0</text><text x="397" y="294" fill="black">x</text><text x="111" y="32" fill="black">y</text><circle cx="100" cy="'+py(c)+'" r="5" fill="#175d50"/>';
  graph.innerHTML=picture;
  document.getElementById('exp-a-value').textContent=fmt(a);document.getElementById('exp-c-value').textContent=fmt(c);
  const exponent=-a;
  const equation=c===0?'y = 0':a===0?'y = '+fmt(c):'y = '+fmt(c)+' · e<sup>'+(exponent===1?'':exponent===-1?'−':fmt(exponent))+'x</sup>';
  document.getElementById('exp-equation').innerHTML=equation+'. Upphafsgildið er y(0) = '+fmt(c)+'.';
  let behaviour;
  if(c===0)behaviour='Núlllausnin: y er alltaf 0, óháð a.';
  else if(a===0)behaviour='Afleiðan er 0. Lausnin er fastafall.';
  else if(a>0)behaviour=c>0?'Fallið minnkar og stefnir á núll ofan frá þegar x vex.':'Fallið hækkar og stefnir á núll neðan frá þegar x vex.';
  else behaviour=c>0?'Fallið vex þegar x vex.':'Fallgildin verða sífellt neikvæðari þegar x vex.';
  document.getElementById('exp-behaviour').textContent=behaviour+' Hallinn við x = 0 er y′(0) = '+fmt(-a*c)+'.';
  graph.setAttribute('aria-label','Lausnarferill með a = '+fmt(a)+' og y(0) = '+fmt(c)+'. '+behaviour);
 }
 aSlider.addEventListener('input',draw);cSlider.addEventListener('input',draw);draw();
})();

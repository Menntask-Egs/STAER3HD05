(() => {
 const graph=document.getElementById('forced-graph');
 const fmt=n=>String(n).replace('-','−').replace('.',',');
 if(graph){
  const slider=document.getElementById('forced-start');
  const px=x=>90+45*x,py=y=>360-45*y;
  function draw(){
   const start=Number(slider.value),c=start-3;let d='';
   for(let i=0;i<=300;i++){const x=-1.2+7.7*i/300;d+=(i?'L':'M')+px(x).toFixed(2)+','+py(3+c*Math.exp(-x)).toFixed(2);}
   let picture='<defs><clipPath id="forced-clip"><rect x="30" y="25" width="360" height="390"/></clipPath></defs><g clip-path="url(#forced-clip)"><path d="M30 '+py(3)+'H390" stroke="#777" stroke-dasharray="6 5"/><path d="'+d+'" stroke="black" stroke-width="3" fill="none"/></g><path d="M30 360H390 M90 415V25" stroke="black" fill="none"/>';
   for(let x=-1;x<=6;x++)if(x!==0)picture+='<path d="M'+px(x)+' 356v8" stroke="black"/><text x="'+px(x)+'" y="382" font-size="15" text-anchor="middle" fill="black">'+fmt(x)+'</text>';
   for(let y=-1;y<=7;y++)if(y!==0)picture+='<path d="M86 '+py(y)+'h8" stroke="black"/><text x="77" y="'+(py(y)+5)+'" font-size="15" text-anchor="end" fill="black">'+fmt(y)+'</text>';
   picture+='<text x="74" y="382" font-size="15" fill="black">0</text><text x="397" y="354" fill="black">x</text><text x="101" y="28" fill="black">y</text><circle cx="90" cy="'+py(start)+'" r="5" fill="#175d50"/>';
   graph.innerHTML=picture;
   graph.setAttribute('aria-label','Lausn y′+y=3 með upphafsgildi '+fmt(start)+'. Jafnvægislínan er y=3.');
   document.getElementById('forced-value').textContent=fmt(start);
   document.getElementById('forced-equation').innerHTML='y = 3'+(c===0?'':(c<0?' − ':' + ')+fmt(Math.abs(c))+'e<sup>−x</sup>')+'.';
   document.getElementById('forced-status').textContent=start===3?'Lausnin er föst: y = 3.':start<3?'Lausnin hækkar og nálgast 3 neðan frá þegar x vex.':'Lausnin lækkar og nálgast 3 ofan frá þegar x vex.';
  }
  slider.addEventListener('input',draw);draw();
 }
 const cards=document.querySelector('[data-separable-cards]');
 if(cards){
  const data=[
   ['y′ = xy',true,'Hægri hliðin er margfeldi x og y. Fyrir y≠0 má skrifa y′/y=x. Núllfallið þarf líka að athuga.'],
   ['y′ = x + y',false,'Hægri hliðin er summa sem skiptist ekki í þátt af x sinnum þátt af y. Þetta er hliðruð línuleg jafna.'],
   ['(1 + y²)y′ = x',true,'Þetta er þegar á forminu g(y)y′=f(x), með g(y)=1+y² og f(x)=x.'],
   ['y′ = x(y − 2)',true,'Fyrir y≠2 má skrifa y′/(y−2)=x. Fastafallið y=2 er líka lausn.']
  ];
  data.forEach(([equation,correct,explanation],i)=>{
   const card=document.createElement('div');card.style.cssText='margin:24px 0;padding:16px 0;border-top:1px solid var(--line)';
   const heading=document.createElement('h3');heading.textContent=equation;
   const options=document.createElement('div');options.className='activity-options';
   const feedback=document.createElement('p');feedback.setAttribute('role','status');
   [true,false].forEach(value=>{
    const button=document.createElement('button');button.type='button';button.textContent=value?'Já, aðskiljanleg':'Nei, ekki aðskiljanleg';button.setAttribute('aria-pressed','false');
    button.addEventListener('click',()=>{
     options.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
     feedback.textContent=(value===correct?'Rétt. ':'Skoðum þetta betur. ')+explanation;
    });options.append(button);
   });card.append(heading,options,feedback);cards.append(card);
  });
 }
})();

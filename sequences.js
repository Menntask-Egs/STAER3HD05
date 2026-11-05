(() => {
 const fmt=n=>new Intl.NumberFormat('en-US',{maximumFractionDigits:6,useGrouping:false}).format(n).replace('.',',');
 const sequence=document.getElementById('sequence-widget');
 if(sequence){
  const count=document.getElementById('sequence-count');let kind='arithmetic';
  function draw(){
   const n=Number(count.value),values=Array.from({length:n},(_,i)=>kind==='arithmetic'?1+i:1.5**i);
   const px=x=>90+40*x,py=y=>385-40*y;
   let picture='<path d="M65 385H365 M90 405V40" stroke="black" fill="none"/>';
   for(let x=1;x<=6;x++)picture+='<path d="M'+px(x)+' 381v8" stroke="black"/><text x="'+px(x)+'" y="410" fill="black" text-anchor="middle" font-size="15">'+x+'</text>';
   for(let y=1;y<=8;y++)picture+='<path d="M86 '+py(y)+'h8" stroke="black"/><text x="77" y="'+(py(y)+5)+'" fill="black" text-anchor="end" font-size="15">'+y+'</text>';
   picture+='<text x="74" y="407" fill="black" font-size="15">0</text><text x="374" y="380" fill="black">n</text><text x="102" y="38" fill="black">aₙ</text>';
   values.forEach((y,i)=>{picture+='<circle cx="'+px(i+1)+'" cy="'+py(y)+'" r="5" fill="black"/>';});
   const graph=document.getElementById('sequence-graph');graph.innerHTML=picture;
   graph.setAttribute('aria-label',(kind==='arithmetic'?'Jafnmunaruna með d=1':'Jafnhlutfallaruna með r=1,5')+'. Liðir: '+values.map(fmt).join(', '));
   document.getElementById('sequence-rule').innerHTML=kind==='arithmetic'?'a<sub>n</sub> = 1 + (n − 1). Mismunurinn er d = 1.':'a<sub>n</sub> = 1,5<sup>n−1</sup>. Hlutfallið er r = 1,5.';
   document.getElementById('sequence-value').textContent=n;
   document.getElementById('sequence-terms').textContent='Fyrstu '+n+' liðirnir: '+values.map(fmt).join('; ')+'.';
  }
  sequence.querySelectorAll('[data-sequence-kind]').forEach(b=>b.addEventListener('click',()=>{
   kind=b.dataset.sequenceKind;sequence.querySelectorAll('[data-sequence-kind]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));draw();
  }));count.addEventListener('input',draw);draw();
 }
 const series=document.getElementById('series-widget');
 if(series){
  const count=document.getElementById('series-count');
  function draw(){
   const n=Number(count.value);let x=20,picture='';
   for(let k=1;k<=n;k++){
    const width=580/2**k;
    picture+='<rect x="'+x+'" y="30" width="'+width+'" height="100" fill="'+(k%2?'#d8d8d8':'#ededed')+'" stroke="black" stroke-width="1"/>';
    if(width>=55)picture+='<text x="'+(x+width/2)+'" y="86" fill="black" font-size="18" text-anchor="middle">1/'+2**k+'</text>';
    x+=width;
   }
   picture+='<rect x="20" y="30" width="580" height="100" fill="none" stroke="black" stroke-width="2"/>';
   const graph=document.getElementById('series-graph');graph.innerHTML=picture;
   graph.setAttribute('aria-label',n+' liðir lagðir saman. Skyggt flatarmál er '+fmt(1-2**(-n))+' af heildarflatarmálinu 1.');
   document.getElementById('series-value').textContent=n;
   document.getElementById('series-equation').innerHTML=n===0?'Engir liðir hafa verið lagðir saman. Allt flatarmálið 1 er óskyggt.':'S<sub>'+n+'</sub> = '+(2**n-1)+'/'+2**n+' = '+fmt(1-2**(-n))+'. Óskyggt flatarmál er 1/'+2**n+'.';
  }
  count.addEventListener('input',draw);draw();
 }
 const induction=document.getElementById('induction-practice');
 if(induction){
  const messages=['Rétt. Sýna þarf að forsendan P(k) leiði til P(k+1) fyrir almennt k≥1. Ásamt grunnskrefinu nær það til allra n≥1.','Þetta er niðurstaðan sem á að leiða af P(k). Ekki má gera ráð fyrir henni án rökstuðnings.','Þetta staðfestir aðeins tvö gildi í viðbót. Þrepunarskrefið þarf að tengja almennt skref k við k+1.'];
  induction.querySelectorAll('[data-induction-choice]').forEach(b=>b.addEventListener('click',()=>{
   induction.querySelectorAll('[data-induction-choice]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
   document.getElementById('induction-feedback').textContent=messages[Number(b.dataset.inductionChoice)];
  }));
 }
})();

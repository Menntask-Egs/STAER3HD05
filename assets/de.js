(() => {
 const format = n => String(n).replace('.', ',');
 document.querySelectorAll('.de-family').forEach(widget => {
  const slider = widget.querySelector('[data-de-slider]');
  const svg = widget.querySelector('[data-de-graph]');
  const initial = widget.dataset.initial === 'true';
  const px=x=>220+40*x, py=y=>350-40*y;
  const curve=c=>{let d='';for(let i=0;i<=160;i++){const x=-3+i*6/160;d+=(i?'L':'M')+px(x).toFixed(2)+','+py(x*x+c).toFixed(2)}return d;};
  const id = 'clip-de-'+slider.id;
  function draw(){
   const c=Number(slider.value);
   let drawing=`<defs><clipPath id="${id}"><rect x="35" y="20" width="370" height="475"/></clipPath></defs><g clip-path="url(#${id})">`;
   [-2,0,2,3].forEach(k=>{if(k!==c)drawing+=`<path d="${curve(k)}" stroke="#bbb" stroke-width="1.4" fill="none"/>`;});
   drawing+=`<path d="${curve(c)}" stroke="black" stroke-width="3" fill="none"/></g><path d="M35 350H405 M220 495V20" stroke="black" fill="none"/>`;
   for(let x=-4;x<=4;x++)if(x!==0)drawing+=`<path d="M${px(x)} 346v8" stroke="black"/><text x="${px(x)}" y="374" text-anchor="middle" font-size="15" fill="black">${x<0?'−'+(-x):x}</text>`;
   for(let y=-3;y<=8;y++)if(y!==0)drawing+=`<path d="M216 ${py(y)}h8" stroke="black"/><text x="206" y="${py(y)+5}" text-anchor="end" font-size="15" fill="black">${y<0?'−'+(-y):y}</text>`;
   drawing+='<text x="204" y="373" font-size="15" fill="black">0</text><text x="412" y="344" fill="black">x</text><text x="231" y="25" fill="black">y</text>';
   if(initial)drawing+='<circle cx="260" cy="190" r="5" fill="#175d50"/><text x="274" y="182" fill="black" font-size="16">(1, 4)</text>';
   svg.innerHTML=drawing;
   svg.setAttribute('aria-label',`Graf y=x² ${c<0?'mínus':'plús'} ${Math.abs(c)}${initial?', með punktinum (1,4)':''}`);
   widget.querySelector('[data-de-value]').textContent=format(c);
   widget.querySelector('[data-de-equation]').textContent='y = x²'+(c===0?'':c<0?' − '+format(-c):' + '+format(c))+'.';
   widget.querySelector('[data-de-status]').textContent=initial?(c===3?'Ferillinn fer í gegnum (1,4). Hann uppfyllir bæði y′=2x og y(1)=4.':'Við x = 1 er y = '+format(1+c)+'. Upphafsskilyrðið krefst y = 4.'):'Afleiðan er y′ = 2x fyrir öll gildi á C.';
  }
  slider.addEventListener('input',draw);draw();
 });
 const messages=['Já. Afleiða e²ˣ er 2e²ˣ, sem er 2y. Jafnan er uppfyllt fyrir öll x.','Afleiðan er 2, en 2y er 4x. Þær stærðir eru ekki jafnar á heilu bili.','Afleiðan er 2x, en 2y er 2x². Þær stærðir eru ekki jafnar á heilu bili.'];
 const buttons=[...document.querySelectorAll('[data-de-choice]')];
 buttons.forEach(button=>button.addEventListener('click',()=>{
  buttons.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  document.getElementById('de-feedback').textContent=messages[Number(button.dataset.deChoice)];
 }));
})();

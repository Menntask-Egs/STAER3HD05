/* Shared review additions: no external libraries or saved student data. */
(() => {
  const lab = document.getElementById('area-lab');
  if (lab) {
    const slider = lab.querySelector('#area-slice');
    const format = value => new Intl.NumberFormat('en-US', {useGrouping:false,maximumFractionDigits:4}).format(value).replace('.',',');
    const px = x => 55 + 80*x;
    const py = y => 370 - 80*y;
    const path = fn => Array.from({length:101},(_,i) => `${i?'L':'M'}${px(i/50)},${py(fn(i/50))}`).join(' ');
    const axes = '<path d="M30 370H260 M55 395V20" fill="none" stroke="black"/>'+
      '<g fill="black" font-size="16"><text x="37" y="393">0</text><text x="129" y="393">1</text><text x="209" y="393">2</text><text x="266" y="365">x</text><text x="64" y="23">y</text>'+[1,2,3,4].map(y=>`<text x="32" y="${py(y)+5}">${y}</text>`).join('')+'</g>';
    function draw() {
      const x = Number(slider.value), f=2*x, g=x*x;
      lab.querySelector('#area-x').textContent = format(x);
      for (const kind of ['upper','lower','region']) {
        const svg=lab.querySelector(`[data-area="${kind}"]`);
        let shape='';
        if(kind==='region') {
          const points=[...Array.from({length:101},(_,i)=>`${px(i/50)},${py(2*i/50)}`),...Array.from({length:101},(_,i)=>{const q=2-i/50;return `${px(q)},${py(q*q)}`;})].join(' ');
          shape=`<polygon points="${points}" fill="#dedede"/>`;
        }
        const curveF=`<path d="${path(q=>2*q)}" fill="none" stroke="black" stroke-width="2.5"/>`;
        const curveG=`<path d="${path(q=>q*q)}" fill="none" stroke="black" stroke-width="2.5"${kind==='region'?' stroke-dasharray="6 4"':''}/>`;
        const top=kind==='lower'?g:f, bottom=kind==='region'?g:0;
        svg.innerHTML=shape+axes+(kind!=='lower'?curveF:'')+(kind!=='upper'?curveG:'')+
          `<path d="M${px(x)} ${py(bottom)}V${py(top)}" stroke="#175a4d" stroke-width="5"/><circle cx="${px(x)}" cy="${py(top)}" r="4" fill="#175a4d"/>`;
      }
      lab.querySelector('#area-readout').textContent = `Við x = ${format(x)} er f(x) = ${format(f)} og g(x) = ${format(g)}. Hæð sneiðarinnar: ${format(f)} − ${format(g)} = ${format(f-g)}.`;
    }
    slider.addEventListener('input',draw);draw();
  }
  const host=document.getElementById('method-practice');
  if(host) {
    const options=['Einföldun og grunnreglur','Innsetning','Hlutheildun','Stofnbrot'];
    const cards=[
      [String.raw`\int 2x\cos(x^2)\,dx`,1,String.raw`Innri stæðan er \(x^2\) og afleiða hennar \(2x\). Innsetning með \(u=x^2\) gefur grunnheildið \(\int\cos u\,du\).`],
      [String.raw`\int xe^x\,dx`,2,'Þátturinn x einfaldast við diffrun og eˣ er auðvelt að heilda. Hlutheildun gefur nýtt heildi sem er grunnheildi.'],
      [String.raw`\int\frac{1}{x^2-1}\,dx`,3,'Nefnarinn þáttast í (x−1)(x+1). Liðun í tvö stofnbrot gefur brot með línulegum nefnurum.'],
      [String.raw`\int\frac{x^2+2x}{x}\,dx`,0,'Fyrir x≠0 einfaldast brotið í x+2. Þá nægja grunnreglurnar. Skilyrðið x≠0 heldur sér.']
    ];
    cards.forEach((card,k)=>{
      const box=document.createElement('div');box.className='activity method-card';
      const h=document.createElement('h3');h.textContent=`Heildi ${k+1}`;
      const formula=document.createElement('div');formula.className='method-integral';formula.textContent=String.raw`\[`+card[0]+String.raw`\]`;
      const choices=document.createElement('div');choices.className='activity-options';choices.setAttribute('role','group');choices.setAttribute('aria-label',`Aðferð fyrir heildi ${k+1}`);
      const feedback=document.createElement('div');feedback.className='activity-feedback';feedback.setAttribute('role','status');feedback.setAttribute('aria-live','polite');
      const reset=document.createElement('button');reset.type='button';reset.className='method-reset';reset.textContent='Prófa aftur';reset.hidden=true;
      const buttons=options.map((label,i)=>{
        const button=document.createElement('button');button.type='button';button.textContent=label;button.setAttribute('aria-pressed','false');
        button.addEventListener('click',()=>{
          buttons.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
          if(window.MathJax?.typesetClear) window.MathJax.typesetClear([feedback]);
          feedback.textContent=i===card[1]?'Rétt. '+card[2]:'Þessi aðferð er ekki heppilegasta næsta skrefið hér. Skoðaðu byggingu heildisins aftur og prófaðu annan valkost.';
          if(window.MathJax?.startup?.promise) window.MathJax.startup.promise.then(()=>window.MathJax.typesetPromise([feedback]));
          reset.hidden=false;
        });choices.append(button);return button;
      });
      reset.addEventListener('click',()=>{buttons.forEach(b=>b.setAttribute('aria-pressed','false'));feedback.textContent='';reset.hidden=true;buttons[0].focus();});
      box.append(h,formula,choices,feedback,reset);host.append(box);
    });
    if(window.MathJax?.startup?.promise) window.MathJax.startup.promise.then(()=>window.MathJax.typesetPromise([host]));
  }
})();

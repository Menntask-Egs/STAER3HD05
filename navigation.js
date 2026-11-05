(() => {
 const nav=document.getElementById('book-navigation');
 const dialog=document.getElementById('book-drawer');
 const opener=document.getElementById('book-menu-toggle');
 if(!nav||!dialog||!opener)return;
 const content=dialog.querySelector('.drawer-content'),closer=document.getElementById('book-menu-close');
 const home=document.createComment('Desktop navigation');nav.before(home);
 const compact=window.matchMedia('(max-width:900px)');
 function close(){if(dialog.open)dialog.close();}
 function sync(){
  close();
  if(compact.matches)content.append(nav);else home.after(nav);
  opener.setAttribute('aria-expanded','false');
 }
 opener.addEventListener('click',()=>{
  if(!compact.matches)return;
  dialog.showModal();document.body.classList.add('book-menu-open');opener.setAttribute('aria-expanded','true');
  const active=nav.querySelector('.current-unit');if(active)active.scrollIntoView({block:'nearest'});
 });
 closer.addEventListener('click',close);
 dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)close();}});
 dialog.addEventListener('close',()=>{document.body.classList.remove('book-menu-open');opener.setAttribute('aria-expanded','false');});
 nav.addEventListener('click',event=>{if(event.target.closest('a')&&compact.matches)close();});
 window.addEventListener('hashchange',close);compact.addEventListener('change',sync);sync();
})();

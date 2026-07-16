// Shared behaviors extracted from index.html
// Nav scroll state
const nav = document.getElementById('mainNav');
window.addEventListener('scroll', () => {
  if(nav) nav.classList.toggle('scrolled', window.scrollY > 20);
}, { passive:true });

// Scroll progress -> bearing rail + mobile top bar
const bearingFill = document.getElementById('bearingFill');

// Initialize hero-dot CSS variables from data attributes and other small in-DOM migrations
document.addEventListener('DOMContentLoaded', ()=>{
  document.querySelectorAll('.hero-dot').forEach(el => {
    const t = el.dataset.top;
    const l = el.dataset.left;
    const d = el.dataset.delay;
    if(t) el.style.setProperty('--top', t);
    if(l) el.style.setProperty('--left', l);
    if(d) el.style.setProperty('--delay', d);
  });
});
const bearingNode = document.getElementById('bearingNode');
const bearingDeg = document.getElementById('bearingDeg');
const topFill = document.getElementById('topProgressFill');

function updateProgress(){
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const pct = docHeight > 0 ? Math.min(100, Math.max(0, (scrollTop / docHeight) * 100)) : 0;
  if(bearingFill) bearingFill.style.height = pct + '%';
  if(bearingNode) bearingNode.style.top = pct + '%';
  if(topFill) topFill.style.width = pct + '%';
  if(bearingDeg){
    const deg = Math.round((pct / 100) * 360);
    bearingDeg.textContent = 'N ' + String(deg).padStart(3,'0') + '°';
  }
}
window.addEventListener('scroll', updateProgress, { passive:true });
updateProgress();

// Reveal on scroll
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('in-view');
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
revealEls.forEach(el => io.observe(el));

// Smooth internal nav links
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', function(e){

  // Dropdown hover accessibility & small delay handling (desktop)
  function setupDropdowns(){
    if(window.matchMedia('(hover: hover) and (pointer: fine)').matches){
      document.querySelectorAll('.nav-item.has-dropdown').forEach(item => {
        let timeout;
        const dd = item.querySelector('.dropdown');

        const open = () => {
          clearTimeout(timeout);
          item.classList.add('open');
          if(dd) dd.setAttribute('aria-hidden','false');
        };
        const close = () => {
          timeout = setTimeout(()=>{ item.classList.remove('open'); if(dd) dd.setAttribute('aria-hidden','true'); }, 160);
        };

        // Keep dropdown open when entering either the trigger (item) or the dropdown itself
        item.addEventListener('mouseenter', open);
        item.addEventListener('mouseleave', close);
        if(dd){
          dd.addEventListener('mouseenter', open);
          dd.addEventListener('mouseleave', close);
        }
      });
    }
  }
  setupDropdowns();
  window.addEventListener('resize', setupDropdowns);
    const id = this.getAttribute('href');
    if(id.length > 1){
      const target = document.querySelector(id);
      if(target){
        e.preventDefault();
        const y = target.getBoundingClientRect().top + window.scrollY - 84;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  });
});

// Mobile menu toggle
const navMenuBtn = document.getElementById('navMenuBtn');
const navMobile = document.getElementById('navMobile');
if(navMenuBtn && navMobile){
  navMenuBtn.addEventListener('click', ()=>{
    const open = navMenuBtn.getAttribute('aria-expanded') === 'true';
    navMenuBtn.setAttribute('aria-expanded', String(!open));
    navMobile.setAttribute('aria-hidden', String(open));
  });
  window.addEventListener('resize', ()=>{
    if(window.innerWidth > 860){ navMenuBtn.setAttribute('aria-expanded','false'); navMobile.setAttribute('aria-hidden','true'); }
  });
  document.addEventListener('click', (e)=>{
    if(!navMobile.contains(e.target) && !navMenuBtn.contains(e.target)){
      navMenuBtn.setAttribute('aria-expanded','false'); navMobile.setAttribute('aria-hidden','true');
    }
  });
}

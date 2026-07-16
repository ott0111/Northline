from pathlib import Path
import re

nav = '''<nav class="nav" id="mainNav">
  <div class="logo"><span class="logo-mark"></span>NORTHLINE</div>
  <div class="nav-links">
    <div class="nav-item"><a href="index.html">Home</a></div>
    <div class="nav-item has-dropdown">
      <a href="about.html" class="nav-link">Company ▾</a>
      <div class="dropdown" aria-hidden="true">
        <a href="about.html">About</a>
        <a href="team.html">Team</a>
        <a href="careers.html">Careers</a>
        <a href="press.html">Press</a>
        <a href="contact.html">Contact</a>
      </div>
    </div>
    <div class="nav-item has-dropdown">
      <a href="agency.html" class="nav-link">Creators ▾</a>
      <div class="dropdown" aria-hidden="true">
        <a href="agency.html">Creator Agency</a>
        <a href="become-a-creator.html">Become a Creator</a>
        <a href="programs.html">Creator Programs</a>
      </div>
    </div>
    <div class="nav-item has-dropdown">
      <a href="partnerships.html" class="nav-link">Business ▾</a>
      <div class="dropdown" aria-hidden="true">
        <a href="partnerships.html">Partnerships</a>
        <a href="ventures.html">Ventures</a>
        <a href="software.html">Software</a>
        <a href="apparel.html">Apparel</a>
      </div>
    </div>
    <div class="nav-item has-dropdown">
      <a href="community.html" class="nav-link">Community ▾</a>
      <div class="dropdown" aria-hidden="true">
        <a href="community.html">Community</a>
        <a href="events.html">Events</a>
      </div>
    </div>
  </div>
  <div class="nav-cta">
    <a href="become-a-creator.html" class="btn btn-ghost btn-sm">Become a Creator</a>
    <a href="contact.html" class="btn btn-primary btn-sm">Join Northline</a>
  </div>
  <button class="nav-menu-btn" id="navMenuBtn" aria-label="Open menu" aria-expanded="false">☰</button>
  <div class="nav-mobile" id="navMobile" aria-hidden="true">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="team.html">Team</a>
    <a href="careers.html">Careers</a>
    <a href="press.html">Press</a>
    <a href="agency.html">Creator Agency</a>
    <a href="become-a-creator.html">Become a Creator</a>
    <a href="programs.html">Creator Programs</a>
    <a href="partnerships.html">Partnerships</a>
    <a href="ventures.html">Ventures</a>
    <a href="software.html">Software</a>
    <a href="apparel.html">Apparel</a>
    <a href="community.html">Community</a>
    <a href="events.html">Events</a>
    <a href="contact.html">Contact</a>
  </div>
</nav>'''

footer = '''<footer>
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="logo"><span class="logo-mark"></span>NORTHLINE</div>
        <p>A gaming lifestyle brand built for the next generation of competitive gaming creators.</p>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <a href="about.html">About</a>
        <a href="careers.html">Careers</a>
        <a href="press.html">Press</a>
      </div>
      <div class="footer-col">
        <h5>Platform</h5>
        <a href="#what-we-do">Agency</a>
        <a href="#community">Community</a>
        <a href="#what-we-do">Software</a>
      </div>
      <div class="footer-col">
        <h5>Legal</h5>
        <a href="privacy.html">Privacy</a>
        <a href="terms.html">Terms</a>
      </div>
      <div class="footer-col footer-newsletter">
        <h5>Stay Ahead</h5>
        <form onsubmit="return false;">
          <input type="email" placeholder="Your email" aria-label="Email address">
          <button type="submit" aria-label="Subscribe">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </button>
        </form>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Northline. All rights reserved.</p>
      <div class="footer-social">
        <a href="https://x.com" aria-label="X / Twitter">X</a>
        <a href="https://discord.com" aria-label="Discord">DC</a>
        <a href="https://instagram.com" aria-label="Instagram">IG</a>
        <a href="https://youtube.com" aria-label="YouTube">YT</a>
      </div>
    </div>
  </div>
</footer>'''

hero_field = '''  <div class="hero-field" aria-hidden="true">
    <span class="hero-dot" style="top:22%; left:12%; animation-delay:0s;"></span>
    <span class="hero-dot" style="top:65%; left:8%; animation-delay:1.2s;"></span>
    <span class="hero-dot" style="top:30%; left:88%; animation-delay:2.1s;"></span>
    <span class="hero-dot" style="top:75%; left:80%; animation-delay:0.6s;"></span>
    <span class="hero-dot" style="top:15%; left:60%; animation-delay:3s;"></span>
  </div>'''

nav_pattern = re.compile(r'<nav class="nav"[\s\S]*?</nav>', re.IGNORECASE)
footer_pattern = re.compile(r'<footer[\s\S]*?</footer>', re.IGNORECASE)
hero_pattern = re.compile(r'<(?:header|section) class="hero">[\s\S]*?</(?:header|section)>', re.IGNORECASE)

for path in sorted(Path('.').glob('*.html')):
    if path.name == 'index.html':
        continue
    content = path.read_text(encoding='utf-8')
    content = nav_pattern.sub(nav, content, count=1)
    content = footer_pattern.sub(footer, content, count=1)
    content = re.sub(r'<div class="site-shell">\s*', '', content, count=1)
    content = re.sub(r'<header class="site-header">\s*', '', content, count=1)
    content = re.sub(r'</header>\s*(?=<main>)', '', content, count=1)
    content = re.sub(r'<div class="mobile-nav">[\s\S]*?</div>\s*(?=<\/header>)', '', content, count=1)
    content = re.sub(r'</footer>\s*</div>\s*(?=<script|</body>)', '</footer>\n', content, count=1)
    match = hero_pattern.search(content)
    if match:
        hero_block = match.group(0)
        eyebrow_match = re.search(r'<(?:div|span)[^>]*class="(?:hero-eyebrow|eyebrow)"[^>]*>(.*?)</(?:div|span)>', hero_block, re.IGNORECASE | re.DOTALL)
        eyebrow = eyebrow_match.group(1).strip() if eyebrow_match else ''
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', hero_block, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else ''
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', hero_block, re.IGNORECASE | re.DOTALL)
        sub = paragraphs[0].strip() if paragraphs else ''
        anchors = re.findall(r'<a\b[^>]*>.*?</a>', hero_block, re.IGNORECASE | re.DOTALL)
        ctas = [a.strip() for a in anchors[:2]]
        if not ctas:
            ctas = ['<a href="contact.html" class="btn btn-primary">Contact</a>']
        hero_ctas = '      <div class="hero-ctas">\n        ' + '\n        '.join(ctas) + '\n      </div>'
        hero_scroll = '      <div class="hero-scroll"><span class="hero-scroll-line"></span>Scroll</div>'
        hero_content = f'''    <div class="wrap hero-content">\n      <div class="eyebrow">{eyebrow}</div>\n      <h1>{title}</h1>\n      <div class="hero-horizon"></div>\n      <p class="sub">{sub}</p>\n{hero_ctas}\n{hero_scroll}\n    </div>'''
        canonical_hero = '<header class="hero">\n' + hero_field + '\n' + hero_content + '\n  </header>'
        content = content[:match.start()] + canonical_hero + content[match.end():]
    path.write_text(content, encoding='utf-8')
    print(f'Updated: {path.name}')

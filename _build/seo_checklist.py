import re,os,json,html,glob,collections
pages=sorted(f for f in glob.glob('*.html'))
skip_index={'404.html','thanks.html','sign.html','signed.html'}
sm=open('sitemap.xml').read(); locs=set(re.findall(r'<loc>https://www\.figperformance\.com(/[^<]*)</loc>',sm))
titles=collections.defaultdict(list); descs=collections.defaultdict(list)
inlinks=collections.Counter(); issues=collections.defaultdict(list)
files=set(pages)
def exists(path):
    p=path.split('#')[0].split('?')[0]
    if p in('','/'): return True
    p=p.lstrip('/')
    return os.path.exists(p) or os.path.exists(p+'.html') or os.path.exists(os.path.join(p,'index.html'))
vj=json.load(open('vercel.json')); redirects={r['source'] for r in vj.get('redirects',[])}|{r['source'] for r in vj.get('rewrites',[])}
for f in pages:
    s=open(f).read(); slug='/' if f=='index.html' else '/'+f[:-5]
    noindex='noindex' in (re.search(r'<meta name="robots"[^>]*>',s) or [''])[0] if re.search(r'<meta name="robots"[^>]*>',s) else False
    t=re.search(r'<title>(.*?)</title>',s,re.S); t=html.unescape(t.group(1).strip()) if t else ''
    d=re.search(r'<meta name="description" content="([^"]*)"',s); d=html.unescape(d.group(1)) if d else ''
    can=re.search(r'<link rel="canonical" href="([^"]*)"',s)
    if not noindex and f not in skip_index:
        titles[t].append(f); descs[d].append(f)
        if not can: issues['canonical missing'].append(f)
        elif can.group(1).rstrip('/')!=('https://www.figperformance.com'+slug).rstrip('/'): issues['canonical mismatch'].append(f+' -> '+can.group(1))
        if not t: issues['title missing'].append(f)
        elif len(t)>65: issues['title >65 chars'].append(f'{f} ({len(t)})')
        if not d: issues['description missing'].append(f)
        elif len(d)>165: issues['description >165'].append(f'{f} ({len(d)})')
        elif len(d)<70: issues['description <70'].append(f'{f} ({len(d)})')
        if 'application/ld+json' not in s: issues['schema missing'].append(f)
        if 'og:image' not in s: issues['og image missing'].append(f)
        if slug not in locs and slug+'/' not in locs: issues['not in sitemap'].append(f)
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(m.group(1))
        except Exception as e: issues['schema invalid'].append(f)
    if 'name="viewport"' not in s: issues['viewport missing'].append(f)
    h1=re.findall(r'<h1\b',s)
    if len(h1)!=1: issues['h1 count != 1'].append(f'{f} ({len(h1)})')
    body=re.sub(r'<(script|style)\b.*?</\1>','',s,flags=re.S)
    levels=[int(x) for x in re.findall(r'<h([1-6])\b',body)]
    for a,b in zip(levels,levels[1:]):
        if b>a+1: issues['heading skips a level'].append(f'{f} (h{a}->h{b})'); break
    for m in re.finditer(r'<img\b[^>]*>',s):
        tag=m.group(0)
        if not re.search(r'\balt="',tag): issues['img without alt'].append(f)
        if not re.search(r'\bwidth=',tag): issues['img without width/height'].append(f)
    for m in re.finditer(r'(?:href|src)="([^"]+)"',s):
        u=m.group(1)
        if u.startswith('http://'): issues['http link'].append(f+' '+u)
        if u.startswith(('http','mailto:','tel:','sms:','#','data:')): continue
        if u.startswith('/'):
            p=u.split('#')[0].split('?')[0]
            if not exists(u) and p not in redirects: issues['broken internal link'].append(f+' -> '+u)
            if m.group(0).startswith('href') and not p.startswith('/assets'): inlinks[p.rstrip('/') or '/']+=1 if ('/'+f[:-5])!=p else 0
    if f!='index.html' and not re.fullmatch(r'[a-z0-9-]+\.html',f): issues['slug not lowercase-hyphen'].append(f)
for t,fs in titles.items():
    if len(fs)>1: issues['duplicate title'].append(', '.join(fs))
for d,fs in descs.items():
    if len(fs)>1 and d: issues['duplicate description'].append(', '.join(fs))
for l in locs:
    if not exists(l): issues['sitemap url missing file'].append(l)
for f in pages:
    slug='/' if f=='index.html' else '/'+f[:-5]
    if f not in skip_index and inlinks[slug.rstrip('/') or '/']<2: issues['few internal links pointing in (<2)'].append(f'{f} ({inlinks[slug]})')
big=[(os.path.getsize(p)//1024,p) for p in glob.glob('assets/**/*',recursive=True) if p.lower().endswith(('.jpg','.jpeg','.png','.webp','.gif')) and os.path.getsize(p)>300*1024]
print('pages',len(pages),'sitemap urls',len(locs))
for k,v in sorted(issues.items()): print(f'\n## {k}: {len(v)}'); [print('  ',x) for x in v[:12]]
print('\n## images over 300KB:',len(big)); [print('  ',kb,'KB',p) for kb,p in sorted(big,reverse=True)[:12]]
print('\nrobots.txt:',open('robots.txt').read()[:400] if os.path.exists('robots.txt') else 'MISSING')

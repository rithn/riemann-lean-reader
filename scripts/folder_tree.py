import sys
import csv, collections, re, json
csv.field_size_limit(10**9)
T=1000
rows=list(csv.DictReader(open(sys.argv[1]),delimiter='\t'))
cnt=collections.Counter(); lines=collections.Counter(); kids=collections.defaultdict(set); direct=collections.defaultdict(list)
for r in rows:
    p=r['file'].split('/'); L=int(r['lines'])
    direct['/'.join(p[:-1])].append(p[-1][:-5])
    for i in range(len(p)):
        n='/'.join(p[:i]); cnt[n]+=1; lines[n]+=L
        if i<len(p)-1: kids[n].add('/'.join(p[:i+1]))
STOP=set('of eq le lt iff statement proof mem ne zero one two three exists forall is and the on in to at for from with map add mul sub alt aux apply comp def lemma holds all self not ge gt pos neg left right succ sum prod set fun hom iso equiv range card finite bound bounds general local global basic step case main first second form data pair type core part'.split())
def toks(name):
    return {t.lower() for t in re.findall(r'[A-Z][a-z]+|[a-z]+',name) if len(t)>=4 and t.lower() not in STOP}
def clusters(names,maxg=14):
    tk=[toks(n) for n in names]; left=set(range(len(names))); out=[]
    while left and len(out)<maxg:
        c=collections.Counter(t for i in left for t in tk[i])
        if not c: break
        t,k=c.most_common(1)[0]
        if k<max(20,len(names)*0.01): break
        mem=[i for i in left if t in tk[i]]
        co=collections.Counter(x for i in mem for x in tk[i] if x!=t).most_common(4)
        out.append({'kw':t,'n':k,'also':[x for x,_ in co],'eg':[names[i] for i in mem[:3]]})
        left-=set(mem)
    return out,len(left)
out=[]
def go(n,depth):
    if cnt[n]<=T and n: out.append({'path':n,'files':cnt[n],'lines':lines[n],'kind':'leaf','subs':len(kids[n])}); return
    if not kids[n]:
        cl,rest=clusters(direct[n]); out.append({'path':n,'files':cnt[n],'lines':lines[n],'kind':'flat','clusters':cl,'rest':rest}); return
    if n: out.append({'path':n,'files':cnt[n],'lines':lines[n],'kind':'split','subs':len(kids[n])})
    if n and direct[n]:
        d={'path':n+'/(loose files)','files':len(direct[n]),'lines':0,'kind':'loose'}
        if len(direct[n])>T: d['clusters'],d['rest']=clusters(direct[n]); d['kind']='flat'
        out.append(d)
    ks=sorted(kids[n],key=lambda k:-cnt[k]); thr=min(300,max(40,cnt[n]*0.02)) if n else 0
    small=[k for k in ks if cnt[k]<thr]
    if len(small)<=3: small=[]
    for k in ks:
        if k not in small: go(k,depth+1)
    if small: out.append({'path':n+'/(other)','files':sum(cnt[k] for k in small),'lines':sum(lines[k] for k in small),'kind':'other','nf':len(small),'eg':[k.split('/')[-1] for k in small[:6]]})
go('',0)
json.dump(out,open('adapt.json','w'))
print(len(out),collections.Counter(o['kind'] for o in out))
for o in out:
    if o['kind'] in('flat',): print(o['path'],o['files'],'rest',o['rest'],[(c['kw'],c['n']) for c in o['clusters']])
for o in out:
    if o['kind']!='flat': print(o['kind'][0],o['files'],o['path'], o.get('eg',''))

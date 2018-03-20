import collections
import numpy as np
from nltk.stem import SnowballStemmer

fold = "/home/masteradamo/academy/models/Wikipedia/5x5/"

fr = fold + "wordus.txt"
fv = fold + "vectors/"
fd = fold + "dimensions/"

def translater():
    rt = [x.split("::")[0] for x in open(fr,'r').readlines()]
    tr = {rt[n]:str(n) for n in range(len(rt))}
    return tr,rt

def indyer(inds,ext):
    outs = set()
    pt = 0
    while len(outs) < ext:
#        print "LOUT",outs,pt,len(outs)
        pt  += max(1,(ext-len(outs))/len(inds))
        outs.update([x for y in inds for x in y[:pt]])
    return outs

def returner(words,ext):
    print "DOING",words,[type(x) for x in words]
    allvecs = []
    vecs = []
    for word in words:
        vec = collections.defaultdict(float)
        for pair in open(fv+tr[word]+".txt",'r').readlines():
            vec[pair.split("::")[0]] = float(pair.split("::")[1])
            allvecs.append(pair.split("::")[0])
        vecs.append(vec)
    allvecs = set(allvecs)
    svecs = [z[1] for z in sorted([(sum([x[y] for x in vecs]),y) for y in allvecs],reverse=True)[:ext]]
#    print "SVECS",svecs
    jvecs = [z[1] for z in sorted([(sum([x[y] for x in vecs]),y) for y in allvecs if min([w[y] for w in vecs]) > 0],reverse = True)[:ext]]
#    print "JVECS",jvecs
    simps = [[x[y] for y in svecs] for x in vecs]
    joints = [[x[y] for y in jvecs] for x in vecs]
    return simps,joints

tr,rt = translater()
print "TRANSLATERS BUILT"
words = []

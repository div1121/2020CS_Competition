import logging
import json
import sys

from flask import request, jsonify,Response;
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def evaluategmo():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("list")
    for c in inputValue:
        c["geneSequence"] = findmaxstr(c["geneSequence"])
    logging.info("My result :{}".format(data))
    #resp = Response(jsonify(data))
    #resp.headers["Content-Type"] = "application/json"
    return Response(json.dumps(data), mimetype='application/json')

def findmaxstr(s):
    a = 0
    c = 0
    g = 0
    t = 0
    for p in s:
        if p=="A":
            a+=1
        if p=="C":
            c+=1
        if p=="G":
            g+=1
        if p=="T":
            t+=1
    #print(a,c,g,t)
    ans = -sys.maxsize - 1
    te = [0,0,0]
    space = c + g + t
    m = min(a,c,g,t)
    for i in range(m+1):
        n = (c-i)//2
        for j in range(n+1):
            k = ((a-i)-(space-3*i-j)*2)//3
            if k<0:
                k = 0
            temp = i*15+j*25-k*10
            ans = max(ans,temp)
            #print(ans,temp)
            if ans==temp:
                te = [i,j,k]
    strans = ""
    for i in range(te[0]):
        strans += "ACGT"
        a-=1
        c-=1
        g-=1
        t-=1
    while a>0:
        if a >= 2:
            strans += "AA"
            a -= 2
        elif a == 1:
            strans += "A"
            a -= 1
        if te[1]>0:
            strans += "CC"
            c -= 2
            te[1]-=1
        else:
            tpp = max(c,g,t)
            if tpp == 0:
                continue
            if tpp==c:
                strans += "C"
                c-=1
            elif tpp==g:
                strans += "G"
                g-=1
            elif tpp==t:
                strans += "T"
                t-=1
    tpp = max(c,g,t)
    while tpp>0:
        if tpp==c:
            strans += "C"
            c-=1
        elif tpp==g:
            strans += "G"
            g-=1
        elif tpp==t:
            strans += "T"
            t-=1
        tpp = max(c,g,t)
    return strans


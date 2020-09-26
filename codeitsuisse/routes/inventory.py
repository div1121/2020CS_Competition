import logging
import json
import sys
import heapq

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def evaluateinventory():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    realstr = data[0].get("searchItemName")
    itemlist = data[0].get("items")
    print(realstr)
    print(itemlist)
    result = []
    count = 0
    for s in itemlist:
        r = findstr(s,realstr)
        print(r)
        if count < 10:
            result.append(r)
            count+=1
        else:
            result.append(r)
    result.sort()
    print(result)
    ab = []
    for i,c in enumerate(result):
        if i<10:
            ab.append(c[1])
    fp = [{"searchItemName":realstr,"searchResult":ab}]
    logging.info("My result :{}".format(fp))
    return json.dumps(fp)

def findstr(s,realstr):
    n = len(s)
    m = len(realstr)
    dp = [[0] * (n+1) for _ in range (m+1)]
    print(s,realstr,len(dp))
    for i in range(m+1):
        for j in range(n+1):
            #if (i-1>=0 and j-1>=0):
                #print(realstr[i-1].lower(),s[j-1].lower(),(realstr[i-1].lower())==(s[j-1].lower()))
            if (i==0 or j==0):
                #print(i,j,max(i,j))
                dp[i][j] = max(i,j)
            elif (realstr[i-1].lower())==(s[j-1].lower()):
                #print(i,j,i-1,j-1,dp[i-1][j-1])
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
            #print(i,j,dp[i][j],end=" ")
        #print()
    realans = ""
    print("Real ans:" , dp[m][n])
    i = m
    j = n
    while (i>0 and j>0):
        if (realstr[i-1].lower())==(s[j-1].lower()):
            realans = realstr[i-1] + realans
            i-=1
            j-=1
        else:
            t = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
            if t==dp[i-1][j-1]:
                realans = s[j-1] + realans
                i-=1
                j-=1
            elif t==dp[i-1][j]:
                realans = "-" + realstr[i-1] + realans
                i-=1
            else:
                realans = "+" + s[j-1] + realans
                j-=1
    print(i,j)
    while i>0:
        realans = "-" + realstr[i-1] + realans
        i-=1

    print(dp[m][n],realans)
    return (dp[m][n],realans)


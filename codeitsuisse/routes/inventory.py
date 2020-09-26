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
        if count < 10:
            result.append(r)
            count+=1
        #else:
            #heapq.heapify(result)
            #heapq.heappush(r)
            #heapq.heappop(result)
    print(result)
    ab = []
    for c in result:
        ab.append(c[1])
    fp = [{"searchItemName":realstr,"items":ab}]
    logging.info("My result :{}".format(fp))
    return json.dumps(fp)

def findstr(s,realstr):
    n = len(s)
    m = len(realstr)
    dp = [[0] * (n+1)] * (m+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if realstr[i-1]==s[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else: 
                dp[i][j] = min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1])) + 1
    realans = ""
    i = m
    j = n
    while (i>0 and j>0):
        if realstr[i-1]==s[j-1]:
            realans = realstr[i-1] + realans
            i-=1
            j-=1
        else:
            t = min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))
            if t==dp[i-1][j-1]:
                realans = s[j] + realans
            elif t==dp[i-1][j]:
                realans = "-" + realans[i] + realans
            else:
                realans = "+" + s[j] + realans
    print(dp[m][n],realans)
    return (dp[m][n],realans)


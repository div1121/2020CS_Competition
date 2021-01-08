import logging
import json

from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluatecluster():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    count = 0
    m = len(data)
    n = len(data[0])
    for i,c in enumerate(data):
        for j,d in enumerate(c):
            if d=="1":
                spread(data,i,j,m,n)
                count += 1
    result = {"answer":count}
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def spread(data,i,j,m,n):
    if i<0 or i>=m or j<0 or j>=n or data[i][j]=="*" or data[i][j]=="2":
        return
    data[i][j] = "2"
    spread(data,i-1,j,m,n)
    spread(data,i+1,j,m,n)
    spread(data,i,j-1,m,n)
    spread(data,i,j+1,m,n)
    spread(data,i+1,j+1,m,n)
    spread(data,i-1,j+1,m,n)
    spread(data,i+1,j-1,m,n)
    spread(data,i-1,j-1,m,n)


import logging
import json
import operator as op

from flask import request, jsonify;
from functools import reduce
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluatesocial():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    testcase = data["tests"]
    save = {}
    count = 0
    for x in testcase:
        y = testcase[x]
        seat = y["seats"]
        people = y["people"]
        space = y["spaces"]
        n = people + (people - 1) * space
        ans = 0
        if n>seat:
            ans = 0
        elif n==seat:
            ans = 1
        else:
            k = seat - n
            m = people + 1
            ans = ncr(m+k-1,k)
        save[x] = ans
        count+=1
    result = {"answers":save}
    logging.info("My result :{}".format(result))
    return json.dumps(result)


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

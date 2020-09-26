import logging
import json
import sys

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluatesalad():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("number_of_salads")
    rmap = data.get("salad_prices_street_map")
    result = sys.maxsize
    for street in rmap:
        result = min(result,findvalue(n,street))
    if result == sys.maxsize:
        result = 0
    ans = {"result":result}
    logging.info("My result :{}".format(ans))
    return json.dumps(ans)

def findvalue(n,street):
    temp = 0
    count = 0
    ans = sys.maxsize
    for i,s in enumerate(street):
        if s != "X":
            temp += int(s)
            count += 1
            if count==n:
                ans = min(ans,temp)
            elif count>n:
                temp -= int(street[i-n])
                count -= 1
                ans = min(ans, temp)
        else:
            temp = 0
            count = 0
    return ans
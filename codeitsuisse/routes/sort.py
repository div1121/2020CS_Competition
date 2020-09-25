import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def evaluatesort():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    n = 20001
    save = [0] * n
    result = []
    for i in inputValue:
        save[i+10000]+=1
    for i in range(n):
        t = i - 10000
        result += [t] * save[i]
    logging.info("My result :{}".format(result))
    return json.dumps(result)




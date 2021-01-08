import logging
import json

from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def evaluatesecret():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for test_case in data:
        result.append(encrypt(test_case["n"],test_case["text"]))
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def encrypt(n,text):
    preprocess = ""
    for c in text:
        if c.isalnum():
            preprocess += c.upper()
    start = 0
    listofstring = []
    length = len(preprocess) // n
    remain = len(preprocess) % n
    for i in range(n):
        r = length
        if i<remain:
            r += 1
        substr = preprocess[start:start+r]
        listofstring.append(substr)
        start += r
    result = ""
    for i in range(len(preprocess)):
        rnum = i % n
        cnum = i // n
        result += listofstring[rnum][cnum]
    return result

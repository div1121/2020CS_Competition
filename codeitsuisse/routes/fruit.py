import logging
import json
import ast

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluatefruit():
    data = request.get_data()
    #data = json.loads(data)
    #logging.info("data sent for evaluation {}".format(data))
    data = ast.literal_eval(data)
    a = data["maApple"]
    b = data["maWatermelon"]
    c = data["maBanana"]
    ta = 30
    tb = 30
    tc = 30
    print(a)
    print(b)
    print(c)
    result = ta*a + tb*b + tc*c
    logging.info("My result :{}".format(result))
    return jsonify("0")




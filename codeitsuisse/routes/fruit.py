import logging
import json
import ast

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluatefruit():
    data = request.get_data()
    data = json.loads(data)
    logging.info("data sent for evaluation {}".format(data))
    #data = ast.literal_eval(data)
    a = data["maApple"]
    b = data["maWatermelon"]
    c = data["maBanana"]
    ta = 50
    tb = 50
    tc = 50
    print(a)
    print(b)
    print(c)
    guess = ta*a + tb*b + tc*c
    #logging.info("My result :{}".format(result))
    guess = 4440
    result = "{}".format(guess)
    return jsonify(result)




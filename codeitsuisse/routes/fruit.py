import logging
import json
import ast
import random

from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluatefruit():
    data = request.get_data()
    print(data)
    data = json.loads(data.decode())
    print(data)
    #logging.info("data sent for evaluation {}".format(data))
    #data = ast.literal_eval(data)
    count = 0
    guess = 0
    save = [i for i in range(60,101)]
    random.shuffle(save)
    for i in data:
        guess += save[count] * data[i]
        count +=1
    #logging.info("My result :{}".format(result))
    result = "{}".format(guess)
    return jsonify(result)




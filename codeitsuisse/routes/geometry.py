import logging
import json

from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def evaluategemoetry():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    shape = data.get("shapeCoordinates")
    line = data.get("lineCoordinates")
    result = []
    for i,setofpoint in enumerate(shape):
        print(i)
        r = line_intersection([shape[i-1],shape[i]],line)
        print(r)
        if bool(r):
            result.append(r)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def line_intersection(rline1, rline2):
    line1 = [[rline1[0]["x"],rline1[0]["y"]],[rline1[1]["x"],rline1[1]["y"]]]
    line2 = [[rline2[0]["x"],rline2[0]["y"]],[rline2[1]["x"],rline2[1]["y"]]]
    print(line1)
    print(line2)
    #dxx = line2[0][0] - line2[1][0]
    #dyy = line2[0][1] - line2[1][1]
    #line2[0][0] -= 10000 * dxx
    #line2[1][0] += 10000 * dxx
    #line2[0][1] -= 10000 * dyy
    #line2[1][1] += 10000 * dyy
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    print(div)
    if div == 0:
        return {}

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    tx = min(line1[0][0],line1[1][0])
    mx = max(line1[0][0],line1[1][0])
    ty = min(line1[0][1],line1[1][1])
    my = max(line1[0][1],line1[1][1])
    if (tx<=x and x<=mx and ty<=y and y<=my):
        return {"x":x,"y":y}
    else:
        return {}
import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/supermarket', methods=['POST'])
def evaluatesupermarket():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("tests")
    result = {}
    for x in inputValue:
        y = inputValue[x]
        maze = y["maze"]
        start = y["start"]
        end = y["end"]
        ans = breathfirstsearch(maze,start,end)
        result[x] = ans
    result = {"answers":result}
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def breathfirstsearch(maze,start,end):
    start = [start[1], start[0]]
    end = [end[1], end[0]]
    queue = []
    queue.append(start)
    count = 1
    while queue:
        n = len(queue)
        for i in range(n):
            s = queue.pop(0)
            if (s[0]==end[0] and s[1]==end[1]):
                return count
            if (s[0]>=0 and s[0]<len(maze) and s[1]>=0 and s[1]<len(maze[0]) and maze[s[0]][s[1]]==0):
                maze[s[0]][s[1]]=3
                queue.append([s[0]+1,s[1]])
                queue.append([s[0]-1,s[1]])
                queue.append([s[0],s[1]+1])
                queue.append([s[0],s[1]-1])
        count+=1
    return -1


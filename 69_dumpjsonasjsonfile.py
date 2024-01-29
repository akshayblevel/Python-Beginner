import json

point = {
          "x":100,
          "y":100
        }


json.dump(point,open("./point2.json",mode='w'))

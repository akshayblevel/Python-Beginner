import json

path = "point1.json"

point = json.load(open(path, mode='r'))
print(point)

print("x = {}".format(point.get("x")))
print("y = {}".format(point.get("y")))

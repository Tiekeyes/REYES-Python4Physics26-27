import numpy as np

#stores all points
points = {"Inside": [], "Outside": []}

#Point class
class Point:
    def __init__(self, count):
        self.count = count
        self.x = np.random.uniform(-1, 1)
        self.y = np.random.uniform(-1, 1)

#create a random point and determine if it is within a circle
for i in range(100000):
    new_point = Point(i)
    if np.sqrt(new_point.x**2 + new_point.y**2) <= 1:
        points["Inside"].append(new_point)
    else:
        points["Outside"].append(new_point)
    
probability = len(points["Inside"]) / (len(points["Inside"]) + len(points["Outside"]))

print(probability * 4)

    
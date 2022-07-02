import math


class Point(object):
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def ManhattanDistance(point):
        return math.sqrt(((point.x1-point.x2)**2 + (point.y1-point.y2)**2))


print("Distance = ", Point.ManhattanDistance(point=Point(1, 4, 1, 5)))

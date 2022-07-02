import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    @staticmethod  
    def distance(p1, p2):
        return math.sqrt( (p1.x-p2.x)**2 + (p1.y-p2.y)**2 )

    def __str__(self):
        return "x=%d, y=%d"%(self.x, self.y)

p1 = Point(3, 5)
p2 = Point(5, 7)
print(Point.distance(p1, p2))

p1.move_up()
print(p1.x, p1.y)
print(p1)
print(Point.distance(p1, p2))
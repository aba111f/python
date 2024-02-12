import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

point1 = Point(5, 2)
point2 = Point(7, 3)
point1.move(4, 4)
point1.show()
point2.show()
print(point1.dist(point2))
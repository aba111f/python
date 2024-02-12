class Shape:
    def area(self):
       return 0
   
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)

rec = Rectangle(int(input()),int(input()))
rec.area()
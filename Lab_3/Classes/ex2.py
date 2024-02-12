class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    

class Square(Shape):
    def __init__(self, Length):
        Shape.__init__(self)
        self.lenght = Length
    def area(self):
        print(int(self.lenght ** 2))

inputSquare = Square(int(input()))
inputSquare.area()
class string:
    def __init__(self):
        pass
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())

x = string()
x.getString()
x.printString()
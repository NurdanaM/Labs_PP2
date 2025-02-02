class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

s1 = Shape()
print(s1.area())
s2 = Square(5)
print(s2.area())
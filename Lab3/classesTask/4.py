import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print((self.x , self.y))

    def move(self, x1, y2):
        self.x = x1
        self.y = y2
    
    def dist(self, point2):
        return math.sqrt((point2.x - self.x)**2 + (point2.y - self.y)**2)
    
p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()
p2.show()

print(p1.dist(p2))

p1.move(2, 7)
p1.show()
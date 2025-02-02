import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"(x,y) = ({self.x}, {self.y})")
    def move(self,x2,y2):
        self.x += x2
        self.y += y2
    def dist(self, x2,y2):
        d = math.sqrt(pow(x2-self.x, 2)+pow(y2-self.y,2))
        print("The distance:", d)
p = Point(1,2)
p.show()
p.move(1, -2)
p.show()
p.dist(2,1)

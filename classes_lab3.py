class Shape:
    def __init__(self):
        self.area = 0
    def Area(self):
        print("The area of shape:", self.area)
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.l = length
        self.area = self.l*self.l
x1 = Shape()
x2 = Square(3)
x1.Area()
x2.Area()
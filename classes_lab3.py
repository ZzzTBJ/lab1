class Shape:
    def __init__(self):
        self.area = 0
    def Area(self):
        print("The area of shape:", self.area)
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.l = length
        self.w = width
        self.area = self.l*self.w
x1 = Shape()
x2 = Rectangle(4,3)
x1.Area()
x2.Area()
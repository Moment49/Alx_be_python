import math

class Shape:
    def area(self):
        raise NotImplementedError("Area must be overriddent by the child classes")


class Rectangle(Shape):
    def __init__(self, lenght,  width):
        super().__init__()
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius** 2
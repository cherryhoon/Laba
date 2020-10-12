class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height


class Triangle(Shape):
    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Shape):
    def area(self):
        return self.base * self.height


triangle = Triangle(3, 4)
rectangle = Rectangle(3, 4)
print(f"Triangle area: {triangle.area()}\nRectangle area: {rectangle.area()}")
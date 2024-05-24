from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Shape Abstract Class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Circle Class"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Should handle negative radius
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):
    """Rectangle Class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 3. shape_info Function
def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
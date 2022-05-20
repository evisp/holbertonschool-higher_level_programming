#!/usr/bin/python3
""" Class Rectangle defines a rectangle with properties width and height """


class Rectangle:
    """ class initialization """
    def __init__(self, width=0, height=0):
        """
        Initialization of a rectangle object 
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        Raises:
            TypeError: if width or height is not integer
            ValueError: if width or height is smaller than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                rect.append("#")
            if h != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")

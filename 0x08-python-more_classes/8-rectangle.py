#!/usr/bin/python3
""" Class Rectangle defines a rectangle with properties width and height """


class Rectangle:
    """ class initialization """

    # class attribute number_of_instances
    number_of_instances = 0
    #class attribyte print_symbol
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_w, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                rect.append(str(self.print_symbol))
            if h != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

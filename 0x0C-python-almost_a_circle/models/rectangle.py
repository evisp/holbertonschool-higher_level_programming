#!/usr/bin/python3
""" class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherited from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle definition
        Args:
            width (int):
            height (int):
            x (int):
            y (int):
            id :
        """
        super().__init__(id)  # Call super class with id __init__ Base logic
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter definition
        Returns:
            the Rectangle width
        """
        return self.__width

    @property
    def height(self):
        """ height getter definition
        Returns:
            the retrieve height
        """
        return self.__height

    @property
    def x(self):
        """ x getter definition """
        return self.__x

    @property
    def y(self):
        """ y getter definition """
        return self.__y

    @width.setter
    def width(self, width):
        """ width setter
        Raises:
            TypeError: if width is not  integer
            ValueError: if width is less than zero
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ height setter
        Raises:
            TypeError: if height is not  integer
            ValueError: if height is less than zero
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ x setter
        Raises:
            TypeError: if x is not  integer
            ValueError: if x is less than zero
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ y setter
        Raises:
            TypeError: if y is not  integer
            ValueError: if y is less than zero
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area definition"""
        return self.width * self.height

    def display(self):
        """ prints in the stdout the rectangle instance with # """
        for y in range(self.y):
            print()
        for a in range(self.height):
            print(' ' * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """ str representation"""
        return ("[Rectangle] (" + str(self.id) + ") " +
                str(self.__x) + "/" + str(self.__y) + " - " +
                str(self.__width) + "/" + str(self.__height))

    def update(self, *args, **kwargs):
        """ public method update """
        arguments = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            i = 0
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        else:
            for s, g in kwargs.items():
                if hasattr(self, s):
                    setattr(self, s, g)

    def to_dictionary(self):
        """ dict definition """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

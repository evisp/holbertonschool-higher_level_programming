#!/usr/bin/python3
""" Define class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    
    """ Define class Rectangle """

    def __init__(self, width, height):
        """ Initializaing and validating """ 
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ method that computer rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ return string representation of object """
        return f"[Rectangle] {self.__width}/{self.__height}"

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

    

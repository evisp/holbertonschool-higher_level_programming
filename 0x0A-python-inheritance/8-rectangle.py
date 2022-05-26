#!/usr/bin/python3
""" Define class Rectangle """


class Rectangle(BaseGeometry):
    
    """ Define class Rectangle """

    def __init__(self, width, height):
        """ Initializaing and validating """ 
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    

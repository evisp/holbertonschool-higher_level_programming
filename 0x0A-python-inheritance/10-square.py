#!/usr/bin/python3
""" Define class Rectangle """
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    
    """ Define class Square """

    def __init__(self, size):
        """ Initializaing and validating """ 
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ method that computer square area """
        return self.__size * self.__size

#!/usr/bin/python3
""" Define class BaseGeometry """


class BaseGeometry:
    
    """ Define class BaseGeometry """
    
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validate value
        Args:
            name (str): first parameter
            value (int): second parameter to validate
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

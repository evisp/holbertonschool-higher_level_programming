#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """Function computes the sum of two integer arguments

    Float arguments are typecasted into integers

    Raises:
        TypeErorr: if a or b is not integer or not float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    result = int(a) + int(b)

    return result

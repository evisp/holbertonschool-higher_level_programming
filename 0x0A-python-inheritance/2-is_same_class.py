#!/usr/bin/python3
""" Checks if the object is exactly an instance of a class """

def is_same_class(obj, a_class):
    """ check if obj is exactly an instance of a_class
    Args:
        obj: the object
        a_class: the class
    Returns:
        True if obj is exactly instance of a_class
    """
    return type(obj) is a_class

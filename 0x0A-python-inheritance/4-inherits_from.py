#!/usr/bin/python3
""" Checks if the object is an instance of a class that inherited
(directly or indirectly) from the specified class 
"""

def inherits_from(obj, a_class):
    """ check if obj is exactly an instance of a_class
    Args:
        obj: the object
        a_class: the class
    Returns:
        True if obj if the object is an instance of a class 
that inherited (directly or indirectly) from the specified class 
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

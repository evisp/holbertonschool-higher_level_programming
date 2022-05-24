#!/usr/bin/python3
""" Method lookup"""

def lookup(obj):
    """ lookup method
    Returns:
        the list of available attributes and methods of an object
    """
    return dir(obj)

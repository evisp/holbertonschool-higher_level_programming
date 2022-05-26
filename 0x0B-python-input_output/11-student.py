#!/usr/bin/python3
""" class Student """


class Student:
    """ definition """
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method that retrieves a dictionary representation
        of a student instance """
        return self.__dict__
    
    def to_json(self, attrs=None):
        """ public method that retrieves a dictionary representation
        of a student instance """
        if isinstance(attrs, list) and ([isinstance(atr, str)] for atr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    for k, v in json.items():
        setattr(self, k, v)
        """ alternatively
        for names in json:
            self.__dict__[names] = json[names]

        """

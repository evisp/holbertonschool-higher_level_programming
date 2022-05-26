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

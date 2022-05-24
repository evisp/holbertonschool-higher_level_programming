#!/usr/bin/python3
""" MyList class inherits from list """

class MyList(list):
    """ MyList definition """
    def print_sorted(self):
        """ prints a list sorted in ascending order """
        print(sorted(self))

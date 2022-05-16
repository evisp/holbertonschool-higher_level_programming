#!/usr/bin/python3
""" Class Square is defined as an empty class.  """


class Square:
        """ class Square"""
        def __init__(self, size=0):
                """private instance size"""
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >= 0")
                self.__size = size

        @property
        def size(self):
                return self.__size

        @size.setter
        def size(self, value):
                if type(value) is not int:
                        raise TypeError("size must be an integer")
                if value < 0:
                        raise ValueError("size must be >= 0")
                self.__size = value

        @property
        def position(self):
                """Get/set the current position of the square."""
                return (self.__position)
        
        @position.setter
        def position(self, value):
                if type(value) is not tuple or len(value) is not 2 or type(value[0]) is not int or value[0] < 0 or type(value[1]) is not int or value[1] < 0:
                        raise TypeError("position must be a tuple of 2 positive integers")
                else:
                        self.__position = value


        def area(self):
                """ method that computes the area of a square"""
                return self.__size ** 2

        def my_print(self):
                for i in range(self.size):
                     for el in range(self.size):
                             print('#', end="")
                     print("")

                if self.size == 0:
                        print("")

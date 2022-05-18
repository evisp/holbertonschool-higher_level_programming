#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ class initialization """
    def __init__(self, size=0, position=(0, 0)):
        """ Definition with private instance attribute size
        which is asigned with the double underscore before given name
        Args:
            size (int): private instance attribute.
            position (int, int): private instance attribut.
        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is less than zero
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ size definition to retrieve (getter)
        A method used for getting a value is decorated with @property
        Returns:
            the retrieve size
        """
        return self.__size

    @property
    def position(self):
        """ position definition to retrieve (getter)
        A method used for getting a value is decorated with @property
        Returns:
            the retrieve position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """ size definition to setter the data, now size will be equal to value
        A method that function as the setter is decorated with @ .setter
        Args:
            value (int): new integer to set as the size
        Raises:
            TypeError: if `size` is not an integer
            ValueError: if `size` is less than zero
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):

        """ size definition to setter the data, now size will be equal to value
        A method that function as the setter is decorated with @ .setter
        Args:
            value (int): new integer to set as the position
        Raises:
            TypeError: if value for position is not a tuple (two integers)
            or positives  (greater than zero"), in positions [0] and [1]
        """
        if type(value) is not tuple or len(value) is not 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Public instance method
        Returns:
            Square Area. self.size ** 2
        """
        return self.size * self.size

    def my_print(self):
        """ Public instance method that prints in stdout
        the square with the character #
        """
        if self.size is 0:
            print("")
        else:
            for jumps in range(self.position[1]):
                print("")
            for row in range(self.size):
                print(" " * self.position[0], end="")
                for column in range(self.size):
                    print("#", end="")
                print("")

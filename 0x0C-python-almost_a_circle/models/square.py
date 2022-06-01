#!/usr/bin/python3
""" class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def __str__(self):
        """ string representation """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ public method update definition """
        if args:
            arguments = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])  # setting position to atr
        else:
            for s, g in kwargs.items():
                if hasattr(self, s):
                    setattr(self, s, g)

    def to_dictionary(self):
        """ to dictionary representation """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

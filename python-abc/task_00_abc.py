from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class for animals"""

    def __init__(self):
        pass

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound"""
        pass

class Dog(Animal):
    """Dog class"""

    def sound(self):
        """Dog sound"""
        return "Bark"

class Cat(Animal):
        """Cat class"""
    
        def sound(self):
            """Cat sound"""
            return "Meow"


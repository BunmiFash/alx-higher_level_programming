#!/usr/bin/python3


"""Module that creates a class Square
which inherits from the Rectangle class
which is a subclass of BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits the Rectangle class"""
    def __init__(self, size):
        """Initializing and Validating the value of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

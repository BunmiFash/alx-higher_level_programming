#!/usr/bin/python3


"""Module that creates a class Rectangle
which inherits from the BasGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits the BaseGeometry class"""
    def __init__(self, width, height):
        """Initializing and Validating the values of width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(type(self).__name__,
                                         self.__width, self.__height)

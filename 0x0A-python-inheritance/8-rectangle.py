#!/usr/bin/python3


"""Module that creates a class Rectangle
which inherits from the BasGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits the BaseGeometry class"""
    def __init__(self, width, height):
        """Initializing and Validating the values of width and height"""
        super().integer_validator("width", height)
        self.__width = width
        super().integer_validator("width", height)
        self.__height = height

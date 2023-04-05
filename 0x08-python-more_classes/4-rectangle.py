#!/usr/bin/python3

"""A module that creates a class Rectangle
and does basic calculations
"""


class Rectangle:
    """Initializing"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """Getter for width"""
    @property
    def width(self):
        return self.__width

    """Setter for width"""
    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Getter for height"""
    @property
    def height(self):
        return self.__height

    """Setter for height"""
    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Method for Area"""
    def area(self):
        return (self.__width * self.__height)

    """Method for Perimeter"""
    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    """Method to print rectangle with #"""
    def __str__(self) -> str:
        rect = ""
        if (self.__height == 0) or (self.__width == 0):
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()
        return rect

    """__repr__"""
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

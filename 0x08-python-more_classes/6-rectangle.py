#!/usr/bin/python3

"""A module that creates a class Rectangle
and does basic calculations
"""


class Rectangle:
    """Number of instances created"""
    number_of_instances = 0

    """Initializing"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        rect = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rect

    """__repr__"""
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    """Method that deletes an instance of rectangle"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

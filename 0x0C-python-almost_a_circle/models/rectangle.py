#!/usr/bin/python3

"""Module Retangle
Creates a Rectangle class
"""
from models.base import Base
import json


class Rectangle(Base):
    """Rectangle class with private instances"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Sets the attribute and calls the id attribute
        of the base class
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the private instance
        width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private instance
        height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the private instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the private instance
        x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the private instance x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the private instance
        y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the private instance y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints out a rectangle with #"""
        for space in range(self.__y):
            print()
        for row in range(self.__height):
            for space_x in range(self.__x):
                print(" ", end='')
            for col in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Returns the string format of Rectangle class"""
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.x,
                self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating the object instances class Rectangle"""
        if args and len(args) > 0:
            idx = 0
            for i in args:
                if idx == 0:
                    if i is None:
                        self.__init__(
                                self.width, self.height, self.x, self.y
                                )
                    else:
                        self.id = i
                elif idx == 1:
                    self.width = i
                elif idx == 2:
                    self.height = i
                elif idx == 3:
                    self.x = i
                elif idx == 4:
                    self.y = i
                idx += 1
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    if val is None:
                        self.__init__(
                                self.width, self.height, self.x, self.y
                                )
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        attr_dict = {
                "x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width
                }
        return attr_dict

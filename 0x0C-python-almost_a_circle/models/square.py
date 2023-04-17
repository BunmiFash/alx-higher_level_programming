#!/usr/bin/python3

"""Module square which creates a class Square with parent
class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square which inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing object instances from class Rectangle
        """
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Retrieves the value of private width"""
        return self.__width

    @size.setter
    def size(self, value):
        """Validate from parent class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns the string format for Square"""
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x,
                self.y, self.size)

    def update(self, *args, **kwargs):
        """Updates the object attributes"""
        if args and len(args) > 0:
            idx = 0
            for arg in args:
                if idx == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif idx == 1:
                    self.size = arg
                elif idx == 2:
                    self.x = arg
                elif idx == 3:
                    self.y = arg
                idx += 1
        else:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(
                                self.size, self.x, self.y
                                )
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        attr_dict = {
                "id": self.id, "x": self.x,
                "size": self.size, "y": self.y
                }
        return attr_dict

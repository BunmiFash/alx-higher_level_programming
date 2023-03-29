#!/usr/bin/python3

""" A square class is defined"""


class Square:
    """ The method creates a private instance attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """ This method retireves the value of __size"""
    @property
    def size(self):
        return self.__size

    """ This method sets the value of __size"""
    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ This method retrieves the coordinates of the square """
    @property
    def position(self):
        return self.__position

    """ This method sets the coordinates of the square """
    @position.setter
    def position(self, value):
        if (type(value) is not tuple) or (len(value) != 2) or  \
           (type(value[0]) is not int) or \
           (type(value[1]) is not int) or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ Area Mthod that returns the area of the square"""
    def area(self):
        return self.__size ** 2

    """ This method prints a square with # """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        sqr = self.__size
        for i in range(self.__position[1]):
            print("")
        while (sqr > 0):
            for i in range(self.__position[0]):
                print("_", end='')
            for i in range(self.__size):
                print("#", end='')
            print()
            sqr -= 1

    """ Magic Method __str__"""
    def __str__(self):
        obj = ""
        if self.__size == 0:
            print()
            return
        sqr = self.__size
        for i in range(self.__position[1]):
            print("")
        while (sqr > 0):
            for i in range(self.__position[0]):
                print("_", end='')
            for i in range(self.__size):
                print("#", end='')
            print()
            sqr -= 1

        return obj

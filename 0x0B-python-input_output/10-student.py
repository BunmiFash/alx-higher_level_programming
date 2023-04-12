#!/usr/bin/python3

""" Module 9-student
Creates a class Student
"""


class Student:
    """class Student with public instance attributes"""

    def __init__(self, first_name, last_name, age):
        """Initializing the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the class student"""
        if (type(attrs) == list and
                all(type(a) == str for a in attrs)):
            return {b: getattr(self, b) for b in attrs if hasattr(self, b)}
        return self.__dict__

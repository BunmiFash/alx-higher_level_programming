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

    def to_json(self):
        """Retrieves a dictionary representation of the class student"""
        return self.__dict__

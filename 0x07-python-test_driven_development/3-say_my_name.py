#!/usr/bin/python3

"""A module that prints out first and last names"""


def say_my_name(first_name, last_name=""):
    """Prints First and Last Names
    Args:
        first_name: First Name
        last_name: Last Name
    Raises:
        TypeError if an argument other than string is raised
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

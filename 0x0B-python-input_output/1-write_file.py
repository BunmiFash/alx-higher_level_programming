#!/usr/bin/python3


"""Module 1-write_file
Writes into a file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w', encoding='UTF8') as a_file:
        return (a_file.write(text))

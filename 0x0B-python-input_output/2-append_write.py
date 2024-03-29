#!/usr/bin/python3

"""Module 2-append_write
Appends string to a file
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """

    with open(filename, 'a', encoding='UTF8') as a_file:
        return (a_file.write(text))

#!/usr/bin/python3


"""Module 100-append_after
Inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string
    """

    with open(filename, encoding='UTF8') as a_file:
        editted = ""
        for line in a_file:
            editted += line
            if (search_string in line):
                editted += new_string
    with open(filename, "w", encoding='UTF8') as new:
        new.write(editted)

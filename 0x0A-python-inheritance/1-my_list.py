#!/usr/bin/python3

"""MyList module that prints integers in sorted order"""


class MyList(list):
    """MyList class that inherits the list class"""
    def print_sorted(self):
        """Prints elements of a list in sorted order"""
        print(sorted(self))

#!/usr/bin/python3
"""
The 5-text_indentation module that prints a new line
after the characters . , ?, :

"""


def text_indentation(text):
    """Prints a text with two new lines after the characters . , ? , :

    Args:
        text: Text to be printed

    Raises:
        TypeError if text is not a string
    """
    if not type(text) is str:
        raise TypeError("text must be a string")

    for char in text:
        print(char, end='')
        if char in ['.', '?', ':']:
            print()
            print()
        continue

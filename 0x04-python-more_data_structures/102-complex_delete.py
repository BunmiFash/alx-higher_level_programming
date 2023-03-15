#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    val = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    if value not in val:
        return a_dictionary
    for i in range(len(val)):
        if val[i] == value:
            del a_dictionary[keys[i]]
    return a_dictionary

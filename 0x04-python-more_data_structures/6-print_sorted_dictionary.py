#!/usr/bin/python3
#check#check#check
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        print("{} : {}".format(i, a_dictionary[i]))

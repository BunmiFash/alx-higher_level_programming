#!/usr/bin/python3

# Write a function that replaces an element of a list at a specific position (like in C).

def replace_in_list(my_list, idx, element):
    last_index = len(my_list) - 1
    if (idx < 0) or (idx > last_index):
        return (my_list)
    
    else:
        my_list[idx] = element
        return (my_list)

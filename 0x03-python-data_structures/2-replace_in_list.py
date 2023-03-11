#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    last_index = len(my_list) - 1
    if (idx < 0) or (idx > last_index):
        return (my_list)
    my_list[idx] = element
    return (my_list)

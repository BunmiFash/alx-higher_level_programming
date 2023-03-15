#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list == 0):
        return 0
    add = 0
    div = 0
    for sub in my_list:
        first = sub[0]
        second = sub[1]
        mul = first * second
        add += mul
        div += second
    return (add / div)

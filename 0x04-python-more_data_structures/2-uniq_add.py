#!/usr/bin/python

def uniq_add(my_list=[]):
    uniq_num = set(my_list)
    sum = 0
    for i in uniq_num:
        sum += i
    return sum

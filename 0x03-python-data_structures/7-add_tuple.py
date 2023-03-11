#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    
    if len1 == 0:
        first_a = 0
        second_a = 0
    elif len1 == 1:
        first_a = tuple_a[0]
        second_a = 0
    else:
        first_a = tuple_a[0]
        second_a = tuple_a[1]
    if len2 == 0:
        first_b = 0
        second_b = 0
    elif len2 == 1:
        first_b = tuple_b[0]
        second_b = 0
    else:
        first_b = tuple_b[0]
        second_b = tuple_b[1]

    first = first_a + first_b
    second = second_a + second_b

    new_tuple = (first, second)
    return new_tuple

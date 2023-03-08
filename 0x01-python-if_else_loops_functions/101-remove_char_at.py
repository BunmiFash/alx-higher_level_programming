#!/usr/bin/python3
def remove_char_at(str, n):
    new = []
    count = 0
    for i in str:
        if (count != n):
            new.append(i)
        count += 1
    return ("".join(new))

#!/usr/bin/python3
for i in range(100):
    first_digit = i / 10
    last_digit = i % 10
    if (first_digit < last_digit):
        if (i != 89):
            print("{:02d}, ".format(i), end="")
        else:
            print("{}".format(i))

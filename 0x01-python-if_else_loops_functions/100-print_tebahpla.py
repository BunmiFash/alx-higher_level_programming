#!/usr/bin/python3
number = 122
count = 0
while (count < 26):
    if (count % 2 == 0):
        no = number
    else:
        no = number - 32
    print("{}".format(chr(no)), end="")
    number -= 1
    count += 1

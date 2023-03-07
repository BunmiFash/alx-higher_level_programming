#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = 0
if number > -1:
    value = 1
else:
    value = -1
    number = number * -1
last_digit = (number % 10) * value
number = number * value
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"""Last digit of {number} is {last_digit} and is less than 6 and
    not 0""")



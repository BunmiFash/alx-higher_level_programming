#!/usr/bin/python3

aList = [10,8,4,4]
bList = [2, 8,2, 2, 7]
cList = []

for x, y in zip(aList, bList):
    res = (x / y)
    cList.append(res)

print(cList)

#!/usr/bin/env python3.7

import random

minListSize = 5
maxListSize = 20

minNumber = 1
maxNumber = 10

def generateList():
    listSize = random.randint(minListSize, maxListSize)
    list = []

    while listSize >= 0:
        list.append(random.randint(minNumber, maxNumber))
        listSize -= 1
    return list

def comprehense(list1, list2):
    return set(num for num in list1 if num in list2)
    

print(comprehense(generateList(), generateList()))

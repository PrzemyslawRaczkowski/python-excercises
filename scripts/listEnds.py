#!/usr/bin/env python3.7

import random


def generateRandomList():
    size = random.randint(5, 10)
    generatedNumbers = []
    while size >= 0:
        generatedNumbers.append(random.randint(5, 10))
        size -= 1
    return generatedNumbers


def getFirstAndLastIndexOf(list):
    lastIndex = len(list) - 1
    result = []
    result.append(list[0])
    result.append(list[lastIndex])
    return result


generatedList = generateRandomList()
print(generatedList)
print(getFirstAndLastIndexOf(generatedList))

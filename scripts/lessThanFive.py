#!/usr/bin/env python3.7

def getElementsFromListLessThan(list, comparator):
    results = []

    for num in list:
        if isLessThan(num, comparator):
            results.append(num)
    return results

def printList(list):
    for elem in list:
        print(str(elem))

def isLessThan(number, comparator):
    if number < comparator:
        return True

comparator = 5
list = [1,1,2,3,5,8,13,21,34,55,89]
printList(getElementsFromListLessThan(list, comparator))

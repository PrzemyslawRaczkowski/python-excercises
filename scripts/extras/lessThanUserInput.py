#!/usr/bin/env python3.7

def getNumbersLowerThanCeiling(list, ceiling):
    newList = []
    for num in list:
        if (num < ceiling):
            newList.append(num)
    return newList

originalList = [1,2,3,4,5,6,7,8,9,10]
ceiling = input("Type a ceiling number: ")
print(getNumbersLowerThanCeiling(originalList, int(ceiling)))

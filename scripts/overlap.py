#!/usr/bin/env python3.7

list1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def findOccurences(list1, list2):
    len1 = len(list1)
    len2 = len(list2)

    if len1 >= len2:
        return overlap(list1, list2)
    else:
        return overlap(list2, list1)

def overlap(bigger, smaller):
    results = []
    
    for biggerElem in bigger:
        for smallerElem in smaller:
            if biggerElem == smallerElem:
                if biggerElem not in results:
                    results.append(biggerElem)
    return results    

print(findOccurences(list1, list2))    

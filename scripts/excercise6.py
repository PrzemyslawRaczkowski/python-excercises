#!/usr/bin/env python3.7

userString = input("Type a string, we will check if is palindrome: ")

def isPalindrome(string):
    length = len(string)
    lastIndex = length - 1
    midIndex =  lastIndex / 2
    
    countFromBegining = 0
    countFromTheEnd = lastIndex
    while (countFromBegining <= midIndex):
        if (string[countFromBegining] != string[countFromTheEnd]):
            return False
        countFromBegining+=1
        countFromTheEnd-=1
    return True

print(str(isPalindrome(userString)))





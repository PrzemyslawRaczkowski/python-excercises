#!/usr/bin/env python3.7

userInput = input("Type a word to check if palindorme: ")

def reverse(string):
    length = len(string)
    lastIndex = length - 1
    reversedString = ''

    while lastIndex >= 0:
        reversedString += string[lastIndex]
        lastIndex-=1
    return reversedString

def isPalindrome(string):
    return string == reverse(string)

print(isPalindrome(userInput))


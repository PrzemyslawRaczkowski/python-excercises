#!/usr/bin/env python3.7

def isEven(num, check):
    if (int(num) % int(check) != 0):
        print(check +  "divides " + num + " evenly!")
    else:
        print(check + " divides " + num + " oddly!")

num = input("Type number to divide: ")
check = input("Type divider: ")

isEven(num, check)

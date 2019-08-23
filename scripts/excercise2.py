#!/usr/bin/env python3.7

def checkIfNumberIsOdd(number):
    userGuess = int(number)
    if userGuess % 4 == 0:
        print(str(userGuess) + " is a multiple of 4!")
    elif userGuess % 2 == 0:
        print(str(userGuess) + " is even!")
    else:
        print(str(userGuess) + " is not even!")

number = input("Type a number: ")
checkIfNumberIsOdd(number)

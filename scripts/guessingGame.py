#!/usr/bin/env python3.7
import random

tooHigh = "Too high!"
tooLow = "Too low!"
guess = "You guessed the number!"

history = []

def runGame():
    logHistory("Game started")
    generatedNumber = random.randint(1, 9)
    logHistory("Number to guess: " + str(generatedNumber))
    
    continueGame = True
    while continueGame:
        userGuess = input("Guess the number from 1 to 9: ")
        logHistory("User guess: " + str(userGuess))
        compareAndPrintMessage(int(userGuess), generatedNumber)
        userChoice = input("Type exit if you want to end game, type any key to continue: ")
        if (userChoice == "exit"):
            continueGame = False
            logHistory("Game finished")
            printHistory()

def compareAndPrintMessage(userGuess, generatedNumber):
    if userGuess > generatedNumber:
        print(tooHigh)
        logHistory(tooHigh)
    elif userGuess < generatedNumber:
        print(tooLow)
        logHistory(tooLow)
    else:
        print(guess)
        logHistory(guess)

def logHistory(message):
    history.append(message)

def printHistory():
    for message in history:
        print(message)

runGame()

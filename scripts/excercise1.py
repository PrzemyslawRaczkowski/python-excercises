#!/usr/bin/env python3.7

import datetime


def calculateYearWhenClientPass100Years(name, age, multiplicationIndex):
    now = datetime.datetime.now().year
    year = now + 100 - int(age)
    print(int(multiplicationIndex) * (name + " will be 100 years old in " + str(year) + "\n"))


name = input("Tell me your name: ")
age = input("Type your age: ")
multiplicationIndex = input("How many times do you want to print copy of the message? ")

calculateYearWhenClientPass100Years(name, age, multiplicationIndex)

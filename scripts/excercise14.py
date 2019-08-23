#!/usr/bin/env python3.7

import random


def generateRandomList():
    randomNumbers = []

    counter = 1
    while counter <= 10:
        randomNumbers.append(random.randint(1, 6))
        counter += 1

    return randomNumbers


def removeDuplicates(list):
    filtered = set()

    for num in list:
        filtered.add(num)

    return filtered


def run():
    duplicates = generateRandomList()
    print("List with duplicates: " + duplicates.__str__())

    filtered = removeDuplicates(duplicates)
    print("List without duplicates: " + filtered.__str__())


run()

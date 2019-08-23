#!/usr/bin/env python3.7

def getAllDivisors(number):
    results = []
    for i in range(1,number + 1):
        if number % i == 0:
            results.append(i)
    return results

number = input("Type a number to get all divisors: ")
print(getAllDivisors(int(number)))



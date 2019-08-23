#! /usr/bin/env python3.7


def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)


number = input("Type a number to get fibonacci for: ")
print("Fibonacci number for: " + number + " is: " + str(fibonacci(int(number))))

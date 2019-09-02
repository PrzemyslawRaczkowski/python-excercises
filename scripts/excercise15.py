#!/usr/bin/env python3.7


def reverse(sentence):
    splited = sentence.split(" ")
    splited.reverse()
    return " ".join(splited)


sentence = input("Provide a sentence to reverse: ")
print(reverse(sentence))

#!/usr/bin/python3

""""Print the alphabet in reverse order alternating upper- and lower-case."""
for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 != 0:
        print("{:c}".format(letter - 32), end="")
    elif letter % 2 == 0:
        print("{:c}".format(letter), end="")

#!/usr/bin/python3

def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print('#', end="")
        print("")

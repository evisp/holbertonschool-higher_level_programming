#!/usr/bin/python3
def no_c(my_string):
    without_c = ''
    for letter in my_string:
        if letter not in 'Cc':
            without_c += letter
    return without_c

#!/usr/bin/python3
def uppercase(str):
    result = ''
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            result = result + chr(ord(letter) - 32)
        else:
            result = result + letter
    print('{}'.format(result))

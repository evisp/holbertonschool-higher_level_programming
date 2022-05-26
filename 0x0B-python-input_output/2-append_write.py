#!/usr/bin/python3

""" appends to text file """

def append_write(filename="",text=""):
    """ reads a file """
    with open(filename, encoding='utf-8', mode='a') as file:
        return file.write(text)

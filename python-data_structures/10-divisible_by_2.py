#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_of_two = []
    for el in my_list:
        if el % 2 == 0:
            multiple_of_two.append(True)
        else:
            multiple_of_two.append(False)
    return multiple_of_two

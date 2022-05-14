#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for value in range(x):
        try:
            print(f"{my_list[value]}", end="")
            lenght += 1
        except IndexError:  
            break  
    print("")
    return length

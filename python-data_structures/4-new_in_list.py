#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if idx < 0 or idx not in range(len(my_list)):
        return copy_list
    else:
        copy_list[idx] = element
    return copy_list

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_length = len(my_list)
    new_in_list = my_list.copy()

    if 0 > idx or idx >= my_length:
        return new_in_list
    new_in_list[idx] = element
    return new_in_list
   
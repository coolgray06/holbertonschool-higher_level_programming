#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != "c" or char != "C":
            new_string += my_string
    return new_string

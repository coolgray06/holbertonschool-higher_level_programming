#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    result = [integer % 2 == 0 for integer in my_list]
    return result

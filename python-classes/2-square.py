#!/usr/bin/python3

"""
Module doc: This module checks if the size argument is an integer,
and raises a TypeError exception if it is not.
It also checks if the size argument is less than 0,
 and raises a ValueError exception if it is.
"""


class Square:

    """
    Class doc: Defines a Square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

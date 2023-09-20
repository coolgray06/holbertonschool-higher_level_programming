#!/usr/bin/python3
"""
Module doc: This module is printing a square.
It checks if the size argument is an integer,
and raises a TypeError exception if it is not.
It also checks if the size argument is less than 0,
and raises a ValueError exception if it is.
"""


class Square:

    """
    Class doc: Represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square.
        """
        self.__size = size

    def size(self):
        """
        Retrieves and returns the size of the square.
        """
        return self.__size

    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value: The new size of the square.

            Must be an integer greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of square.
        """
        return self.__size ** 2

    def my_print(self):

        """
        Prints in stdout the square with the character `#`.

        If size equals to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

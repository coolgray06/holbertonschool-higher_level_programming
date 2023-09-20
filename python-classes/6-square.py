#!/usr/bin/python3

"""
Module doc: The class defines the coordinates of a square.
"""


class Square:

    """
    A class to represent a square with attributes.

    Attributes:
        __size: The size of the square.
        __position: The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):

        """
        Initializes a new square.

        Args:
            size: Size of square must be an integer greater than or equal to 0.
            position: Position of square must be a tuple of 2 positive integers
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        if not isinstance(position, tuple) or len(position) != 2\
                or not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = position

    @property
    def size(self):

        """
        Retrieves and returns the size of the square.
        """
        return self.__size

    @size.setter
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

    @property
    def position(self):

        """
        Gets and returns the position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):

        """
        Sets the position of the square.

        Args:
            value: The new position of the square.
            Must be a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2\
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """
        Calculates and returns the area of square.
        """
        return self.__size ** 2

    def my_print(self):

        """
        Prints out coordinates of the square with #.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1])
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

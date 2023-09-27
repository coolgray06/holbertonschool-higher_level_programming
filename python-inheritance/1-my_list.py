#!/usr/bin/python3
"""
Defines an inherited list class MyList.
"""


class MyList(list):
    """
    class for MyList

    Args:
        list (self): Print sorted list
    """

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        my_sorted_list = sorted(self)
        print(sorted(self))

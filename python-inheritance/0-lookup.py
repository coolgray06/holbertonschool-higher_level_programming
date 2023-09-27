#!/usr/bin/python3
"""
Look up available objects.
"""


def lookup(obj):
    """
    Return the available attributes of an object
    in a list using dir func.

    Args:
    (obj) for object
    """
    return (dir(obj))

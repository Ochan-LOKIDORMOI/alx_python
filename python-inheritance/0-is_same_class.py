#!/usr/bin/python3
"""This check if the object is an instance of a class"""


def is_same_class(obj, a_class):
    """This returns True if obj is an instance of a_class: otherwise false."""
    return type(obj) is a_class
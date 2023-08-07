#!/usr/bin/python3
"""This checks if it is an instance or inherited class"""


def is_kind_of_class(obj, a_class):
    """This returns if an object is an instance,
    or if the object is an instance of a class that inherited
    from the specified class: otherwise false.
    """
    return isinstance(obj, a_class)
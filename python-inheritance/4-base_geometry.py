#!/usr/bin/python3
"""This defines a BaseGeometry class"""


class BaseGeometry:
    """
    This is a class for geometry operations.
    """
    def area(self):
        """
        This raises an exception with the sms "area() is not made".
        """
        raise Exception("area() is not implemented")
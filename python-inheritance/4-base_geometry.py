#!/usr/bin/python3

class BaseGeometry:
    """
    This class defines a base geometry.

    Methods:
        area(): Raises an exception with the message "area() is not implemented".
    """
    def area(self):
        """
        This method raises an exception with the message "area() is not implemented".

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
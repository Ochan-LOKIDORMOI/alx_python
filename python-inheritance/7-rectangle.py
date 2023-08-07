#!/usr/bin/python3
class BaseGeometry:
    """
    A base class for geometric shapes.

    Attributes:
        None

    Methods:
        area(): This method is intended to be overridden by subclasses to calculate the area of the shape.
    """
    def area(self):
        """
        Calculate the area of the shape.

        Raises:
            NotImplementedError: This method should be overridden by subclasses to provide the area calculation.

        Returns:
            None
        """
        raise NotImplementedError("area() method is not yet implemented")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle instance with specified width and height.
        __str__(self): Returns a string representation of the rectangle.
        area(self): Calculates the area of the rectangle.
        integer_validator(self, name, value): Validates that a value is a positive integer.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Returns:
            None
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A formatted string describing the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

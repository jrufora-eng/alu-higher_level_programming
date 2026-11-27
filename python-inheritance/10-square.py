#!/usr/bin/python3
"""Module that defines Square inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with validated size."""

    def __init__(self, size):
        """Initialize a Square after validating size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

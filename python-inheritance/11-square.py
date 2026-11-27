#!/usr/bin/python3
"""Module that defines Square with custom string representation."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with validated size and [Square] string format."""

    def __init__(self, size):
        """Initialize a Square after validating size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

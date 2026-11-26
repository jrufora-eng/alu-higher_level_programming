#!/usr/bin/python3
"""Module that defines a class Square with a private size."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size):
        """Initialize the square with a size (no validation)."""
        self.__size = size

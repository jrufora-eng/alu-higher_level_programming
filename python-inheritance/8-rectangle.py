#!/usr/bin/python3
"""Module that defines Rectangle inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class validated by BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

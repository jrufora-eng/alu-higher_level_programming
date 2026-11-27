#!/usr/bin/python3
"""Module that defines the Student class."""


class Student:
    """Student class with basic profile attributes and JSON dict export."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of the Student instance."""
        return self.__dict__.copy()

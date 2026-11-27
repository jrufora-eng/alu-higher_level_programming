#!/usr/bin/python3
"""Module that defines Student with filtered attribute serialization."""


class Student:
    """Student class supporting optional attribute filtering on to_json."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict of Student attributes, filtered by attrs if list of str."""
        if isinstance(attrs, list) and all(
            isinstance(item, str) for item in attrs
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__.copy()

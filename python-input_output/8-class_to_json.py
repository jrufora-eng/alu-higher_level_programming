#!/usr/bin/python3
"""Module that defines a function to get dictionary description of an object."""


def class_to_json(obj):
    """Return the dictionary description of a class instance."""
    return obj.__dict__.copy()

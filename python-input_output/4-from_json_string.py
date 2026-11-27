#!/usr/bin/python3
"""Module that defines a function to parse a JSON string into an object."""
import json


def from_json_string(my_str):
    """Return the Python object represented by JSON string my_str."""
    return json.loads(my_str)

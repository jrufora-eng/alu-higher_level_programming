#!/usr/bin/python3
"""Module that defines a function to serialize an object to JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of my_obj."""
    return json.dumps(my_obj)

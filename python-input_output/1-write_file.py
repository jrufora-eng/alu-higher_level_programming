#!/usr/bin/python3
"""Module that defines a function to write a string to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write text to filename (UTF-8) and return character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

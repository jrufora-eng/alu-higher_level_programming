#!/usr/bin/python3
"""Module that defines a function to append a string to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append text to filename (UTF-8) and return added character count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

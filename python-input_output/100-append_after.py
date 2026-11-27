#!/usr/bin/python3
"""Module that defines append_after to insert text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line in filename containing search_string."""
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string and search_string in line:
                lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)

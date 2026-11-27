#!/usr/bin/python3
"""Module that defines MyList inheriting from list."""


class MyList(list):
    """Custom list class with a sorted printing method."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self)) 

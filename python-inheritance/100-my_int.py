#!/usr/bin/python3
"""Module that defines MyInt with inverted equality operators."""


class MyInt(int):
    """Integer subclass with == and != operators inverted."""

    def __eq__(self, other):
        """Return True when self is not equal to other."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True when self is equal to other."""
        return super().__eq__(other)

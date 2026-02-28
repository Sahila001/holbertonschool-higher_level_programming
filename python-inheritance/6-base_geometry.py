#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an exception since area is not implemented."""
        raise Exception("area() is not implemented")

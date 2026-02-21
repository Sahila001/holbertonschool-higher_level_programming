#!/usr/bin/python3
"""Defines a Square class with private size, getter/setter, and area method"""


class Square:
    """Square class with private instance attribute size"""

    def __init__(self, size=0):
        """Initialize a new square with optional size"""
        self.size = size  # çağırır setter validation

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

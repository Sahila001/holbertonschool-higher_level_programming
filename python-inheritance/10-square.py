#!/usr/bin/python3
"""
Module: 10-square
Defines a Square class inheriting from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a Square with size"""
        self.integer_validator("size", size)
        self.__size = size
        # Pass size as both width and height to Rectangle
        super().__init__(size, size)

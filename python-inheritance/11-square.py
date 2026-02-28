#!/usr/bin/python3
"""
Module: 11-square
Defines a Square class inheriting from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle with custom __str__"""

    def __init__(self, size):
        """Initialize a Square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation [Square] width/height"""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)

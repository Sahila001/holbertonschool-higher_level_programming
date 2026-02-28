#!/usr/bin/env python3
"""
Module task_01_duck_typing
Defines Shape abstract class, Circle and Rectangle subclasses,
and a duck-typed function shape_info
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""

    def __init__(self, radius):
        """Initialize circle with radius"""
        self.radius = radius

    def area(self):
        """Return area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape.
    Relies on duck typing (no isinstance checks).
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

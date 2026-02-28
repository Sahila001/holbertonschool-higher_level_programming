#!/usr/bin/env python3
"""Module for Shape, Circle, Rectangle classes and shape_info function."""
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initializes radius."""
        self.radius = radius

    def area(self):
        """Calculates circle area."""
        # math.pi əvəzinə öz dəyərimizi təyin edirik
        pi = 3.141592653589793
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates circle perimeter."""
        pi = 3.141592653589793
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initializes dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of a shape using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

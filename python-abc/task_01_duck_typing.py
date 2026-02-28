#!/usr/bin/env python3
"""
Module task_01_duck_typing
Defines Shape abstract class, Circle and Rectangle subclasses,
and a duck-typed function shape_info
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self) -> float:
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""

    def __init__(self, radius: float) -> None:
        """Initialize circle with radius"""
        self.radius = radius

    def area(self) -> float:
        """Return area of the circle"""
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self) -> float:
        """Return perimeter of the circle"""
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""

    def __init__(self, width: float, height: float) -> None:
        """Initialize rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return area of the rectangle"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape: Shape) -> None:
    """
    Print area and perimeter of a shape.
    Relies on duck typing (no isinstance checks).
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

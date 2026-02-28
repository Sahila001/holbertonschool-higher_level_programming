#!/usr/bin/env python3
"""
Module task_00_abc
Defines an abstract Animal class and its subclasses Dog and Cat
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal"""

    def sound(self):
        """Return dog sound"""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal"""

    def sound(self):
        """Return cat sound"""
        return "Meow"

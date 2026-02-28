#!/usr/bin/env python3
"""
Module for Dragon and Mixins.
Demonstrates multiple inheritance using mixin classes.
"""


class SwimMixin:
    """Mixin for swimming behavior."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying behavior."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar."""

    def roar(self):
        """Prints roaring message."""
        print("The dragon roars!")

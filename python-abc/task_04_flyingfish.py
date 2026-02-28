#!/usr/bin/env python3
"""
Fish, Bird və FlyingFish sinifləri üçün modul.
Çoxlu mirasalma və metod həlli sırasını (MRO) nümayiş etdirir.
"""


class Fish:
    """Balıq sinfi."""

    def swim(self):
        """Üzmə metodu."""
        print("The fish is swimming")

    def habitat(self):
        """Yaşayış yeri metodu."""
        print("The fish lives in water")


class Bird:
    """Quş sinfi."""

    def fly(self):
        """Uçma metodu."""
        print("The bird is flying")

    def habitat(self):
        """Yaşayış yeri metodu."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Həm Fish, həm də Bird siniflərindən miras alan Uçan Balıq sinfi."""

    def fly(self):
        """Uçma metodunu yenidən təyin edir (override)."""
        print("The flying fish is soaring!")

    def swim(self):
        """Üzmə metodunu yenidən təyin edir (override)."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Yaşayış yeri metodunu yenidən təyin edir (override)."""
        print("The flying fish lives both in water and the sky!")

#!/usr/bin/env python3
"""
CountedIterator sinfi üçün modul.
Bu sinif neçə elementin iterasiya edildiyini izləyir.
"""


class CountedIterator:
    """İterasiya olunan elementlərin sayını saxlayan iterator."""

    def __init__(self, iterable):
        """Iteratoru və sayğacı inisializasiya edir."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Cari sayğac dəyərini qaytarır."""
        return self.counter

    def __next__(self):
        """Növbəti elementi qaytarır və sayğacı 1 vahid artırır."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Obyektin özünü iterator kimi qaytarır."""
        return self

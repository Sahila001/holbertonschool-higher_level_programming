#!/usr/bin/python3
"""Function that returns a dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """Returns a dictionary with all simple attributes of an object."""
    return obj.__dict__.copy()

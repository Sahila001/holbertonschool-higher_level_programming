#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Xüsusi işarələrdən sonra sətirbaşı edirik
    for char in ".:?":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)]
        )

    print("{}".format(text), end="")

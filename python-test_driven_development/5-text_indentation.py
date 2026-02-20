#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = {'.', '?', ':'}
    i = 0
    length = len(text)

    while i < length:
        start = i
        # Move i until we find end char
        while i < length and text[i] not in end_chars:
            i += 1

        # Slice the line, strip spaces
        line = text[start:i + 1].strip() if i < length else text[start:].strip()

        if line:
            print(line)

        i += 1  # Skip the punctuation

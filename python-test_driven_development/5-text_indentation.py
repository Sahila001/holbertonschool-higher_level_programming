#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = {'.', '?', ':'}
    start = 0
    length = len(text)

    for i in range(length):
        if text[i] in end_chars:
            line = text[start:i + 1].strip()
            print(line, end="\n\n")
            start = i + 1

    # Print any remaining text after the last punctuation
    if start < length:
        remaining = text[start:].strip()
        if remaining:
            print(remaining, end="")

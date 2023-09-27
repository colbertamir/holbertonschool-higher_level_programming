#!/usr/bin/python3
"""Defines a file-appending func."""


def append_write(filename="", text=""):
    """Appends (adds) a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the appended file.
        text (str): The string to add (append) to the file.
    Returns:
        The number of char's appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

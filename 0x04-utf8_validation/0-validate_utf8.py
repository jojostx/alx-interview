#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    isValid = True

    for char_code in data:
        if char_code < 0 or char_code > 127:
            isValid = False

    return isValid
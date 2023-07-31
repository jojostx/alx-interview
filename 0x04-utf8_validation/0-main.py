#!/usr/bin/python3
"""
Main file for testing
  # check an integer in the list
  # consider only the least 8 significant bits
  # count = the number of bits from the most significant position that are one's,
  # if count > 4:
  #   return false
  # else: // count is less than 4
  #   look forward in the list until (count - 1)
  #       if all (count - 1) bytes donot have their most significant 2 bits being 10
  #           return false
  #       else
  #           continue outer loop at count index if count index is less than length of data.
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data)) # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data)) # True

data = [467, 133, 108]
print(validUTF8(data)) # True

data = [240, 188, 128, 167]
print(validUTF8(data)) # True

data = [197, 130, 1]
print(validUTF8(data)) # True

data = [229, 65, 127, 256]
print(validUTF8(data)) # False

data = [110, 130, 1]
print(validUTF8(data)) # False

data = [235, 140, 4]
print(validUTF8(data)) # False

data = [235, 140]
print(validUTF8(data)) # False

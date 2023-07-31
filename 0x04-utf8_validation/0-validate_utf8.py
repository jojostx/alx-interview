#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """

    data_lsb = []

    # map the data list to a new list that contains
    # the least significant bytes of each integer
    for v in data:
        v = bin(v & 0xFF)[2:]
        while len(v) < 8:
            v = '0' + v
        data_lsb.append(v)

    data_counts = []
    count = 0
    for v in data_lsb:
        if v.startswith('110'):
            count = 2
        elif v.startswith('1110'):
            count = 3
        elif v.startswith('11110'):
            count = 4
        elif v.startswith('0'):
            count = 1
        else:
            count = 0

        data_counts.append(count)

    is_valid = True
    for (i, v) in enumerate(data_counts):
        if i == 0 and v == 0:
            is_valid = False

        nxt_ix = i + 1
        if (v == 1 and nxt_ix < len(data_counts) and data_counts[nxt_ix] == 0):
            is_valid = False

        if v > 1:
            c = i + v
            s = i + 1
            if s >= len(data_counts):
                is_valid = False
            while s < len(data_counts) and (s < c):
                if data_counts[s] > 0:
                    is_valid = False
                s += 1

            i = s
        pass

    return is_valid

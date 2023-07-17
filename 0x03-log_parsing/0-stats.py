#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
about an imaginary access log file typically from services
like Nginx
"""

import signal
from datetime import datetime
import sys
import re


line_format = re.compile(r'(\S+) - \[(.*?)\] "(.*?)" (\d+) (\d+)')
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
count = 0
status_counts = {}
bytes_sent_total = 0


def handler(signum, frame):
    """
    Signal handler for Ctrl+C interrupt
    """
    print_stats()


def parseLog(line):
    """
    Parse the line and return important metrics
    """
    # Match the line against the regular expression pattern
    match = line_format.match(line.strip())

    # If there is a match, extract the relevant fields
    # and write them to the output file
    if match:
        status = match.group(4)
        file_size = match.group(5)

        if status_codes:
            return [status, file_size]

    return None


def print_stats():
    """
    Print stats to the stdout
    """
    print(f'File size: {bytes_sent_total}')
    for status_ in status_codes:
        stc = status_counts.get(f"{status_}")
        if stc:
            print(f"{status_}: {stc}")


signal.signal(signal.SIGINT, handler)


if __name__ == '__main__':
    for line in sys.stdin:
        count += 1
        stats = parseLog(line.rstrip())
        if stats:
            status = stats[0]
            file_size = stats[1]
            bytes_sent_total += int(file_size)
            status_counts[status] = status_counts.get(status, 0) + 1

            if count % 10 == 0:
                print_stats()

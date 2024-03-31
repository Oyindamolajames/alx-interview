#!/usr/bin/python3

"""A script that reads stdin line by line and computes metrics"""

import sys

def print_stats(status_dict, total_size):
    """Prints information"""
    print("File size: {:d}".format(total_size))
    for status_code, count in sorted(status_dict.items()):
        if count != 0:
            print("{}: {:d}".format(status_code, count))

def process_logs():
    """Processes log lines from stdin"""
    status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                     "404": 0, "405": 0, "500": 0}
    total_requests = 0
    total_size = 0

    try:
        for count, line in enumerate(sys.stdin, start=1):
            if count % 10 == 0:
                print_stats(status_counts, total_size)

            parts = line.split()
            total_requests += 1

            try:
                total_size += int(parts[-1])
            except ValueError:
                pass

            try:
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

        print_stats(status_counts, total_size)

    except KeyboardInterrupt:
        print_stats(status_counts, total_size)
        raise

if __name__ == "__main__":
    process_logs()

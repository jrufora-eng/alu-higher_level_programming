#!/usr/bin/python3
"""Script that reads HTTP log lines from stdin and prints metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print total file size and sorted non-zero status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin line by line and print stats every 10 lines or on exit."""
    total_size = 0
    line_count = 0
    printed_last = False
    codes = ("200", "301", "400", "401", "403", "404", "405", "500")
    status_counts = {code: 0 for code in codes}

    try:
        for line in sys.stdin:
            line_count += 1
            printed_last = False
            parts = line.split()

            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass

                status = parts[-2]
                if status in status_counts:
                    status_counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
                printed_last = True

        if not printed_last:
            print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""Script that reads log lines from stdin and prints size and status metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print cumulative file size and non-zero status counts sorted."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Parse stdin lines every 10 lines and handle KeyboardInterrupt."""
    total_size = 0
    line_count = 0
    valid_codes = ("200", "301", "400", "401", "403", "404", "405", "500")
    status_counts = {code: 0 for code in valid_codes}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass
                code = parts[-2]
                if code in status_counts:
                    status_counts[code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args_count = len(argv)
    sum = 0

    for arg in range(1, args_count):
        sum += int(argv[arg])
    print(f"{sum}")

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_count = len(argv) - 1
    if args_count == 0:
        print('0 arguments.')
    elif args_count == 1:
        print('1 argument:')
    else:
        print(f"{args_count} arguments:")
    for arg in range(args_count):
        print(f"{arg + 1}: {argv[arg + 1]}")

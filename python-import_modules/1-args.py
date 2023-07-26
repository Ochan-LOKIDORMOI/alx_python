#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1
    arguments = sys.argv[1:]

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} {'argument' if num_arguments == 1 else 'arguments'}:")
        for i, arg in enumerate(arguments, 1):
            print(f"{i}: {arg}")
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: factorial.py number")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Use a non-negative integer");
        sys.exit(1)
except ValueError:
    print("Invalid integer")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)
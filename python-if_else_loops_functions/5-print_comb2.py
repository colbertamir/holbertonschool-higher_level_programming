#!/usr/bin/python3
# 4-print_hexa.py
"""Print numbers 0 to 99 in decimal and hexadecimal."""
for number in range(0, 100):
    print(f"{number:2d} = {number:02x}", end=" ")
    print()

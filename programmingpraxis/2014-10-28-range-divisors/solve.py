#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[...] find the number of integers between x and y that are divisible by n;
you may assume that x, y and n are all positive and that x < y.

http://programmingpraxis.com/2014/10/28/number-of-divisors-in-a-range/
"""


def range_divisors(x, y, n):
    """Find the number of numbers divisible by n between x and y."""
    first_div = x + (n - x % n)  # First divisor in range.
    if first_div > y:  # Unless that's already out of range.
        return 0

    return 1 + (y - first_div) // n


def main():
    # Assert that this works. First one is simple:
    print "There should be 3 numbers divisible by 5 between 8 and 20."
    if range_divisors(x=8, y=20, n=5) == 3:
        print "Yup."

    # This one is from the website.
    print
    print "There should be 14 numbers divisible by 7 between 100 and 200."
    if range_divisors(x=100, y=200, n=7) == 14:
        print "Yup."


if __name__ == '__main__':
    main()

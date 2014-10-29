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


def test(x, y, n, expect):
    print "Are there %s numbers divisible by %s between %s and %s?" % (
        expect, n, x, y)
    if range_divisors(x, y, n) == expect:
        print "Yup."
    else:
        print "Nope."
    print


def main():
    # Assert that this works. First one is simple:
    test(x=8, y=20, n=5, expect=3)

    # This one is from the website.
    test(x=100, y=200, n=7, expect=14)

    # What about a negative range.
    test(x=-200, y=-100, n=40, expect=2)


if __name__ == '__main__':
    main()

"""
Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
"""

import gmpy2

def is_prime(num):
    if num > 0:
        if gmpy2.is_prime(num):
            return True
    return False

print(is_prime(45))
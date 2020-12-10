import math

def isPrime(number):
    """Return true is the passed in number is prime, fasle otherwise"""

    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    bound = int(math.sqrt(number)) + 1

    for divisor in range(3, bound, 2):
        if number % divisor == 0:
            return False

    return True

def primesUpTo(n):
    """Takes a natural number n, and returns a list of all of the primes
    numbers between 0 and n(exclusive). A ValueError will be raised if n is negative."""

    if n < 0:
        raise ValueError("n must not be negative")

    primes = []

    for number in range(n):
        if isPrime(number):
            primes.append(number)


    return primes

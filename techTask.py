import math
from bitarray import bitarray

FIRST_PRIME = 2

def isPrime(numbers, number):
    return numbers[number - FIRST_PRIME]

def markAsNotPrime(numbers, number):
    numbers[number - FIRST_PRIME] = False

def primesUpTo(n):
    """Takes a natural number n, and returns a list of all of the primes
    numbers between 0 and n(exclusive). A ValueError will be raised if n is negative."""

    if n < 0:
        raise ValueError("n must not be negative")
    elif n >= 0 and n <= FIRST_PRIME:
        return []

    # 0 and 1 not to included in the numbers list
    numbersLength = n - FIRST_PRIME

    # Indicates if a number is prme or not
    # Index 0 maps to 2, index 1 to 3, index 2 to 4 ect...
    numbers = bitarray(numbersLength)
    # All prime to begin with
    numbers.setall(True)

    # Only needs to look up to the sqrt of n(inclusive), as when it gets to the sqrt of n
    # all of the composite numbers will have been found
    bound = math.ceil(math.sqrt(n)) + 1

    for number in range(FIRST_PRIME, bound):
        if isPrime(numbers, number):
            for compositeNumber in range(number * number, n, number):
                markAsNotPrime(numbers, compositeNumber)

    primes = []

    for number in range(FIRST_PRIME, n):
        if isPrime(numbers, number):
            primes.append(number)

    return primes

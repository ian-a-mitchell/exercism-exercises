from math import sqrt
import itertools as it
from functools import cache

# Adapted to test the primality of numbers > 2
# This allows 1) instantly rejecting any even number
# 2) only iterating over odd numbers
# in practice this allows ~40% faster execution

# A better primality algorithm would be even better, of course
@cache
def primality(n):
    
    upper = int(sqrt(n)) + 1

    return (n % 2 != 0) and not any(n % k == 0 for k in range(3, upper, 2))
    
def prime(number):
    
    if number == 0:
        raise ValueError('there is no zeroth prime')
        
    # the prime number 2 has to be handled specially
    output = 2
    
    if number != 1:
        primes = it.islice(filter(primality, it.count(3, 2)), number - 1)
        for _ in range(number - 1): output = next(primes)
            
    return output
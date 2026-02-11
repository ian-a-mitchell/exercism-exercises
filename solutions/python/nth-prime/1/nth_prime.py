from math import sqrt
import itertools as it

def primality(n):
        
    upper = int(sqrt(n)) + 1
    
    if n % 2 == 0:
        return False
    
    for i in range(3, upper, 2):
        if n % i == 0:
            return False
            
    return True

def next_prime(base):
    
    if base % 2 == 0:
        base = base + 1
        
    for n in it.count(base, 2):
        if primality(n):
            return n
    
def prime(number):
    
    if number == 0:
        raise ValueError('there is no zeroth prime')
        
    primes = [2, 3]
        
    while len(primes) < number:
        primes.append(next_prime(primes[-1] + 2))
            
    return primes[number - 1] 
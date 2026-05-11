""" 
Module for finding all prime numbers less than the provided limit using the
Sieve of Eratosthenes method.
"""

PRIME = "prime"
NOT_PRIME = "not prime"

def primes(limit: int) -> list[int]:
    """
    Finds all primes less than the provided limit using the Sieve of
    Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    Parameters
    ----------
    limit : int
        The limit to calculate prime numbers up to (and including).

    Returns
    -------
    list[int]
        All prime numbers less than or equal to limit.
    """
    
    not_prime = set()
    prime = []
    
    for num in range(2, limit + 1):
        if num not in not_prime:
            prime.append(num)
            not_prime.update(range(num + num, limit + 1, num))
                    
    return prime

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
    
    primes_list = [[num, "prime"] for num in range(2, limit + 1)]
        
    output = []
        
    for idx, num in enumerate(primes_list):
        n, primality = num
        if primality == PRIME:
            output.append(n)
            for mark_idx in range(idx + n, len(primes_list), n):
                primes_list[mark_idx][1] = NOT_PRIME
                    
    return output

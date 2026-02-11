def is_palindrome(candidate):
    
    return str(candidate) == str(candidate)[::-1]

def find_factors(candidate, min_factor, max_factor):
        
    factors = []
    for factor in range(min_factor, max_factor + 1):
        if candidate % factor == 0:
            comp_factor = candidate//factor
            if min_factor <= comp_factor <= max_factor:
                factored = [min(factor, comp_factor), max(factor, comp_factor)]
                if factored not in factors:
                    factors.append(factored)
    
    return factors

def proc_candidates(candidates, min_factor, max_factor):
    
    for candidate in candidates:
        if is_palindrome(candidate):
            factors = find_factors(candidate, min_factor, max_factor)
            if factors:
                return (candidate, factors)
            
    return []
    

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
        
    candidates = range(max_factor ** 2, min_factor ** 2 - 1, -1)
    
    solution = proc_candidates(candidates, min_factor, max_factor)
    
    if not solution:
        solution = (None, [])

    return solution


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
    
    candidates = range(min_factor ** 2, max_factor ** 2 + 1, 1)
    
    solution = proc_candidates(candidates, min_factor, max_factor)
    
    if not solution:
        solution = (None, [])

    return solution

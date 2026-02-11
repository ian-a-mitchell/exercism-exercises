from functools import cache

def is_palindrome(candidate):
    
    return str(candidate) == str(candidate)[::-1]

@cache
def generate_palindromes(min_factor, max_factor):
    
    output = []
    
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            candidate = i * j
            if is_palindrome(candidate):
                insertion = (candidate, min(i, j), max(i, j))
                if insertion not in output:
                    output.append(insertion)
              
    if output:
        output = sorted(output, key = lambda x: (x[0], x[1]))
                
    return output

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
    
    output = (None, [])
    
    candidates = generate_palindromes(min_factor, max_factor)
    
    if candidates: 
        max_palindrome = candidates[-1][0] 
        candidates = list(filter(lambda x: x[0] == max_palindrome, candidates))
        factors = []
    
        for candidate in candidates:
            factors.append([candidate[1], candidate[2]])
        
        output = (max_palindrome, factors)

    return output


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

    output = (None, [])
    
    candidates = generate_palindromes(min_factor, max_factor)
    
    if candidates: 
        min_palindrome = candidates[0][0] 
        candidates = list(filter(lambda x: x[0] == min_palindrome, candidates))
        factors = []
    
        for candidate in candidates:
            factors.append([candidate[1], candidate[2]])
        
        output = (min_palindrome, factors)

    return output

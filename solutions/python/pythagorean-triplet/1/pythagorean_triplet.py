""" 
Module to calculate all Pythagorean triplets that sum to a provided number.
"""

from math import gcd, isqrt

def triplets_with_sum(number: int) -> list[list[int]]:
    """
    Calculates all Pythagorean triplets that sum to a given number, number.
    
    Proceeds by using Euclid's formula
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
    for integers m > n > 0; m,n coprime (gcd(m, n) == 1); and either m or n
    but not both is even (this ensures that the generated set is primitive,
    that is, gcd(a, b, c) == 1).
    
    First, note that a + b + c = 2 * m ** 2 + 2 * m * n, therefore number must
    be even for a solution to exist.
    
    Second, note that the maximum possible value of m comes when n = 1, so
        N = 2 * m ** 2 + 2 * m
    With an error of 2 * sqrt(N/2), the solution to this can be approximated by
        m = sqrt(N/2)
    This provides an upper bound on the values of m that need to be checked.
    
    Similarly, the maximum possible value of n comes when n = m - 1, so
        N = 4 * n ** 2 + 6 * n + 2
    This may also be approximated by
        n = sqrt((N / 2 - 1) / 2)
    With an error of 6 * sqrt((N / 2 - 1) / 2).
    
    Note that both of these upper bounds are for flow control, so reducing the
    size of the error term improves performance but not accuracy.
    
    The actual meat of the algorithm comes in iterating over possible values of
    m from 2 to m_max. This allows the calculation of the correct starting 
    value for n (if m is odd then n must be even and vice-versa to ensure that
    the generated triplets are primitive). 
    
    The range of possible n values (from the calculated start value up to and
    including either m - 1 or sqrt((N / 2 - 1) / 2), whichever is less) is then
    stepped over in size-2 steps, to ensure it remains odd/even.
    
    For each pair m, n, if it is coprime then the resulting N value is
    calculated using the above formula. If N % number == 0, i.e. number / N is
    an integer k, the a, b, c triplet is calculated using k times the above
    formulas for a, b, c, the resulting list is sorted to match the desired
    output format and inserted into the output list. Then the next n value is
    checked, or it falls through and to the next m value, etc.
    
    If any of the above checks fails, it skips immediately to the next n value,
    or the next m value, etc.
    
    Note that single-letter variable names *are intended* to align with the
    mathematical literature on the subject.

    Parameters
    ----------
    number : int
        The number which the output triplets should sum to.

    Returns
    -------
    list[list[int]]
        A list of lists of Pythagorean triplets summing to the given number.
    """
    
    output = []
    
    # The sum of Pythagorean triples must be even
    if number % 2 != 0:
        return output
    
    # Calculates the maximum possible values for m and n
    m_max = isqrt(number // 2)
    n_max = isqrt((number // 2 - 1) // 2)
    
    for m in range(2, m_max + 1):
        n_start = 2
        if m % 2 == 0:
            n_start = 1
        for n in range(n_start, min(m, n_max + 1), 2):
            if gcd(m, n) == 1:
                N = 2 * m ** 2 + 2 * m * n
                if number % N == 0:
                    k = number // N
                    a = k * (m ** 2 - n ** 2)
                    b = k * 2 * m * n
                    c = k * (m ** 2 + n ** 2)
                    triplet = sorted([a, b, c])
                    output.append(triplet)
    
    return output
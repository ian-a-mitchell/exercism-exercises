""" Method for solving the Sum of Multiples Exercism problem. """
    
def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Calculates:
        1: All multiples of the provided base values that are less than the
           provided limit;
        2: The sum of all unique values in 1, i.e. if a multiple of the base
           values is less than the provided limit it is only counted once.
           
    This is done by directly generating a set of multiples using a set
    comprehension and the fact that the range() method allows iterating by
    arbitrary numerical steps, then calculating the sum of values in the set.

    Parameters
    ----------
    limit : TYPE
        DESCRIPTION.
    multiples : list[int]
        A list of integer base values to calculate the multiples of.

    Returns
    -------
    int
        The sum of all unique multiples of the integers in multiples that are
        less than limit.
    """
    
    return sum({multiple for base in multiples 
              if base != 0 
              for multiple in range(base, limit, base)})
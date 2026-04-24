""" Methods for solving the Sum of Multiples Exercism problem. """
def find_multiples(limit: int, base_value: int) -> set:
    """
    Calculates the unique multiples of a provided base value that are less than
    the given limit.

    Parameters
    ----------
    limit : int
        The upper bound for the multiples.
    base_value : int
        The base value to calculate the multiples of.

    Returns
    -------
    set
        The set of unique multiples of base value less than limit, if any.
    """
        
    try:
        true_limit = limit // base_value
    except ZeroDivisionError:
        return set()
    else:
        # Since no multiple can be *equal to* the limit, the maximum multiplier
        # of the provided base value needs to be decreased by one step if the
        # base value evenly divides the limit.
        if limit % base_value == 0:
            true_limit -= 1
        return {base_value * mult for mult in range(1, true_limit + 1)}
    
def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Calculates:
        1: All multiples of the provided base values that are less than the
           provided limit;
        2: The sum of all unique values in 1, i.e. if a multiple of the base
           values is less than the provided limit it is only counted once.
           
    This is done by generating a list of sets of multiples fulfilling criteria
    1, and then calculating the sum of the union of those sets.

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
    
    points_list = [find_multiples(limit, multiple) for multiple in multiples]
    
    return sum(set().union(*points_list))

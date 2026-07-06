""" Module solving the Book Store exercise from Exercism. """

from copy import deepcopy

PRICE = 800

DISCOUNTS = (1.0, 1.0, 0.95, 0.90, 0.80, 0.75)

def total_multiset(subset_len: int, basket: list[int]) -> int:
    """
    Helper function for handling the case where the basket is not a set of
    books, that is, at least one title appears more than once.

    Parameters
    ----------
    subset_len : int
        The length of the subset to look for.
    basket : list[int]
        The basket of books to calculate the total for.

    Returns
    -------
    int
        The total price of a subset_len sub_basket and the remainder of basket.
    """
    
    remain_basket = deepcopy(basket)
    sub_basket = []
    available_values = set(basket)

    # First add repeated titles to the sub_basket until one copy of each has
    # been added or the sub_basket has reached the desired length.
    for value in available_values:
        if len(sub_basket) < subset_len:
            if remain_basket.count(value) > 1 and sub_basket.count(value) == 0:
                sub_basket.append(value)
                remain_basket.remove(value)
            
    # if the sub-basket has not matched the desired length, add titles that
    # haven't been added yet (that is, titles that weren't repeated in the
    # original list) until it reaches the desired length.
    for value in set(remain_basket):
        if len(sub_basket) < subset_len:
            if sub_basket.count(value) == 0:
                sub_basket.append(value)
                remain_basket.remove(value)
        
    return total(sub_basket) + total(remain_basket)

def total(basket: list[int]) -> int:
    """
    Calculates the total of a shopping basket (in cents) containing books from
    a certain series. Discounts are provided for buying more than one book from
    the same series, and the problem is to identify how to divide up the basket
    to minimize the customer cost. A recursive method is used.

    Parameters
    ----------
    basket : list[int]
        A basket of books (identified by number).

    Returns
    -------
    int
        The price paid by the customer for basket.
    """
    
    max_subset = len(set(basket))
    
    output = 0
    
    if max_subset == len(basket) or max_subset == 1:
        output = int(PRICE * len(basket) * DISCOUNTS[max_subset])
    else:
        # Because of the 10 point jump in discount from 3 to 4, there are some
        # cases where several sets of 4 are better than a set of 5 and 3.
        # This only needs to be checked if a set of 5 is even possible.
        if max_subset > 4:
            for subset_len in range(max_subset, 3, -1):
                candidate = total_multiset(subset_len, basket)
                if candidate < output or output == 0:
                    output = candidate
        else:
            output = total_multiset(max_subset, basket)
    
    return output

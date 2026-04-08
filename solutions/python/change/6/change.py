""" Module contains methods to find the combination of coins from a given set
of possible coins that will add up to a target value while minimizing the
number of coins used.
"""

from math import gcd
from functools import reduce
from itertools import combinations_with_replacement

def min_coin_number(coins: list, target: int) -> list:
    """
    Calculates the minimum number of coins from coins needed to make target 
    change value.
    Parameters
    ----------
    coins : list
        The available denominations of coins.
    target : int
        The total value of change we wish to make.

    Returns
    -------
    int
        The minimum number of coins needed to make target units of change.
    """
    
    num_coins = list(range(target + 1))
    len_coins = range(len(coins))
    
    for change in range(1, target + 1):
        minimum = target + 1
        for coin_index in len_coins:
            if coins[coin_index] <= change:
                can = 1 + num_coins[change - coins[coin_index]]
                minimum = min(minimum, can)
        num_coins[change] = minimum
        
    return num_coins[target]

def find_fewest_coins(coins: list, target: int) -> list:
    """
    Find the fewest coins given the provided denomination that add up to
    the desired target. This is equivalent to finding the minimum non-negative
    solution to the linear Diophantine equation
    
        x[0] * coins[0] + x[1] * coins[1] + ... = target
        
    However, trying to find that solution directly is hard, so that's not what
    most solutions do (it is handy for checking whether a solution can be found
    without actually having to look for any, though).
    
    Instead, they take the approach of brute-forcing coin combinations with
    increasing numbers of possible values (i.e., coins) and checking whether
    there are any solutions.
    
    As it happens, there is a fairly elegant way of computing the correct
    number of coins at
    
    http://www.ccs.neu.edu/home/jaa/CSG713.04F/Information/Handouts/dyn_prog.pdf
    
    which can be used to greatly reduce the number of combinations that have to
    be generated. This provides about a 2x speed-up over the brute-force 
    method.

    Parameters
    ----------
    coins : list
        The available denominations of coins.
    target : int
        The total value of change we wish to make.

    Returns
    -------
    list
        A list containing all of the coins from the minimal solution.

    Raises
    ------
    ValueError
        Rasies errors for two reasons:
            1: Target is negative;
            2: It is not possible to make the target with the available coins.
    """
    
    if target < 0:
        raise ValueError("target can't be negative")
        
    # A linear Diophantine equation only has a solution if the right side
    # is a multiple of the greatest common denominator of the parameters
    # on the left side.
    max_div = reduce(gcd, coins)
    
    if target % max_div != 0:
        raise ValueError("can't make target with given coins")
                        
    num_coins = min_coin_number(coins, target)
    
    output = []
        
    # The brute-force solution would iterate from 1 to the maximum number of
    # coins possible (relatively easily calculated).
    combos = combinations_with_replacement(coins, num_coins)
    for combo in combos:
        if sum(combo) == target:
            output = sorted(combo)
            
    return output
            
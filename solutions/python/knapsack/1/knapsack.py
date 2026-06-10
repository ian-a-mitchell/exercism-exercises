""" (Not very good) solution to the Knapsack problem from Exercism. """

from itertools import combinations

def maximum_value(maximum_weight: int, items:list[dict]) -> int:
    """
    Finds the highest possible value combination of items from items that can
    be stored in the given maximum weight. Uses a very straightforward, CS
    101 algorithm of simply generating every possible combination of items
    and checking whether each one fits in the weight limit and has a higher
    value than the current maximum.

    Parameters
    ----------
    maximum_weight : int
        The maximum weight of items that can be carried.
    items : list[dict]
        A list of two-element dictionaries, each dictionary as follows:
            1: Key: "weight"; Value: int representing the weight of the item
            2: Key: "value"; Value: int representing the (monetary?) value
               of the item.

    Returns
    -------
    int
        The total value of the combination of items from items with the highest
        total value and a combined weight less than maximum weight.
    """
    
    max_value = 0
    
    for num_items in range(1, len(items)):
        possibles = combinations(items, num_items)
        for combo in possibles:
            value = sum((item["value"] for item in combo))
            weight = sum((item["weight"]) for item in combo)
            
            if weight <= maximum_weight and value > max_value:
                max_value = value
                
    return max_value
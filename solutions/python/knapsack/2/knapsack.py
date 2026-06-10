""" Better solution to the Knapsack problem from Exercism. """

def maximum_value(maximum_weight: int, items:list[dict]) -> int:
    """
    Finds the highest possible value combination of items from items that can
    be stored in the given maximum weight. Calculates the weight and value of
    all possible combinations of items, then uses max for evaluation.

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
    
    combinations = [(0, 0)]
    
    for item in items:
        combinations += [(weight + item["weight"], value + item["value"])
                         for weight, value in combinations]
        
    return max(value for weight, value in combinations 
               if weight <= maximum_weight)
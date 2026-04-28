""" Solution to the Yacht problem on Exercism. """

def _digit(die: int):
    """ 
    Calculates the score for a set of dice in the game Yacht using any one of
    the "numerical" scoring methods that multiply a dice value by the number of
    dice in the hand which landed that side up.
    """
        
    return lambda dice: dice.count(die) * die

def _straights(score_dice: set[int]):
    """ 
    Determines whether the provided dice match the provided big straight or
    little straight hands (see below) and returns the resulting score.
    """
        
    return lambda dice: 30 if set(dice) == score_dice else 0

def _full_house(dice: list[int]):
    """ 
    Determines whether the provided dice form a "full house" and calculates
    the resulting score.
    """
    
    filled_house = len(set(dice)) == 2 and dice.count(dice[0]) in {2, 3}
                
    return sum(dice) if filled_house else 0

def _four_of_kind(dice: list[int]):
    """
    Determines whether the provided dice form a "four of a kind" and calculates
    the resulting score.
    """
    
    # Guarantees dice[1] is of the "four of a kind" if a four of a kind exists.
    dice = sorted(dice)
    
    return 4 * dice[1] if dice.count(dice[1]) > 3 else 0

# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = _digit(1)
TWOS = _digit(2)
THREES = _digit(3)
FOURS = _digit(4)
FIVES = _digit(5)
SIXES = _digit(6)
FULL_HOUSE = lambda dice: _full_house(dice)
FOUR_OF_A_KIND = lambda dice: _four_of_kind(dice)
LITTLE_STRAIGHT = _straights({1, 2, 3, 4, 5})
BIG_STRAIGHT = _straights({2, 3, 4, 5, 6})
CHOICE = sum

def score(dice: list[int], category) -> int:
    """
    Calculates the score for a throw of Yacht. A series of score-calculating
    functions are defined and stuffed into a dictionary, allowing the correct
    one to be chosen at runtime.

    Parameters
    ----------
    dice : list[int]
        A list of dice forming a hand in the game Yacht.
    category : str
        The category to score the hand with.

    Returns
    -------
    int
        The score for the provided hand given the provided category.
    """
        
    return category(dice)

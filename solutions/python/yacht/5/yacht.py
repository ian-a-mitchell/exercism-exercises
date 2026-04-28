""" Solution to the Yacht problem on Exercism. """

from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS ="fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"

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
    return sum(dice) if sorted(Counter(dice).values()) == [2, 3] else 0
    
def _four_of_kind(dice: list[int]):  
    """  
    Determines whether the provided dice form a "four of a kind" and calculates
    the resulting score.
    """
    # Gets the most common element in the hand
    head = Counter(dice).most_common()[0]

    # head[1] is the number of times the most common element appears.    
    return 4 * head[0] if head[1] > 3 else 0


CATEGORIES = {
    YACHT: lambda dice: 50 if len(set(dice)) == 1 else 0,
    ONES: _digit(1),
    TWOS: _digit(2),
    THREES: _digit(3),
    FOURS: _digit(4),
    FIVES: _digit(5),
    SIXES: _digit(6),
    FULL_HOUSE: _full_house,
    FOUR_OF_A_KIND: _four_of_kind,
    LITTLE_STRAIGHT: _straights({1, 2, 3, 4, 5}),
    BIG_STRAIGHT: _straights({2, 3, 4, 5, 6}),
    CHOICE: sum
}

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
        
    return CATEGORIES[category](dice)

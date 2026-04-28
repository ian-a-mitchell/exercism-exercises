""" Solution to the Yacht problem on Exercism. """

# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"

def _yacht(dice: list[int]) -> int:
    """ 
    Determines whether the provided dice form a "yachet" and returns the 
    resulting score.
    """
        
    return 50 if len(set(dice)) == 1 else 0
    
def _num_method(dice: list[int], die: int):
    """ 
    Calculates the score for a set of dice in the game Yacht using any one of
    the "numerical" scoring methods that multiply a dice value by the number of
    dice in the hand which landed that side up.
    """
        
    return die * dice.count(die)
    
def _full_house(dice: list[int]):
    """ 
    Determines whether the provided dice form a "full house" and calculates
    the resulting score.
    """
    output = 0
        
    if len(set(dice)) == 2:
        if dice.count(dice[0]) in {2, 3}:
            output = sum(dice)
                
    return output
    
def _four_kind(dice: list[int]):
    """ 
    Determines whether the provided dice form a "four of a kind" and calculates
    the resulting score.
    """
        
    output = 0
        
    for die in dice:
        if dice.count(die) >= 4:
            output = 4 * die
                
    return output  
    
def _straights(dice: list[int], score_dice: set[int]):
    """ 
    Determines whether the provided dice match the provided big straight or
    little straight hands (see below) and returns the resulting score.
    """
        
    return 30 if set(dice) == score_dice else 0
    
def _choice(dice: list[int]):
    """ 
    Calculates the score using the "choice" method
    """
        
    return sum(dice)
    
_CATEGORIES = {
    YACHT: _yacht,
    ONES: lambda dice: _num_method(dice, die = 1),
    TWOS: lambda dice: _num_method(dice, die = 2),
    THREES: lambda dice: _num_method(dice, die = 3),
    FOURS: lambda dice: _num_method(dice, die = 4),
    FIVES: lambda dice: _num_method(dice, die = 5),
    SIXES: lambda dice: _num_method(dice, die = 6),
    FULL_HOUSE: _full_house,
    FOUR_OF_A_KIND: _four_kind,
    LITTLE_STRAIGHT: lambda dice: _straights(dice, 
                                  score_dice = {1, 2, 3, 4, 5}),
    BIG_STRAIGHT: lambda dice: _straights(dice,
                               score_dice = {2, 3, 4, 5, 6}),
    CHOICE: _choice,
}

def score(dice: list[int], category: str) -> int:
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
        
    return _CATEGORIES[category](dice)

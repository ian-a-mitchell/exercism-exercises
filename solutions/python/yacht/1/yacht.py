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

def score(dice: list[int], category: str) -> int:
    
    def _yacht(dice: list[int]) -> int:
        
        return 50 if len(set(dice)) == 1 else 0
    
    def _num_method(dice: list[int], die: int):
        
        return die * dice.count(die)
    
    def _full_house(dice: list[int]):
        output = 0
        
        if len(set(dice)) == 2:
            if dice.count(dice[0]) in [2, 3]:
                output = sum(dice)
                
        return output
    
    def _four_kind(dice: list[int]):
        
        output = 0
        
        for die in dice:
            if dice.count(die) >= 4:
                output = 4 * die
                
        return output  
    
    def _straights(dice: list[int], score_dice: set[int]):
        
        return 30 if set(dice) == score_dice else 0
    
    def _choice(dice: list[int]):
        
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
        
    return _CATEGORIES[category](dice)

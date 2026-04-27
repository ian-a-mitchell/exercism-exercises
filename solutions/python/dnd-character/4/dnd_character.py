""" Solution to the DnD Character exercise on Exercism. """

import random as rd

class Character:
    """
        Class representing (some) key stats for a Dungeons and Dragons
        character. Supports random attribute generation.
    """
        
    _ATTRIBUTES = ("strength", "dexterity", "constitution", "intelligence", 
                  "wisdom", "charisma")
    
    @staticmethod
    def dice_throws(throws:int = 4, keep:int = 3, size: int = 6) -> int:
        """
        Randomly generates the value of one attribute following the algorithm
        of throwing throw dice of size size, discarding the smallest throws
        until only keep are left, and summing the rest.
        
        Parameters
        -------
        throws: int
            The number of dice rolls to make. Default value 4.
            
        keep: int
            The number of dice rolls to keep. Default value 3.
            
        size: int
            The size of dice to use. Default value 6.

        Returns
        -------
        int
            Candidate attribute score for one attribute.
        """
        
        throws = [rd.randint(1, size) for _ in range(throws)]
        
        throws = sorted(throws, reverse = True)[0:keep]
                        
        return sum(throws)
                
    def __init__(self) -> None:
        """
        Sets up a new Dungeons and Dragons character using random ability
        generation.
        """
                        
        for attribute in Character._ATTRIBUTES:
            setattr(self, attribute, Character.dice_throws())
        
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self) -> int:
        """
        Returns a random ability score from the available values in the object.
        """
                
        return rd.choice([*vars(self).values()])

def modifier(value):
    """ Calculates the modifier implied by a given ability score. """
    
    return (value - 10) // 2

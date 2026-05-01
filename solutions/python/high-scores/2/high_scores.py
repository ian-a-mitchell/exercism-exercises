""" Module solving the High Scores exercise from Exercism. """

from heapq import nlargest

class HighScores:
    """
    Class for storing a list of high scores on a game and returning some
    special scores (highest, most recent, top three).
    """
    
    def __init__(self, scores: list[int]):
        """
        Create object. the provided list already has the scores in order of 
        when they were accomplished, so no reason to change anything.
        """
        
        self.scores = scores
    
    def personal_best(self) -> int:
        """ Personal best = maximum score. """
        
        return max(self.scores)
    
    def latest(self) -> int:
        """ The latest score is the final score in the list, apparently. """
        
        return self.scores[-1]
    
    def personal_top_three(self) -> list[int]:
        """ Return the three largest scores. """
        
        return nlargest(3, self.scores)

""" 
Method and dictionary for calculating the Scrabble score of a given word.
"""

KEYS = "aeioulnrstdgbcmpfhvwykjxqz"
SCORES = [1] * 10 + [2] * 2 + [3] * 4 + [4] * 5 + [5] * 1 + [8] * 2 + [10] * 2

SCORE_TABLE = {key:SCORES[idx] for idx, key in enumerate(KEYS)}

def score(word: str) -> int:
    """
    Calculates the Scrabble score for a given word.

    Parameters
    ----------
    word : str
        Word to calculate the Scrabble score for.

    Returns
    -------
    int
        Score using the provided scoring table.
    """
            
    return sum(SCORE_TABLE[char] for char in word.casefold())

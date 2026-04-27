""" 
Method and dictionary for calculating the Scrabble score of a given word.
"""

SCORE_TABLE = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}

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

"""
A "module" used to solve the Exercism problem "Word Count"
"""

import re
from collections import Counter

def count_words(sentence: str) -> dict:
    """
    Counts the number of words in the provided text. A "word" is a sequence of 
    alphanumerical characters excluding punctuation except in the case of
    contractions, which may have a single apostrophe.
    

    Parameters
    ----------
    sentence : str
        The text to parse for words.

    Returns
    -------
    dict
        A dictionary of words as keys and the number of times they appear in
        the text as values.
    """
                            
    return Counter(re.findall(r"\b[a-zA-Z0-9']+\b", 
                              sentence.replace("_", " ").casefold()))

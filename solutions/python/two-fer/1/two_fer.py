""" Solution to the Two-Fer exercise on Exercism. """

def two_fer(name:str = "you") -> str:
    """
    Solution to the Two-Fer exercise on Exercism.

    Parameters
    ----------
    name : str, optional
        The name to insert into the sentence "One for X, one for me". The 
        default is "you". This neatly solves the "problem" of the exercise with 
        no if-else clauses needed.

    Returns
    -------
    str
        The sentence "One for X, one for me," with the supplied name inserted
        in place of X.
    """
    
    return f'One for {name}, one for me.'

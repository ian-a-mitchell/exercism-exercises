""" Solution to the Two-Fer exercise on Exercism. """

def two_fer(name:str = "you") -> str:
    """
    Solution to the Two-Fer exercise on Exercism.

    Parameters
    ----------
    name : str, optional
        The name to insert into the sentence "One for X, one for me". The 
        default is "you".

    Returns
    -------
    str
        The sentence "One for X, one for me".
    """
    
    return f'One for {name}, one for me.'

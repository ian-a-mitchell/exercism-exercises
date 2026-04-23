import itertools

""" Method for solving the Exercism "Transpose" problem. """
def transpose(text: str) -> str:
    """
    Transposes a string as if it were a matrix where each line corresponds to
    a row.

    Parameters
    ----------
    text : str
        The string to be transposed.

    Returns
    -------
    str
        The transposed string.
    """
        
    output = itertools.zip_longest(*text.splitlines(), fillvalue = "~")
    output = (''.join(word).rstrip("~").replace("~", " ") for word in output)
    return "\n".join(output)

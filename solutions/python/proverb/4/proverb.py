""" Solution to the Exercism exercise "Proverb" """

def proverb(*args: str, qualifier: str = "") -> list[str]:
    """
    Generates proverbs of the form "For want of an X the Y was lost" given an
    arbitrary set of input keywords. Also allows the addition of a qualifier in
    the final line "And all for the want of a {qualifier} X".

    Parameters
    ----------
    *args : str
        Arbitrary set of strings to use in the proverbs.
    qualifier : str, optional
        Optional qualifier for the final line. The default is "".

    Returns
    -------
    list[str]
        List of strings, each string corresponding to one line of the proverb.
    """
        
    output = [f'For want of a {word} the {next_word} was lost.' 
              for word, next_word in zip(args, args[1:])]
    
    try:
        nail = args[0]
    except IndexError:
        pass # note in this case (no arguments) output is the empty list.
    else:
        end = nail if not qualifier else f'{qualifier} {nail}'
        output.append(f'And all for the want of a {end}.')
    
    return output

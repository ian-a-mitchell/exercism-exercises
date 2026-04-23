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
    
    keywords = list(args)
    
    output = []
    
    try:
        nail = keywords[0]
    except IndexError:
        pass
    else:
        if len(keywords) > 1:
            output = [f'For want of a {keywords[idx]} the {keywords[idx + 1]} was lost.'
                  for idx in range(0, len(keywords) - 1)]
        
        final_line = "And all for the want of a "
        
        if qualifier:
            final_line += f'{qualifier} {nail}.'
        else:
            final_line += f'{nail}.'
        
        output.append(final_line)
    
    return output

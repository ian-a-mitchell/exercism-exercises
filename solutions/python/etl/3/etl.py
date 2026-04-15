""" A method for solving the Exercism exercise "ETL"
"""
def transform(legacy_data: dict) -> dict:
    """
    Transforms legacy data for a word-point game into a new format. Nothing 
    complicated here, just a nested loop in a dictionary comprehension.

    Parameters
    ----------
    legacy_data : dict
        Dictionary containing letter point values in the format
            point: letters
        Each integer point value is associated with a list of (upper-case)
        letters with that point value.

    Returns
    -------
    dict
        Dictionary containing letter point values in the format
            letter: point
        Each (lower-case) letter is associated with its individual point value.
    """
    
    return {
        letter.lower(): point
        for point, letters in legacy_data.items()
        for letter in letters
    }
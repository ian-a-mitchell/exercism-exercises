""" A set of methods that build the lyrics to the children's song
    "Ten Green Bottles".
    
    The verses of the song are built in the form
    
    {n} green bottles hanging on the wall,
    {n} green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be {n -1} green bottles hanging on the wall
    
    Repeate starting at n-1, etc. The only variation comes when n or n - 1 is
    one or zero; in the first case, "bottles" is replaced with "bottle," and in
    the second "zero" is replaced with "no".
    
    Parameters:
        start (int): Number of the first verse
        take (int): Number of verses to supply.
        
    Output:
        output (list): List of strings 
        
"""

MAX_VERSE = 10

INT_TO_STR = {
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
    0: "no"
}

def bottle(bottle_num: int) -> str:
    """
    A method to provide the plural (or not) form of bottle depending on whether
    one bottle or some other number of bottles is at hand in the song.

    Parameters
    ----------
    bottle_num : int
        The number of bottles at hand.

    Returns
    -------
    str
        "bottle" if the verse_num is singular, i.e. one bottle is involved,
        or "bottles" otherwise.
    """
    
    return "bottle" if bottle_num == 1 else "bottles"

def build_verse(verse_num: int) -> list:
    """
    A method to build individual verses for the song "Ten Green Bottles".

    Parameters
    ----------
    verse_num : int
        The number of the verse to build the lyrics for. "Ten Green Bottles" is
        a counting-type song, so this corresponds to the count in the initial
        lines, e.g. 2 for "Two green bottles..."

    Returns
    -------
    list
        A list containing one string for each line in the specified verse.
    """
        
    first_start = f'{INT_TO_STR[verse_num]} green '
    first_end = f'{bottle(verse_num)} hanging on the wall,'
    
    mid_line = "And if one green bottle should accidentally fall,"
    
    last_start = f'There\'ll be {INT_TO_STR[verse_num - 1]} green '
    last_end = f'{bottle(verse_num - 1)} hanging on the wall.'
    
    output = [first_start.capitalize() + first_end] * 2
    output.append(mid_line)
    output.append(last_start + last_end)
    
    return output

def recite(start: int, take=1) -> list:
    """
    SUMMARY.

    Parameters
    ----------
    start : int
        The first verse (with the most bottles on the wall) in the request.
    take : int, optional
        The number of verses to return. The default is 1.

    Returns
    -------
    list
        A list of strings, each string corresponding to one line in the lyrics
        for "Ten Green Bottles". An additional empty string is inserted between
        verses, if more than one verse is requested.

    Raises
    ------
    IndexError
        IndexError is raised if a verse with more than ten bottles is called
        for or if more verses are requested than allowed (e.g., start = 3,
        take = 4)
    """
    
    if start > 10:
        raise IndexError("There are only ten verses in the song!")
    if take > start:
        raise IndexError(f"You requested {take} verses but allowed for at most"
                         + f"{start} verses!")
        
    output = []
    
    for verse_num in range(start, start - take, -1):
        output.extend(build_verse(verse_num))
        if verse_num - 1 > start - take:
            output.append("")
    
    return output

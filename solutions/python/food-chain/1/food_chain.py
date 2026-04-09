ANIMAL = {
    1: "fly",
    2: "spider",
    3: "bird",
    4: "cat",
    5: "dog",
    6: "goat",
    7: "cow",
    8: "horse"
}

ANIMAL_LINE = {
    2: "wriggled and jiggled and tickled inside her",
    3: "How absurd to swallow a ",
    4: "Imagine that, to swallow a ",
    5: "What a hog, to swallow a ",
    6: "Just opened her throat and swallowed a ",
    7: "I don't know how she swallowed a "
}

def verse_builder(verse_num: int) -> list[str]:
    """
    Method for building a specified verse for the song "I Know an Old Lady Who 
    Swallowed A Fly".

    Parameters
    ----------
    verse_num : int
        The verse number to build a verse for. Verse numbers range from 1 (the
        first verse) to 8 (the final verse).

    Returns
    -------
    list[str]
        A list of strings. Each string represents one line from the specified
        verse, the list representing the whole verse.
    """
    
    output = [f'I know an old lady who swallowed a {ANIMAL[verse_num]}.']
        
    if verse_num != 8:
        
        if verse_num > 1:
            if verse_num > 2:
                output.append(ANIMAL_LINE[verse_num] + f'{ANIMAL[verse_num]}!')
            else:
                output.append("It " + ANIMAL_LINE[verse_num] + ".")
            
            for sub_num in range(verse_num, 1, -1):
                swallow_str = f'She swallowed the {ANIMAL[sub_num]}'
                swallow_str += f' to catch the {ANIMAL[sub_num - 1]}'
                if sub_num == 3:
                    swallow_str += " that " + ANIMAL_LINE[sub_num - 1] + "."
                else:
                    swallow_str += "."
                output.append(swallow_str)
    
        final_line = f'I don\'t know why she swallowed the {ANIMAL[1]}.'
        final_line += " Perhaps she'll die."
        
        output.append(final_line) 
    else:
        output.append("She's dead, of course!")
                
    return output
        

def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Method for constructing all of the verses of the song "I Know an Old Lady 
    Who Swallowed a Fly" running from the specified start verse to the 
    specified end_verse, inclusive.

    Parameters
    ----------
    start_verse : int
        The first verse to generate. Can take any value between 1 and 8.
    end_verse : int
        The final verse to generate. Can take any value between 1 and 8.

    Returns
    -------
    list[str]
        A list of strings representing the selected verses. Each string 
        corresponds to one line from the song, except that between verses there
        are empty strings inserted.
    """
    
    output = []
    
    for verse_num in range(start_verse, end_verse + 1):
        output.extend(verse_builder(verse_num))
        if verse_num < end_verse:
            output.append("")
            
    return output

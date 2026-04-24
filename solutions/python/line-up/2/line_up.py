""" 
Method and data structures for solving the Line Up exercise on Exercism.
"""

SPECIAL_SUFFIX = {
    1: "st",
    2: "nd",
    3: "rd"
}

def create_ordinal(number: int) -> str:
    """
    Creates the ordinal form of the provided integer.

    Parameters
    ----------
    number : int
        The integer to be converted to ordinal form.

    Returns
    -------
    str
        The ordinal form of the integer.
    """
    
    suffix = "th"
    
    final_digit = number % 10
    
    if final_digit in SPECIAL_SUFFIX and not (10 < number % 100 < 14):
        suffix = SPECIAL_SUFFIX[final_digit]
        
    return f'{number}{suffix}'

def line_up(name: str, number: int) -> str:
    """
    Solution to the Line Up exercise on Exercise.

    Parameters
    ----------
    name : str
        Name of the customer as a string.
    number : int
        Ticket number of the customer as an int.

    Returns
    -------
    str
        Constructed sentence identifying the customer and ticket number using
        ordinal numbers.
    """
    
    o_number = create_ordinal(number)
    
    output = f'{name}, you are the {o_number} '
    output += "customer we serve today. Thank you!"
    
    return output

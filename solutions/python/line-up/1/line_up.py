""" 
Method and data structures for solving the Line Up exercise on Exercism.
"""

SPECIAL_ENDINGS = {
    "1": "st",
    "2": "nd",
    "3": "rd"
}

EXCLUDE = {
    "1": "11",
    "2": "12",
    "3": "13"
}

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
    
    str_num = str(number)
    key_digits = ""
    ending = "th"
        
    try:
        key_digits = str_num[-2:]
    except IndexError:
        key_digits = str_num
        
    final_digit = key_digits[-1]
                
    if final_digit in SPECIAL_ENDINGS and key_digits != EXCLUDE[final_digit]:
        ending = SPECIAL_ENDINGS[final_digit]
    
    output = f'{name}, you are the {str_num}{ending} '
    output += "customer we serve today. Thank you!"
    
    return output

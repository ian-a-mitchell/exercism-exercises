""" Methods to solve the Say exercise on Exercism. """

ENGLISH_NUMS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"
}

POWER_MARKERS = {
    1e9: " billion",
    1e6: " million",
    1000: " thousand"
}

LOWER = 0
UPPER = 1e12 - 1

def conv_hundreds(number: int) -> str:
    """
    Given number in the range 1 to 999, returns a string containing the same
    number expressed in English, e.g. 268 becomes "two hundred sixty-eight".

    Parameters
    ----------
    number : int
        Integer in the range 1 to 999.

    Returns
    -------
    str
        String representing the parameter number.
    """
    
    output = []
    
    power = 100
    
    hun_plus = number // power > 0
    
    if hun_plus:
        output.append(ENGLISH_NUMS[int(number // power)])
        output.append(ENGLISH_NUMS[power])
        number = int(number % power)
        
    # Most of the complexity here comes from having to avoid appending zero
    # in cases that end with 30, 40, 50, etc.
    if number > 0:
        if number < 21:
            output.append(ENGLISH_NUMS[number])
        else:
            tens = int(number // 10 * 10)
            ones = int(number % 10)
            tail = ""
            if ones > 0:
                tail = ENGLISH_NUMS[tens] + "-" + ENGLISH_NUMS[ones]
            else:
                tail = ENGLISH_NUMS[tens]
            output.append(tail)
            
    return " ".join(output)

def say(number: int) -> str:
    """
    Given number in the range 0 to 999 999 999 999, returns a string containing 
    the same number expressed in English, Works by chunking the string into
    three-digit pieces with an appropriate suffix, then converting each chunk
    into the appropriate "hundreds" phrase, then adding the suffix.

    Parameters
    ----------
    number : int
        Integer in the range 0 to 999.

    Returns
    -------
    str
        String representing the parameter number.
        
    Raises
    -------
    ValueError
        Error raised if input out of specified range.
    """
    
    if number < LOWER or number > UPPER:
        raise ValueError("input out of range")
        
    # Checking early means the rest of the code can assume strict positivity.
    if number == 0:
        return "zero"
        
    chunk_num = {}
    red_num = number
    
    for power, suffix in POWER_MARKERS.items():
        if red_num // power > 0:
            chunk_num[red_num // power] = suffix
            red_num = red_num % power
            
    if red_num > 0:
        chunk_num[int(red_num)] = ""
            
    output = [conv_hundreds(num) + suffix for num, suffix in chunk_num.items()]
                    
    return (" ".join(output)).strip()
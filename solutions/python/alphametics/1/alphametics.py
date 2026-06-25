""" Module solving the Alphametics exercise from Exercism (badly). """

from itertools import permutations

def apply_math(summands: list[str], result: str, trans_table: dict[str: int]) -> bool:
    """
    Given a processed Alphametics puzzle and a translation table between
    letters and integers, sums the provided summands and checks whether they
    add up to the result. True means that they do, False means that they do not
    and the proposed translation is incorrect.

    Parameters
    ----------
    summands : list[str]
        The list of summands from the puzzle.
    result: str
        The result (summation of the summands) from the puzzle.
    trans_table : dict[str: int]
        A table describing a mapping of strings (characters) to integers.

    Returns
    -------
    bool
        True if, using the translation table, the summands add up to the
        result. False otherwise.
    """
    string_trans = {key: str(value) for key, value in trans_table.items()}
    string_trans = str.maketrans(string_trans)
    summands = [int(value.translate(string_trans)) for value in summands]
    result = int(result.translate(string_trans))
    
    return sum(summands) == result
    
def solve(puzzle: str) -> dict[str: int]:
    """
    Given a string representing an Alphamatics puzzle, computes the solution
    (that is, the mapping of characters to integers that produces a valid
    mathematical equation). Simplified through the assumption that the only
    operation is summation.
    
    Works essentially through guess and check. A guess is made at the
    translation between the leading/left-hand characters in each word and
    digits, due to the limit that they cannot be zero, and then a guess is made
    at the remaining characters, if any. If that guess turns out to work, it
    is returned, otherwise new guesses are made. If no guess works, None is
    returned instead.

    Parameters
    ----------
    puzzle : str
        The input puzzle. This is assumed to consist of alphabetic words,
        "+" signs, and an "==" sign separating the right-most word (the result)
        from all other words (the summands).

    Returns
    -------
    trans_table : dict[str: int]
        Translation table between characters and digits, in the form of a
        dictionary with strings (characters) as keys and digits (integers) as
        values.
    """
    
    list_puzzle = puzzle.split(sep = " ")
    result = list_puzzle[-1]
    summands = [chars for chars in list_puzzle[:-1:] if chars.isalpha()]
    
    lead_chars = set([word[0] for word in summands] + [result[0]])
    tail_chars = set("".join(summands) + result) - lead_chars
    
    lead_chars = list(lead_chars)
    tail_chars = list(tail_chars)
    
    lead_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    for digits in permutations(lead_digits, len(lead_chars)):
        lead_table = {lead_chars[idx]: digits[idx] 
                       for idx in range(len(lead_chars))}
        tail_digits = {digit for digit in lead_digits if digit not in digits}
        tail_digits = tail_digits | {0}
        for remain_digits in permutations(tail_digits, len(tail_chars)):
            tail_table = {tail_chars[idx]: remain_digits[idx] 
                          for idx in range(len(tail_chars))}
            trans_table = lead_table | tail_table
            if apply_math(summands, result, trans_table):
                return trans_table
    
    return None

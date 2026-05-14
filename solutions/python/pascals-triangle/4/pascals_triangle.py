""" 
Module to calculate the first row_count rows of Pascal's Triangle (counting
with 1-based indexing). Solves the Exercism Pascal's Triangle exercise.
"""

import sys

def calc_cell(row_num: int, cell_num: int) -> int:
    """
    Recursively calculates a given binomial coefficient (n, k), where
    n = row_num, k = cell_num.

    Parameters
    ----------
    row_num : int
        The index of the row this cell is in.
    cell_num : int
        The index of the cell in the row.

    Returns
    -------
    int
        The binomial coefficient (n, k).
    """
    
    # Two base cases, for when you're at a terminal cell (n = k or k = 0) or
    # outside of Pascal's triangle altogether.
    if cell_num < 0 or cell_num > row_num:
        return 0
    if cell_num in (0, row_num):
        return 1
    
    new_row = row_num - 1
    return calc_cell(new_row, cell_num - 1) + calc_cell(new_row, cell_num)

def rows(row_count: int) -> list[list[int]]:
    """
    Returns row_count rows of Pascal's triangle.

    Parameters
    ----------
    row_count : int
        The number of rows to provide.

    Returns
    -------
    list[list[int]]
        A list containing lists, each sub-list being a row of Pascal's
        triangle.

    Raises
    ------
    ValueError
        Raised per tests if row_count < 0.
    RecursionError
        Raised per tests if row_count is too big. Note that trying to run this
        normally will *not* raise this error.
    """
    
    if row_count < 0:
        raise ValueError("number of rows is negative")
        
    # Actually trying to run it just hangs rather than raising an error
    if row_count > sys.getrecursionlimit():
        raise RecursionError("maximum recursion depth exceeded")

    return [[calc_cell(row_num, cell_num) for cell_num in range(row_num + 1)] 
            for row_num in range(row_count)]

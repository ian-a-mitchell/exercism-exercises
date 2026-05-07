""" Module to solve the Rectangles exercise on Exercism. """

_HORIZ_CONT = ("+", "-")
_VERT_CONT = ("+", "|")

_CORNER = "+"

def plus_trace(start_point: tuple[int, int], strings: list[str]) -> int:
    """
    Given a starting upper-left-hand corner character, follows connected
    pathways to find any corner characters that might be lower-right-hand
    corners of a rectangle, and fires off the mirror "minus_trace" function to
    count it if it turns out to be.

    Parameters
    ----------
    start_point : tuple[int, int]
        The indices of the starting corner, which will be the upper-left-hand 
        corner of the rectangle (if it exists).
    strings : list[str]
        A list of strings containing rectangles.

    Returns
    -------
    int
        The number of rectangles with start_point as their upper-left-hand
        corner.
    """
    
    output = 0
    
    start_row = start_point[0]
    start_col = start_point[1]
    
    next_col = start_col + 1
    
    for col in range(next_col, len(strings[start_row])):
        if strings[start_row][col] not in _HORIZ_CONT:
            break
        if strings[start_row][col] == _CORNER:
            for row in range(start_row + 1, len(strings)):
                if strings[row][col] not in _VERT_CONT:
                    break
                if strings[row][col] == _CORNER:
                    output += minus_trace(start_point, (row, col), strings)
    
    return output

def minus_trace(initial_point: tuple[int, int], 
                     second_turn: tuple[int, int], strings: list[str]) -> int:
    """
    Given a starting corner and a "second turn" (lower-right-hand corner) of a 
    rectangle, finds whether a path exists back to the starting corner.

    Parameters
    ----------
    initial_point : tuple[int, int]
        The indices of the starting (upper-left-hand) corner of the rectangle.
    second_turn : tuple[int, int]
        The indices of the "second turn" (lower-right-hand) corner of the
        rectangle.
    strings : list[str]
        A list of strings containing rectangles.

    Returns
    -------
    int
        1 if this path does complete a rectangle, 0 otherwise.
    """
    
    output = 0
    
    start_row = second_turn[0]
    start_col = second_turn[1] - 1
    target_row = initial_point[0]
    target_col = initial_point[1]
    
    for col in range(start_col, target_col - 1, -1):
        if strings[start_row][col] not in _HORIZ_CONT:
            break
        if col == target_col and strings[start_row][col] == _CORNER:
            for row in range(start_row - 1, target_row - 1, -1):
                if strings[row][target_col] not in _VERT_CONT:
                    break
                if row == target_row:
                    output = 1        
    
    return output

def rectangles(strings: list[str]) -> int:
    """
    Given a list of strings containing "+", "-", "|", or " ", counts how many
    rectangles are formed by connected paths of "+", "-", and "|" characters,
    with "+" characters forming corners (if applicable).

    Parameters
    ----------
    strings : list[str]
        A list of strings potentially containing rectangles.

    Returns
    -------
    int
        The number of rectangles in the input list.
    """
    
    output = 0
    
    for row_idx, row in enumerate(strings):
        for col_idx, char in enumerate(row):
            if char == _CORNER:
                output += plus_trace((row_idx, col_idx), strings)
                
    return output

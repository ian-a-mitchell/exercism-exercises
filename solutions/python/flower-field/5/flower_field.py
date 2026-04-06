""" Module providing a set of functions that 'solve' a Minesweeper or
Flower Field-type board by calculating the number of mines or flowers around
each non-mined/flowered point.

Input: List of strings, each string corresponding to one row on the board.
       Each string should have equal length, and contain only spaces and
       the '*' character, representing a flower or mine.
       
Output: List of strings, each string corresponding to one row on the board.
        Each string should precisely match to one of the strings in the input,
        with the blank spaces replaced by the number of flowers/mines adjacent
        to that space (or left blank if no flowers/mines are adjacent)
"""

FLOWER = '*'

def flower_counter(row: int, column: int, garden: list) -> int:
    """ Method for actually calculating the number of flowers around a given
        point (row, column). First identifies the relevant boundaries, then
        iterates over the 3 x 3 box around the chosen point to find any 
        flowers/mines and updates a counter that is ultimately returned.
        
        Note that this is only called if the central point is *not* a flower.
        
        Parameters:
            row (int): Row number of the cell to calculate the number of
            neighboring flowers for.
            column (int): Column number of the cell to calculate the number of
            neighboring flowers for.
            garden (list): The input board.
        
        Returns:
            int: the number of flowers/mines neighboring this cell
    """
    
    output = 0
    
    min_row = max(row - 1, 0)
    max_row = min(row + 2, len(garden))
    
    min_col = max(column - 1, 0)
    max_col = min(column + 2, len(garden[0]))
    
    for flower_row in range(min_row, max_row):
        for flower_col in range(min_col, max_col):
            if garden[flower_row][flower_col] == FLOWER:
                output += 1   
                
    return output

def build_output_cell(row: int, column: int, garden: list) -> str:
    """ Method for determining the correct output value of a given point in
        garden (row, column). Determines whether it is a flower/mine, and if
        not then what the count of neighboring mines is or if it should remain
        blank.
        
        Parameters:
            row (int): Row number of the cell to determine the output for.
            column (int): Column number of the cell to determine the output for.
            garden (list): The input board.
            
        Returns:
            str: A character corresponding to the desired output value:
                '*' if the input board at (row, column) has value '*'
                ' ' if there are no neighboring flowers to cell (row, column)
                An integer counting the number of neighboring flowers to cell
                (row, column) if that value is greater than zero.
    """
    
    output = ' '
    
    if garden[row][column] == FLOWER:
        output = FLOWER
    else:
        flower_count = flower_counter(row, column, garden)
        if flower_count > 0:
            output = str(flower_count)
        
    return output

def make_num_garden(garden: list) -> list:
    
    """ Method for building the updated version of the garden according to
        the program specification.
        
        Parameters:
            garden (list): A list of strings corresponding to a
            flower field/Minesweeper board.
            
        Returns:
            list: A list of strings corresponding to the input board, but with
            blank spaces adjacent to flowers/mines replaced with numbers
            representing the number of adjacent flowers/mines.
    """
    
    output = []
    
    num_row = len(garden)
    num_col = len(garden[0])
    
    for check_row in range(num_row):
        row = []
        for check_col in range(num_col):
            row.append(build_output_cell(check_row, check_col, garden))
        output.append(''.join(row))
    
    return output

def valid_garden(garden: list) -> bool:
    """ Method for determining when a ValueError should be raised for the board
        according to the provided specification. These request that the
        ValueError should be raised if:
            1: The length of the rows (number of columns in each row) is not
               equal (not a rectangular board);
            2: There are any characters other than ' ' and '*' on the board.
    
    Parameters:
        garden (list): A list of strings corresponding to a
        flower field/Minesweeper board.
        
    Returns:
        bool: A boolean representing whether the board is valid (True) or
        invalid (False), where invalidity corresponds to either of the above
        criteria being true, and validity is true otherwise.
    """
    
    output = True
            
    # Builds a set of lengths of strings (rows) in garden and checks whether
    # that set has other than one item (in which case the rows have different
    # numbers of columns)
    if len({len(x) for x in garden}) != 1:
        output = False
                
    # Transforms the garden into a list of lengths of the rows after converting
    # any valid chars into the empty string. If the length > 0, this means that
    # there were characters that were *not* valid.
    if output:
        valid_input = str.maketrans({' ': '', '*': ''})
        validation = sum([len(str.translate(x, valid_input)) for x in garden])
        if validation > 0:
            output = False
            
    return output

def annotate(garden: list) -> list:
    """ Main method for annotating a flower field/Minesweeper board.
    
        Primarily handles validation and output selection rather than the
        actual logic or calculations.
        
    Parameters:
        garden (list): A list of strings corresponding to a
        flower field/Minesweeper board.
        
    Returns:
        list: Three possible options:
            A ValueError if the board is non-rectangular or contains characters
            other than ' ' or '*'.
            A list of empty strings if the board is empty.
            The board but with blank spaces replaced with the number of
            neighboring flowers/mines if there are any neighboring
            flowers/mines.
    """
        
    
    output = []
    
    if garden:
        if not valid_garden(garden):
            raise ValueError('The board is invalid with current input.')
        
        if not garden[0]:
            output = [''] * len(garden)
        else:
            output = make_num_garden(garden)
        
    return output

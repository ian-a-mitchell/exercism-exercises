"""
Set of methods for validating and identifying the current gameplay state of
a tic-tac-toe board. Begins with the gamestate method, with other methods being
helper methods to encapsulate logic or other operations.
"""

CROSS = "X"
NOUGHT = "O"

VICTORY = "win"
DRAW = "draw"
IN_PLAY = "ongoing"

def next_cells(start_row: int, start_col: int) -> list:
    """
    Horrible garbage that "calculates" the cells to check after finding a
    candidate for the start of a victory string. In fact just hand-set based
    on the board and considering what cells would be double-checked using a
    more straightforward approach.

    Parameters
    ----------
    start_row : int
        The row number for the candidate start cell.
    start_col : int
        The column number for the candidate start cell.

    Returns
    -------
    list
        List of tuples, each tuples corresponding to the coordinates of a cell
        that needs to be checked for whether it has the same symbol as the
        provided starting cell.
    """
    
    output = []
    
    if start_row == 0 and start_col == 0:
        output = [(0, 1), (1, 0), (1, 1)]
    if start_row == 0 and start_col == 1:
        output = [(1, 1)]
    if start_row == 0 and start_col == 2:
        output = [(1, 1), (1, 2)]
    if start_row == 1 and start_col == 0:
        output = [(1, 1)]
    if start_row == 2 and start_col == 0:
        output = [(2, 1)]
    
    return output

def find_victory(board: list, start_row: int, start_col: int) -> bool:
    """
    Method to determine whether any victorious tic-tac-toe strings begin at a
    given starting cell (start_row, start_col).
    
    Logic:
        1: Find all of the neighboring cells which should be checked for the
        symbol in the starting cell.
        2: Check each of the relevant neighbor cells in turn.
        3: If one of the relevant neighbor cells has the same symbol as the
        starting cell, calculate the row and column number of the final cell.
            (This is equal to the row/column number of the middle cell plus
             the difference between the middle cell's row/column number and
             the starting cell's row/column number)
        4: Check whether the final cell has the relevant symbol.
        5: If it has, return True; otherwise, continue checking.
        6: If no successful sequences were found, return False.

    Parameters
    ----------
    board : list
        A list of strings corresponding to the game board.
    start_row : int
        The row number for the starting cell.
    start_col : int
        The column number for the starting cell.

    Returns
    -------
    bool
        True if there is a string of three "X"es or "O"es following the rules
        of tic-tac-toe starting from the specified point, False otherwise.
    """
    
    output = False
    
    symbol = board[start_row][start_col]
    
    check_cells = next_cells(start_row, start_col)
    for cell in check_cells:
        next_row, next_col = cell
        if not output and board[next_row][next_col] == symbol:
            final_row = next_row + (next_row - start_row)
            final_col = next_col + (next_col - start_col)
            if board[final_row][final_col] == symbol:
                output = True
    
    return output

def symb_victory(board: list, symbol: str) -> bool:
    """
    A method for determining whether the player with the specified symbol won
    a game of Tic-Tac-Toe/Noughts and Crosses given a game board.
    
    Logic:
        1: Scan the first row and column for instances of the specified symbol.
        2: If any instances are found, call find_victory to determine whether
        that instance is the start of a victorious sequence.
        3: If any victorious sequences are found, return True; else False.
        
    Observation: Some thought shows that any victorious position must have the 
                 specified symbol somewhere in the first row or column.

    Parameters
    ----------
    board : list
        A list of strings corresponding to the game board.
    symbol : str
        The symbol ("X" or "O") to check.

    Returns
    -------
    bool
        True if the specified player has made any winning moves, else False.
    """
    
    output = False
    
    start_row = 0
    start_col = 0
    
    for first_cell_index in range(len(board[start_row])):
        if not output and board[start_row][first_cell_index] == symbol:
            output = find_victory(board, start_row, first_cell_index)
        if not output and first_cell_index != start_col:
            if board[first_cell_index][start_col] == symbol:
                output = find_victory(board, first_cell_index, start_col)
    
    return output
    
def gamestate(board: list) -> str:
    """
    A method to determine the gamestate of a supplied tic-tac-toe board. It
        1: Validates the game state:
            a: The game board is not "impossible" (impossibility means that
               both sides won);
            b: Play started with "X";
            c: "X" has taken the appropriate number of turns.
        2: Checks whether either side has won using the symb_victory method;
        3: If neither side has won, checks whether there has been a draw;
        4: If it is not a draw, victory, or invalid board, it must be an
           ongoing game.
           
    In practice, the logic proceeds as:
        1: Counts the number of "X"es and "O"es to check correct turn-taking;
        2: Checks both "X" and "O" for victory;
        3: Checks whether both have won, making an "impossible" state;
        4: If neither has won, checks whether the board is full and a draw
           has occurred, or whether it has blank spaces and play is ongoing.

    Parameters
    ----------
    board : list
        A list of strings corresponding to a tic-tac-toe game board.

    Returns
    -------
    str
        A string identifying whether the board depicts a won, drawn, or ongoing
        game.

    Raises
    ------
    ValueError
        ValueError is raised according to the specifications above. The error
        message is, unfortunately, specified in such a way that it is difficult
        to automatically generate.
    """
    
    count_crosses = sum((row.count(CROSS) for row in board))
    count_noughts = sum((row.count(NOUGHT) for row in board))
    
    if count_noughts > count_crosses:
        raise ValueError("Wrong turn order: O started")
    if count_crosses - count_noughts == 2:
        raise ValueError("Wrong turn order: X went twice")
        
    win_cross = symb_victory(board, CROSS)
    win_nought = symb_victory(board, NOUGHT)
    
    if win_cross and win_nought:
        raise ValueError("Impossible board: game should have ended after the game was won")
        
    output = IN_PLAY
    
    if win_cross or win_nought:
        output = VICTORY
    elif count_crosses + count_noughts == sum((len(row) for row in board)):
        output = DRAW
    
    return output

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

def symb_victory(board: list, symbol: str) -> bool:
    """
    A method for determining whether the player with the specified symbol won
    a game of Tic-Tac-Toe/Noughts and Crosses given a game board.
    
    Logic:
        1: Construct a new "board" with all possible three-letter sequences
           rendered as separate strings;
        2: Return whether a three-symbol string of the specified symbol exists
           in the solutions "board".

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
        
    check_str = symbol * 3
    
    columns = ["".join(col) for col in list(zip(*board))]
    diagonals = [board[0][0] + board[1][1] + board[2][2], board[2][0] + 
                 board[1][1] + board[0][2]]
    
    solutions = board + columns + diagonals
    
    return check_str in solutions
    
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
        imp = "Impossible board: game should have ended after the game was won"
        raise ValueError(imp)
        
    output = IN_PLAY
    
    if win_cross or win_nought:
        output = VICTORY
    elif count_crosses + count_noughts == sum((len(row) for row in board)):
        output = DRAW
    
    return output

""" Module solving the Queen Attack exercise on Exercism. """

class Queen:
    """ Class representing the position of a chess queen on a board. """
    
    # Configurable to allow non-standard board sizes.
    _BOARD_DIM = 7
    
    def __init__(self, row: int, column: int) -> None:
        """
        Constructor for the queen. Validates the row and column values.

        Parameters
        ----------
        row : int
            The row the queen is on (ranges between 0 and _BOARD_DIM).
        column : int
            The column the queen is on (ranges between 0 and _BOARD_DIM).

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if row or column are outside of the board.
        """
        
        values = [("row", row), ("column", column)]
        
        for value_type, value in values:
            if value > Queen._BOARD_DIM:
                raise ValueError(f'{value_type} not on board')
            if value < 0:
                raise ValueError(f'{value_type} not positive')
        
        self.row = row
        self.column = column

    def can_attack(self, another_queen) -> bool:
        """
        Checks whether "another queen" is on the same row, column, rising
        diagonal, or falling diagonal as this queen, that is, in a position to
        attack or be attacked.

        Parameters
        ----------
        another_queen : Queen
            The other queen to check for whether it may attack or be attacked
            by this queen.

        Returns
        -------
        bool
            True if the queens can attack each other, False otherwise.

        Raises
        ------
        ValueError
            Raised if the queens are initalized with the same coordinates.
        """
                
        their_row = another_queen.row
        their_col = another_queen.column
        error_msg = "Invalid queen position: both queens in the same square"
        
        if their_row == self.row and their_col == self.column:
            raise ValueError(error_msg)
        
        return (
                their_row == self.row or 
                their_col == self.column or
                abs(self.row - their_row) == abs(self.column - their_col)
                )

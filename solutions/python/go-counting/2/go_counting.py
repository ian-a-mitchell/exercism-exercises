WHITE = "W"
BLACK = "B"
NONE = " "

PLAYERS = (WHITE, BLACK, NONE)
DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: list[str]):
        
        self.board = board
        
    def on_board(self, row_idx: int, col_idx: int) -> bool:
        """
        Validates whether a given point is on the game board.

        Parameters
        ----------
        row_idx : int
            The row index of a point to be checked.
        col_idx : int
            The column index of a point to be checked.

        Returns
        -------
        bool
            True if on game board, False otherwise.
        """
        
        valid_row = row_idx >= 0 and row_idx < len(self.board)
        
        return valid_row and col_idx >= 0 and col_idx < len(self.board[row_idx])

    def territory(self, x: int, y: int) -> tuple[str, str]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board
            
        Aside: This is a really dumb way to define coordinates, both because
        it 100% ensures that the linter will complain about too short a
        variable name and because it's completely the opposite of how I would
        expect x and y to be used (that is, as row and column indices,
        respectively). What's worse is that you can't change the names to 
        something clearer because the tests use x and y as keyword variables!!!

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not self.on_board(row_idx = y, col_idx = x):
            raise ValueError("Invalid coordinate")
            
        stack = [(x, y)]
        territory = set()
        stones = set()
        
        while stack:
            col_idx, row_idx = stack.pop()
            if (col_idx, row_idx) not in territory and self.on_board(row_idx, col_idx):
                stone = self.board[row_idx][col_idx]
                if stone == NONE:
                    territory.add((col_idx, row_idx))
                    stack += [(col_idx + dcol, row_idx + drow) for dcol, drow in DELTAS]
                else:
                    stones.add(stone)
                    
        if len(stones) == 1 and len(territory) > 0:
            return (stones.pop(), territory)
        else:
            return (NONE, territory)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        
        territories = {player: set() for player in PLAYERS}
        
        for row_idx, row in enumerate(self.board):
            for col_idx, cell in enumerate(row):
                owner, new_territories = self.territory(col_idx, row_idx)
                known_territories = territories[owner]
                territories[owner] = known_territories | new_territories
                            
        return territories

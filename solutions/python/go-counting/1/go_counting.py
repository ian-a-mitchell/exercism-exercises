import re

WHITE = "W"
BLACK = "B"
NONE = " "

PLAYERS = (WHITE, BLACK, NONE)

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: list[str]):
        
        self.board = board
        
    def find_boundary(self, row_idx: int, col_idx: int) -> tuple[str, str]:
        """
        Find the boundary of a given coordinate on the board. The boundary is
        defined as all cells

        Parameters
        ----------
        row_idx : int
            DESCRIPTION.
        col_idx : int
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.
        str
            DESCRIPTION.
        """

    def territory(self, x: int, y: int) -> tuple[str, str]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board
            
        Aside: This is a really dumb way to define coordinates, both because
        it 100% ensures that the linter will complain about too short a
        variable name and because it's completely the opposite of how x and y
        are normally used (i.e., as row and column indices, respectively).
        What's worse is that you can't change the names to something clearer
        because the tests use x and y as keyword variables!!!

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if y < 0 or y >= len(self.board):
            raise ValueError("Invalid coordinate")
            
        if x < 0 or x >= len(self.board[y]):
            raise ValueError("Invalid coordinate")
            
        value = self.board[y][x]
        
        if value != NONE:
            return (NONE, set())

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

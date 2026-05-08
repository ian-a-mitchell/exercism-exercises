""" Module for finding the winner of a Hex/"Connect" game. """

import re

class ConnectGame:
    """ 
    Class storing the board of a Hex game, with methods to find the winner.
    
    The "HORizontal" player is the one trying to connect the sides of the board
    left-to-right (i.e., horizontally) while the "VERtical" player is the one
    trying to connect the top and bottom edges of the board.
    """
    
    # The two players specified in the problem spec.
    _HOR_PLAY = "X"
    _VER_PLAY = "O"
    
    def __init__(self, board: str):
        """
        Sets up the class, mainly by processing the initial board string into
        something more useful for analysis.
        
        It creates one board organized by rows and another organized by columns
        to allow more symmetry in other code.

        Parameters
        ----------
        board : str
            Multiline string containing a Hex board.

        Returns
        -------
        None
        """
        
        self.row_board = board.split("\n")
        self.row_board = [re.sub(r"\s+", "", row) for row in self.row_board]
        
        self.col_board = []
        
        for idx in range(len(self.row_board[0])):
            col = []
            for row in self.row_board:
                col.append(row[idx])
            self.col_board.append("".join(col))
    
    def _score(self, key_char: str) -> str:
        """
        Scores a Hex board based on the specified key_char (and hence direction
        of play).

        Parameters
        ----------
        key_char : str
            The character representing the player to score, as specified by the
            class variables "_HOR_PLAY" and "_VER_PLAY".

        Returns
        -------
        str
            The string representing the specified player if they scored (won), 
            or the empty string if they did not.
        """
        
        output = ""
        
        start = 0
        
        board = []
        
        if key_char == ConnectGame._HOR_PLAY:
            board = self.col_board
        elif key_char == ConnectGame._VER_PLAY:
            board = self.row_board
        
        # Basic check: the player cannot possibly have won if they do not have
        # a stone in each row (_VER_PLAY) or column (_HOR_PLAY)
        if [block for block in board if key_char not in block]:
            return output
        
        for block_idx, char in enumerate(board[start]):
            if char == key_char and not output:
                path = []
                if key_char == ConnectGame._HOR_PLAY:
                    path = self._walk_board([(block_idx, start)])
                elif key_char == ConnectGame._VER_PLAY:
                    path = self._walk_board([(start, block_idx)])
                if path:
                    output = key_char
        
        return output
    
    def _next_points(self, path: list[tuple]) -> list[tuple]:
        """
        Given a list of already visited points, finds all neighboring unvisited
        points that have a stone from the same player as the most recently
        visited point.

        Parameters
        ----------
        path : list[tuple]
            A list of points that form a continuous path starting on the zeroth
            row (_VER_PLAY) or column (_HOR_PLAY).

        Returns
        -------
        list[tuple]
            A list of points that border the final point in path and have the
            same kind of stone on them.
        """
        
        next_points = []
        
        start_point = path[-1]
        
        start_row = start_point[0]
        start_col = start_point[1]
        
        key_char = self.row_board[start_row][start_col]
        
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if row_offset != col_offset: # This avoids illegal diagonals.
                    next_row = start_row + row_offset
                    next_col = start_col + col_offset
                    if next_row in range(0, len(self.row_board)):
                        if next_col in range(0, len(self.col_board)):
                            next_points.append((next_row, next_col))

        next_points = [point for point in next_points
                       if point not in path
                       and self.row_board[point[0]][point[1]] == key_char]
        
        return next_points
    
    def _walk_board(self, path: list[tuple]) -> bool:
        """
        Given a list of previously visited points with key_char stones on them, 
        tries to find if the path continues to the opposite edge from the 
        starting edge.
        
        Works recursively, with the first base case being reaching the winning 
        edge (obviously, this path therefore does reach it) and the second base
        case being standing on a stone that isn't at the winning edge but
        doesn't have a valid next point to continue the path to (in which case
        this path does not reach the winning edge). The recursive case is where
        the most recent point is not at the winning edge but has unvisited
        neighboring stones of the same player that might continue the path
        there.

        Parameters
        ----------
        path : list[tuple]
            A list of previously visited points with key_char stones on them.
        key_char : str
            The character corresponding to the player being checked, either
            _HOR_PLAY ("X") or _VER_PLAY ("O").

        Returns
        -------
        bool
            True if this path continues to the winning edge, false otherwise.
        """
                
        output = False
        
        start_point = path[-1]
        
        start_row = start_point[0]
        start_col = start_point[1]
        
        key_char = self.row_board[start_row][start_col]
        
        # Base case: this path terminates at the winning edge for the player.
        if key_char == ConnectGame._VER_PLAY:
            if start_row == len(self.row_board) - 1:
                output = True
        elif key_char == ConnectGame._HOR_PLAY:
            if start_col == len(self.col_board) - 1:
                output = True
                
        # Not base case: find possible next points to try and try them.
        if not output:
            next_points = self._next_points(path)
            for point in next_points:
                if not output:
                    output = self._walk_board(path + [point])    
        
        return output          

    def get_winner(self):
        """ Gets the winner of the game given the object's board. """
                
        output = self._score(ConnectGame._HOR_PLAY) 
        output = output or self._score(ConnectGame._VER_PLAY)
        
        return output

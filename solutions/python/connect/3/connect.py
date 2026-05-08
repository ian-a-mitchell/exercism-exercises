""" Module for finding the winner of a Hex/"Connect" game. """

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
    
    _NEIGHBORS = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
    
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
        
        self.row_board = [row.replace(" ", "") for row in board.splitlines()]
        
        self.col_board = list(zip(*self.row_board))
        
        self.max_row = len(self.row_board) - 1
        self.max_col = len(self.col_board) - 1
    
    def _score(self, player: str) -> str:
        """
        Scores a Hex board based on the specified player (and hence direction
        of play).

        Parameters
        ----------
        player : str
            The character representing the player to score, as specified by the
            class variables "_HOR_PLAY" and "_VER_PLAY".

        Returns
        -------
        str
            The string representing the specified player if they scored (won), 
            or the empty string if they did not.
        """
        
        output = ""
                
        board = []
        
        if player == ConnectGame._HOR_PLAY:
            board = self.col_board
        elif player == ConnectGame._VER_PLAY:
            board = self.row_board
        
        # Basic check: the player cannot possibly have won if they do not have
        # a stone in each row (_VER_PLAY) or column (_HOR_PLAY)
        if [block for block in board if player not in block]:
            return output
        
        for block_idx, stone in enumerate(board[0]):
            if stone == player and not output:
                path = []
                if player == ConnectGame._HOR_PLAY:
                    path = self._walk_board([(block_idx, 0)])
                elif player == ConnectGame._VER_PLAY:
                    path = self._walk_board([(0, block_idx)])
                if path:
                    output = player
        
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
        
        player = self.row_board[start_row][start_col]
        
        for neighbor in ConnectGame._NEIGHBORS:
            next_row = start_row + neighbor[0]
            next_col = start_col + neighbor[1]
            if next_row >= 0 and next_col >= 0:
                if next_row <= self.max_row and next_col <= self.max_col:
                    point = (next_row, next_col)
                    next_stone = self.row_board[point[0]][point[1]]
                    if point not in path and next_stone == player:
                        next_points.append(point)
        
        return next_points
    
    def _walk_board(self, path: list[tuple]) -> bool:
        """
        Given a list of previously visited points with player stones on them, 
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
            A list of previously visited points with player stones on them.
        player : str
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
        
        player = self.row_board[start_row][start_col]
                
        # Base case: this path terminates at the winning edge for the player.
        v_win = player == ConnectGame._VER_PLAY and start_row == self.max_row
        h_win = player == ConnectGame._HOR_PLAY and start_col == self.max_col
        if v_win or h_win:
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

""" Module solving the Word Search exercise from Exercism. """

class Point:
    """
    A class representing a point in a 2-D matrix.
    """
    def __init__(self, col: int, row: int):
        """ Sets up the point given row (y) and column (x) values."""
        self.col = col
        self.row = row

    def __eq__(self, other):
        """ Checks for equality of two points."""
        return self.col == other.col and self.row == other.row
    
    def __hash__(self):
        """ Gets rid of pylint complaints about not having hash function. """
        return hash((self.col, self.row))
    
    def __str__(self):
        """ Provides a string representation of the point. """
        return f"col: {self.col}, row: {self.row}"

class WordSearch:
    """
    Class storing a matrix (list of strings) of characters from a word search
    puzzle and providing methods to find where a given word is located in the
    matrix. This is in the form of two Point objects storing the coordinates of
    the first and last letters of the word (or a None object if the word is not
    found). This is mainly complicated by the fact that any word may be
    ordered in any direction, i.e. horizontally, vertically, or diagonally.
    """
    
    def __init__(self, puzzle: list[str]):
        """
        Sets up the internal store for the character matrix.

        Parameters
        ----------
        puzzle : list[str]
            A list of strings representing a table of characters to use for a 
            word puzzle game.

        Returns
        -------
        None
        """
        
        self.puzzle = puzzle

    def search(self, word: str) -> tuple[Point, Point]:
        """
        Finds word in this object's character matrix and returns the
        coordinates of the first and the last letter of the word, respectively,
        or None if word is not findable.
        
        Starting at every point where the first letter of the word is located,
        iterates in one of the eight possible directions until either it runs
        off the matrix or find the word. In the latter case it returns the
        start and end coordinates, in the former it tries the next direction.
        Once all possible directions have been checked, it proceeds to the next
        point where the starting letter of word is located.

        Parameters
        ----------
        word : str
            The word to search for.

        Returns
        -------
        Point
            The point where the first letter of word is located.
        Point
            The point where the last letter of word is located.
        """
        
        width, height = len(self.puzzle[0]), len(self.puzzle)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1),
                      (-1, 1), (1, 1))
        start_points = [(col, row)
                        for row in range(height)
                        for col in range(width)
                        if self.puzzle[row][col] == word[0]]
        
        for col, row in start_points:
            start_point = Point(col, row)
            for direction in directions:
                line = []
                stop_row, stop_col = row, col
                while -1 < stop_row < height and -1 < stop_col < width:
                    line.append(self.puzzle[stop_row][stop_col])
                    if "".join(line) == word:
                        end_point = Point(stop_col, stop_row)
                        return start_point, end_point
                    stop_col += direction[0]
                    stop_row += direction[1]
                             
        return None
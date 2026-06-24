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
    
    def transpose(self):
        """
        Swaps row and column values, that is, finds the coordinates of the
        point in a transposed matrix.
        """
        return Point(self.row, self.col)


class WordSearch:
    """
    Class storing a matrix (list of strings) of characters from a word search
    puzzle and providing methods to find where a given word is located in the
    matrix. This is in the form of two Point objects storing the coordinates of
    the first and last letters of the word (or a None object if the word is not
    found). This is mainly complicated by the fact that any word may be
    ordered in any direction, i.e. horizontally, vertically, or diagonally.
    
    The basic approach used is to store the matrix and then transform it into
    a form appropriate for a particular direction of search. This means that
    the search function only needs to be designed for the horizontal, basic
    search, but requestor function needs to keep track of the transformation
    used and be able to reverse it to get the correct coordinates.
    """
    
    @staticmethod
    def _word_search(matrix: list[str], word: str) -> tuple[Point, Point]:
        """
        Core method of the class. Given a matrix, finds the location of a given
        word in it, just as requested.
        
        This DOES NOT use the stored matrix so that the search functionality
        can be abstracted away from the details of whether the search is for
        the word 

        Parameters
        ----------
        matrix : list[str]
            The appropriate transformed matrix of characters to search for the
            word.
        word : str
            The word to search for.

        Returns
        -------
        Point
            Starting point of the word, that is, the coordinates of the first 
            letter.
        Point
            Ending point of the word, that is, the coordinates of the last 
            letter.
        """
        
        start_point = None
        end_point = None
        
        # Note that I just search for the word and its reversed form at the
        # same time.
        rev_word = word[::-1]
        start_row = -1
        start_col_norm = -1
        start_col_rev = -1
        
        for row_idx, row in enumerate(matrix):
            # Why bother checking a row that can't contain the word?
            if len(row) >= len(word):
                # These if statements mean that if the word has already been
                # found I skip checking more rows.
                if start_col_norm < 0:
                    start_col_norm = row.find(word)
                if start_col_rev < 0:
                    start_col_rev = row.find(rev_word)
                if (start_col_norm > -1 or start_col_rev > -1) and start_row < 0:
                    start_row = row_idx
        
        # This figures out the coordinates of the start and end point if the
        # word was found.
        if start_row > -1:
            word_offset = len(word) - 1
            if start_col_norm > -1:
                # str.find(word) finds the index of the first letter of the
                # word, so the index of the last letter has to be calculated.
                start_point = Point(start_col_norm, start_row)
                end_point = Point(start_col_norm + word_offset, start_row)
            elif start_col_rev > -1:
                # Searching for the reversed word means that str.find(word)
                # now finds the index of the last letter of the word.
                start_point = Point(start_col_rev + word_offset, start_row)
                end_point = Point(start_col_rev, start_row)
                
        if start_point and end_point:
            return (start_point, end_point)
        
        return None
    
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
        
        self._matrix = puzzle
        
    def _trans_puzzle(self) -> list[str]:
        """
        Transposes the character matrix (swaps columns and rows) for
        supporting vertical (column-wise) word searches.

        Returns
        -------
        list[str]
            The character matrix but with columns and rows swapped.
        """
        
        return ["".join(col) for col in zip(*self._matrix)]
    
    def _right_down_diag(self) -> list[str]:
        """
        Builds a version of a list where each "row" corresponds to one of the 
        diagonals heading "down" from top left to bottom right. It starts with
        the diagonal in the lower left corner, iterates up the rows until
        reaching the long diagonal starting at the origin, and then continues 
        along the columns to the upper right corner.
        
        The list is assumed to be rectangular.

        Returns
        -------
        list[str]
            A list of strings--each string corresponds to one diagonal as
            described above.
        """
                
        output = []
        
        # Iterates up the left hand side 
        for main_idx in range(len(self._matrix) - 1, -1, -1):
            diag = []
            row_idx = main_idx
            col_idx = 0
            while col_idx < len(self._matrix[main_idx]) and row_idx < len(self._matrix):
                diag.append(self._matrix[row_idx][col_idx])
                row_idx += 1
                col_idx += 1
            output.append("".join(diag))
        
        for main_idx in range(1, len(self._matrix[0]), 1):
            diag = []
            row_idx = 0
            col_idx = main_idx
            while col_idx < len(self._matrix[0]) and row_idx < len(self._matrix):
                diag.append(self._matrix[row_idx][col_idx])
                row_idx += 1
                col_idx += 1
            output.append("".join(diag))
                  
        return output
    
    def _left_down_diag(self) -> list[str]:
        """
        Similar to _right_down_diag, builds a version of a supplied list where
        each "row" corresponds to one of the diagonals in the list. The
        difference is that in this case the diagonals run from top right to 
        bottom left. As such, it starts with the diagonal at the origin, 
        iterates over the columns to the upper right corner, and then iterates
        down the rows to the lower right corner.

        Returns
        -------
        list[str]
            A list of strings as described above.
        """
        
        output = []
        
        for main_idx in range(len(self._matrix[0])):
            diag = []
            row_idx = 0
            col_idx = main_idx
            while(col_idx > -1 and row_idx < len(self._matrix)):
                diag.append(self._matrix[row_idx][col_idx])
                row_idx += 1
                col_idx -= 1
            output.append("".join(diag))
        
        for main_idx in range(1, len(self._matrix), 1):
            diag = []
            row_idx = main_idx
            col_idx = len(self._matrix[row_idx]) - 1
            while(col_idx > -1 and row_idx < len(self._matrix)):
                diag.append(self._matrix[row_idx][col_idx])
                row_idx += 1
                col_idx -= 1
            output.append("".join(diag))
                  
        return output
    
    def _convert_rd_diag_point(self, diag_point: Point) -> Point:
        """
        Converts the "coordinates" of a point in the rd_diag "coordinate"
        system to those of the regular character matrix. This is done by
        finding the coordinates of the first point of the diagonal and then
        adding diag_depth steps to row and column numbers.
        
        Recall that in the rd_diag coordinate system, the diagonals are counted
        up from the lower left corner of _matrix (diag_num = 0) to the upper
        left corner/origin (diag_num = num_rows - 1) and then to the upper
        right corner (diag_num = max(diag_num)).

        Parameters
        ----------
        diag_point : Point
            A point corresponding to a position in a character matrix expressed
            in rd_diag form.

        Returns
        -------
        Point
            A point corresponding to a position in a character matrix expressed
            in standard form.
        """
        
        diag_num = diag_point.row
        diag_depth = diag_point.col
        
        row_num = 0
        col_num = 0
        
        if diag_num < len(self._matrix):
            row_num = len(self._matrix) - diag_num - 1
        else:
            col_num = diag_num - len(self._matrix) + 1
            
        row_num += diag_depth
        col_num += diag_depth
        
        return Point(col_num, row_num)
    
    def _convert_ld_diag_point(self, diag_point: Point) -> Point:
        """
        Converts the "coordinates" of a point in the ld_diag "coordinate"
        system to those of the regular character matrix. This is done by
        finding the coordinates of the first point of the diagonal and then
        adding diag_depth steps to the row number and subtracting it from the
        column number.
        
        Recall that in the ld_diag coordinate system, the diagonals are counted
        up from the upper left corner of _matrix (diag_num = 0) to the upper
        right corner/origin (diag_num = num_rows - 1) and then to the lower
        right corner (diag_num = max(diag_num)).

        Parameters
        ----------
        diag_point : Point
            A point corresponding to a position in a character matrix expressed
            in ld_diag form.

        Returns
        -------
        Point
            A point corresponding to a position in a character matrix expressed
            in standard form.
        """
        
        diag_num = diag_point.row
        diag_depth = diag_point.col
        
        row_num = 0
        col_num = 0
        
        if diag_num < len(self._matrix):
            col_num = diag_num
        else:
            row_num = diag_num - len(self._matrix) + 1
            col_num = len(self._matrix[0]) - 1
            
        row_num += diag_depth
        col_num -= diag_depth
        
        return Point(col_num, row_num)

    def search(self, word: str) -> tuple[Point, Point]:
        """
        Finds word in this object's character matrix and returns the
        coordinates of the first and the last letter of the word, respectively,
        or None if word is not findable.
        
        Basically just checks every possibility in turn: is it visible looking
        left or right? If not, up and down? If not, along the diagonals running
        top left to bottom right? If not, along the diagonals running top right
        to bottom left? And if none of those, it must not be findable at all.

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
        
        output = WordSearch._word_search(self._matrix, word)
        
        if not output:                        
            output = WordSearch._word_search(self._trans_puzzle(), word)
            if output:
                start_point = output[0].transpose()
                end_point = output[1].transpose()
                output = (start_point, end_point)
                
        if not output:
            output = WordSearch._word_search(self._right_down_diag(), word)
            if output:
                start_point = self._convert_rd_diag_point(output[0])
                end_point = self._convert_rd_diag_point(output[1])
                output = (start_point, end_point)
                
        if not output:
            output = WordSearch._word_search(self._left_down_diag(), word)
            if output:
                start_point = self._convert_ld_diag_point(output[0])
                end_point = self._convert_ld_diag_point(output[1])
                output = (start_point, end_point)
                             
        return output

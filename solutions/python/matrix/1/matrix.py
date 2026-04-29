""" Module for the Matrix exercise on Exercism. """

class Matrix:
    """ 
    Class that creates a representation of a mathematical matrix from a
    provided string. 
    """
    
    def __init__(self, matrix_string: str) -> None:
        """
        Creates matrix from provided string.

        Parameters
        ----------
        matrix_string : str
            String representing a mathematical matrix. Rows are assumed to be 
            separated by newlines, and values by whitespace. All values are
            assumed to be integers.

        Returns
        -------
        None
        """
                            
        self.matrix = [[int(num) for num in row.split()] 
                       for row in matrix_string.split("\n")]

    def row(self, index: int) -> list[int]:
        """
        Returns the requested row.

        Parameters
        ----------
        index : int
            The index of the row to return *in mathematical notation*, i.e.
            counting from 1 upwards instead of 0.

        Returns
        -------
        list[int]
            A list corresponding to the requested row.
        """
        
        return self.matrix[index - 1]

    def column(self, index: int) -> list[int]:
        """
        Returns the requested column.

        Parameters
        ----------
        index : int
            The index of the column to return, also in mathematical form.

        Returns
        -------
        list[int]
            A list corresponding to the requested column.
        """
        
        return [row[index - 1] for row in self.matrix]

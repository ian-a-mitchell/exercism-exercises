""" Program to find the saddle points in a 2-D matrix. These are defined by
the specification to be points that are the maximum of their row and minimum
of their column. Also performs validation to bypass calculation for empty and
non-rectangular matrices.
"""

def saddle_points(matrix: list) -> list:
    """
    Identifies the saddle points in a 2-D matrix per spec described above.
    
    The logic is:
        1: Build a list of the maximum values for each row.
        2: Build a list of the maximum values for each column.
        3: Iterate over the points in the matrix.
        4: If a point is the maximum value for its row and minimum for its
           column, append it to the output list, in the format below.

    Parameters
    ----------
    matrix : list
        List of lists. Each sublist is a list of integers representing tree
        heights.

    Returns
    -------
    output : list
        List of dicts. Each dict contains two values, each value pairing a
        label ("row" or "column") with the row or column number of a saddle
        point as defined above. Note that the row or column numbers here are
        in human/mathematical format, counting 1...2...3, etc.

    Raises
    ------
    ValueError
        Error raised for non-rectangular matrices (matrices with varying row 
        lengths).
    """
    
    output = []
    
    if len(matrix) == 0:
        return output
    
    if len({len(row) for row in matrix}) != 1:
        raise ValueError("irregular matrix")
        
    row_max = [max(row) for row in matrix]
    col_min = [min(col) for col in list(zip(*matrix))]
    
    for row_num, row in enumerate(matrix):
        for col_num, value in enumerate(row):
            if value == row_max[row_num] and value == col_min[col_num]:
                output.append({"row": row_num + 1, "column": col_num + 1})
                
    return output

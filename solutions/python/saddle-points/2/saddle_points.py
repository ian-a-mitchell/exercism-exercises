""" Program to find the saddle points in a 2-D matrix. These are defined by
the specification to be points that are the maximum of their row and minimum
of their column. Also performs validation to bypass calculation for empty and
non-rectangular matrices.
"""

def saddle_points(matrix: list) -> list:
    """
    Identifies the saddle points in a 2-D matrix per spec described above.
    
    The logic is:
        1: Build a transposed matrix (each sub-list now represents a column)
        2: For each row, find the maximum value present in the row.
        3: Iterate over the row to find each instance of the maximum value
           (note that the maximum value may be present more than once!)
        4: Each time you find a case of the maximum row value, check whether
           it is the minimum column value using the transposed matrix.
        5: If it is, insert it into the output list in the desired format.

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
        
    t_matrix = list(zip(*matrix))
    
    for row_num, row in enumerate(matrix, start = 1):
        max_value = max(row)
        for col_num, value in enumerate(row):
            if value == max_value:
                if min(t_matrix[col_num]) == value:
                    output.append({"row": row_num, "column": col_num + 1})
    return output

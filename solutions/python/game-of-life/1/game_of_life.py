from copy import deepcopy

LIVE = 1
DEAD = 0

def neighbors(matrix: list[list[int]], point: tuple[int]) -> list[int]:
    """
    Finds the values of the neighbors of a certain point in a matrix.

    Parameters
    ----------
    matrix : list[list[int]]
        The matrix to find the neighbors for.
    point : tuple[int]
        The point around which to find neighbors.

    Returns
    -------
    list[int]
        A list of the values at every point adjacent to the given point in the
        given matrix.
    """
    
    point_row = point[0]
    point_col = point[1]
    
    start_row = max(point_row - 1, 0)
    start_col = max(point_col - 1, 0)
    
    stop_row = min(point_row + 2, len(matrix))
    stop_col = min(point_col + 2, len(matrix[point_col]))
    
    output = []
    
    for row in range(start_row, stop_row):
        for col in range(start_col, stop_col):
            if (row, col) != point:
                output.append(matrix[row][col])
    
    return output

def num_living_neighbors(matrix: list[list[int]], point: tuple[int]) -> int:
    """
    Calculates the number of living neighbors of a given point in the given
    matrix of cells.

    Parameters
    ----------
    matrix : list[list[int]]
        Matrix of cells that the point is embedded in.
    point : tuple[int]
        The point to calculate the number of living neighbors for.

    Returns
    -------
    int
        The sum of values of the cells. This only works because LIVE = 1 and
        DEAD = 0.
    """
    
    return sum(neighbors(matrix, point))

def tick(matrix: list[list[int]]) -> list[list[int]]:
    """
    Updates the provided "board" of the "game of life" using the specified
    rules:
        1) Living cells die if they do not neighbor 2 or 3 living cells;
        2) Dead cells are "colonized" if they neighbor 3 living cells;
        3) All other cells remain the same.

    Parameters
    ----------
    matrix : list[list[int]]
        DESCRIPTION.

    Returns
    -------
    list[list[int]]
        The updated board.
    """
    
    output = deepcopy(matrix)
    
    for row_num, row in enumerate(matrix):
        for col_num, cell in enumerate(row):
            n_neighbors = num_living_neighbors(matrix, (row_num, col_num))
            if cell == LIVE:
                if n_neighbors not in {2, 3}:
                    output[row_num][col_num] = DEAD
            elif cell == DEAD:
                if n_neighbors == 3:
                    output[row_num][col_num] = LIVE
                    
    return output
            

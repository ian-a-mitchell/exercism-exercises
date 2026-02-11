from itertools import cycle

def spiral_matrix(size):
    
    output = [[None] * size for _ in range(size)]
        
    row, col = 0, 0
    deltas = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    d_row, d_col = next(deltas)
        
    for num in range(1, size**2 + 1):
        output[row][col] = num
        
        if (
            not 0 <= row + d_row < size or
            not 0 <= col + d_col < size or
            output[row + d_row][col + d_col]
        ):
            d_row, d_col = next(deltas)
            
        row += d_row
        col += d_col
            
    return output

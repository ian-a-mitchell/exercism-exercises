EXPECT_ROW = 4
EXPECT_COL = 3

ZERO = ' _ | ||_|   '

ONE = '     |  |   '

TWO = ' _  _||_    '

THREE = ' _  _| _|   '

FOUR = '   |_|  |   '

FIVE = ' _ |_  _|   '

SIX = ' _ |_ |_|   '

SEVEN = ' _   |  |   '

EIGHT = ' _ |_||_|   '

NINE = ' _ |_| _|   '

TRANS = {
    ZERO: '0',
    ONE: '1',
    TWO: '2',
    THREE: '3',
    FOUR: '4',
    FIVE: '5',
    SIX: '6',
    SEVEN: '7',
    EIGHT: '8',
    NINE: '9'
}

def validate(input_grid):
    
    errors = {
        'not input_grid': 'Input cannot be empty',
        'len(input_grid) % EXPECT_ROW != 0':
            'Number of input lines is not a multiple of four',
        'sum([len(s) % EXPECT_COL != 0 for s in input_grid])':
            'Number of input columns is not a multiple of three',
        'len(set([len(s) for s in input_grid])) > 1':
            'Input lines have varying numbers of columns'
    }
        
    for expression in errors:
        if eval(expression):
            raise ValueError(errors[expression])
            
# Converts the raw input into a list of lines which have themselves been
# chunked into a list of grid 'squares'
def chunk_input(input_grid):
    
    output = [input_grid[i:i+EXPECT_ROW] for i in 
              range(0,len(input_grid),EXPECT_ROW)]
    
    output = list(map(chunk_line, output))
        
    return output

# Converts raw lines (list of 4 strings) into list of grid 'squares'
# A grid is the concatenation of 3 corresponding elements from each string, i.e.
# [0][0:3] + [1][0:3] + [2][0:3] + [3][0:3],
# [0][3:6] + [1][3:6] + [2][3:6] + [3][3:6],
# etc.
def chunk_line(raw_line):
    
    output = []
    
    for i in range(0, len(raw_line[0]), EXPECT_COL):
        grid = []
        for s in raw_line:
            grid.append(s[i:i+EXPECT_COL])
        output.append(''.join(grid))
    
    return output

# Converts list of pre-chunked grid 'squares' corresponding to a line of input
# into string of digits
def line_convert(chunked_line):
    
    output = ''.join(list(map(translate, chunked_line)))
    
    return output
            
def translate(grid_square):
    
    output = TRANS[grid_square] if grid_square in TRANS else '?'
             
    return output

def convert(input_grid):
    
    validate(input_grid)
                
    output = list(map(line_convert, chunk_input(input_grid)))
    
    if len(output) == 1:
        output = output[0]
    else:
        output = ','.join(output)
        
    return output
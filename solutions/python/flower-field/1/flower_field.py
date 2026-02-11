FLOWER = '*'

def make_ij_pairs(row, column, num_row, num_col):
    
    output = []
    
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if i >= 0 and i < num_row and j >= 0 and j < num_col:
                output.append((i, j))
                
    return output

def make_num_garden(garden):
    
    output = []
    
    num_row = len(garden)
    num_col = len(garden[0])
    
    for i in range(num_row):
        row = []
        for j in range(num_col):
            if garden[i][j] == FLOWER:
                row.append(FLOWER)
            else:
                ij_pairs = make_ij_pairs(i, j, num_row, num_col)
                counter = 0
                for pair in ij_pairs:
                    if garden[pair[0]][pair[1]] == FLOWER:
                        counter += 1
                if counter == 0:
                    row.append(' ')
                else:
                    row.append(str(counter))
        output.append(''.join(row))
    
    return output

def valid_garden(garden):
    
    output = True
    
    validation = set(map(len, garden))
    
    if len(validation) != 1:
        output = False
        
    if output:
        valid_input = str.maketrans({' ': '', '*': ''})
        validation = sum(map(len, 
                             map(lambda x: str.translate(x, valid_input), garden)))
        if validation > 0:
            output = False
            
    return output

def annotate(garden):
    
    output = []
    
    if garden:
        if not valid_garden(garden):
            raise ValueError('The board is invalid with current input.')
        elif len(garden[0]) == 0:
            output = [''] * len(garden)
        else:
            output = make_num_garden(garden)
        
    return output

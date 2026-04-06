FLOWER = '*'

def flower_counter(row, column, garden):
    
    output = 0
    
    min_row = max(row - 1, 0)
    max_row = min(row + 2, len(garden))
    
    min_col = max(column - 1, 0)
    max_col = min(column + 2, len(garden[0]))
    
    for i in range(min_row, max_row):
        for j in range(min_col, max_col):
            if garden[i][j] == FLOWER:
                output += 1   
                
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
                flower_count = flower_counter(i, j, garden)
                if flower_count == 0:
                    row.append(' ')
                else:
                    row.append(str(flower_count))
        output.append(''.join(row))
    
    return output

def valid_garden(garden):
    
    output = True
        
    if len(set(map(len, garden))) != 1:
        output = False
        
    if output:
        valid_input = str.maketrans({' ': '', '*': ''})
        validation = sum(
            map(lambda x: len(str.translate(x, valid_input)), garden))
        if validation > 0:
            output = False
            
    return output

def annotate(garden):
    
    output = []
    
    if garden:
        if not valid_garden(garden):
            raise ValueError('The board is invalid with current input.')
        elif not garden[0]:
            output = [''] * len(garden)
        else:
            output = make_num_garden(garden)
        
    return output

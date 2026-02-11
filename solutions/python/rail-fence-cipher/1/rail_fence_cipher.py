def direction_set(row, rails):
    
    output = True
    
    if row == 0:
        output = True
    if row == rails - 1:
        output = False
        
    return output

def base_update(row, col, direction, rails):
    
    new_col = col + 1
    new_row = row
    
    new_direction = direction
    
    if new_row == 0 or new_row == rails - 1:
        new_direction = direction_set(new_row, rails)
    
    if new_direction:
        new_row += 1
    else:
        new_row -= 1
        
    return (new_row, new_col, new_direction)

def decode_update(row, col, main_row, direction, max_col, rails):
    
    new_row, new_col, new_direction = base_update(row, col, direction, rails)
                
    while new_row != main_row and new_col < max_col:

        new_row, new_col, new_direction = base_update(new_row, new_col, new_direction, rails)
        
    new_main = main_row
        
    if new_col >= max_col:
        new_main += 1
        new_row = new_main
        new_col = new_main
        new_direction = True
        
    return (new_row, new_col, new_direction, new_main)

def encode(message, rails):
    
    output = [[''] * len(message) for _ in range(rails)]
    
    direction = False
    col = 0
    row = 0
    
    for char in message:
        output[row][col] = char
        
        row, col, direction = base_update(row, col, direction, rails)
            
    output = ''.join(map(lambda x: ''.join(x), output))
    
    return output

def decode(encoded_message, rails):
    
    plaintext = [[''] * len(encoded_message) for _ in range(rails)]
    
    direction = False
    col = 0
    row = 0
    main_row = 0
    
    for char in encoded_message:
        plaintext[row][col] = char
        
        row, col, direction, main_row = decode_update(row, col, main_row, direction, len(encoded_message), rails)
    
    output = []
    
    direction = False
    col = 0
    row = 0
    
    while col < len(encoded_message):
        output.append(plaintext[row][col])
        
        row, col, direction = base_update(row, col, direction, rails)
            
    output = ''.join(output)
    
    return output

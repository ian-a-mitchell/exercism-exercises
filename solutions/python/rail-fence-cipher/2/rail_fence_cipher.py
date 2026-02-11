# finds the next step in the zig-zag
def next_step(row, col, direction, rails):
    
    new_col = col + 1
    new_row = row
    
    new_direction = direction
    
    if new_row == 0:
        new_direction = True
    elif new_row == rails - 1:
        new_direction = False
    
    if new_direction:
        new_row += 1
    else:
        new_row -= 1
        
    return (new_row, new_col, new_direction)

def build_indices(length, rails):
    
    indices = []
    
    row, col = 0, 0
    direction = True
    
    for _ in range(length):
        indices.append((row, col))
        row, col, direction = next_step(row, col, direction, rails)
        
    return indices

def fill_rails(message, indices, rails):
    
    output = make_rails(len(message), rails)
    
    for i, char in enumerate(message):
        row, col = indices[i]
        output[row][col] = char
        
    return output

def make_rails(length, rails):
    
    return [[''] * length for _ in range(rails)]

def rails_to_string(indices, full_rails):
    
    return ''.join(full_rails[row][col] for row, col in indices)

def encode(message, rails):
    
    indices = build_indices(len(message), rails)
    ciphertext = fill_rails(message, indices, rails)
    
    sorted_indices = sorted(indices, key = lambda index: (index[0], index[1]))
                
    return rails_to_string(sorted_indices, ciphertext)

def decode(encoded_message, rails):
    
    indices = build_indices(len(encoded_message), rails)
    sorted_indices = sorted(indices, key = lambda index: (index[0], index[1]))
    
    plaintext = fill_rails(encoded_message, sorted_indices, rails)
    
    return rails_to_string(indices, plaintext)

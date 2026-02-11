from string import ascii_uppercase

def rows(letter):
    
    key_index = ascii_uppercase.index(letter.upper())
    
    d = key_index * 2 + 1
    
    output = list(range(d))
    
    for i in output:
        row_element = []
        row_letter = ''
        
        if i <= key_index:
            row_letter = ascii_uppercase[i]
        else:
            row_letter = ascii_uppercase[d - i - 1]
            
        letter_index = ascii_uppercase.index(row_letter)
        pos_index = key_index + letter_index
        neg_index = key_index - letter_index
        
        for j in range(d):
            if j == neg_index or j == pos_index:
                row_element.append(row_letter)
            else:
                row_element.append(' ')
        
        output[i] = ''.join(row_element)
    
    return output

import string

UPPER_ALPHA = list(string.ascii_uppercase)
LOWER_ALPHA = list(string.ascii_lowercase)

def rotate_char(char, key):
    output = ''
    
    if char in UPPER_ALPHA:
        output = UPPER_ALPHA[(UPPER_ALPHA.index(char) + key) % 26]
    elif char in LOWER_ALPHA:
        output = LOWER_ALPHA[(LOWER_ALPHA.index(char) + key) % 26]
    else:
        output = char
        
    return output

def rotate_word(word, key):
            
    return ''.join([rotate_char(char, key) for char in word])

def rotate(text, key):

    output = [rotate_word(word, key) for word in text.split()]
    
    if len(output) == 1:
        output = ''.join(output)
    else:
        output = ' '.join(output)
    
    return output

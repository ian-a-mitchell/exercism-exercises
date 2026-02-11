import string
from math import sqrt

def normalize(plain_text):
    
    translate_table = {k: '' for k in string.punctuation}
    translate_table = translate_table | {k: '' for k in string.whitespace}
    
    normalized_text = str.translate(plain_text, str.maketrans(translate_table))
    normalized_text = normalized_text.lower()
    
    return normalized_text

def calc_c(l):
        
    c = int(sqrt(l))
    r = c
    
    if c * r < l:
        c += 1
        
    if c * r < l:
        r += 1
    
    return (c, r)

def new_row(normal_text, i, c, r, pad):
    
    output = ''
    
    if ((i + 1) * c) < len(normal_text):
        start = i * c
        stop = (i + 1) * c
        output = normal_text[start:stop]
    else:
        start = i * c
        output = normal_text[start:] + pad
        
    return output
    

def cipher(normal_text):
    
    c, r = calc_c(len(normal_text))
        
    pad = ''.join([' '] * (c * r - len(normal_text)))
    
    square = [new_row(normal_text, i, c, r, pad) for i in range(0, r)]
            
    output = [''.join([row[i] for row in square]) for i in range(0, c)]
    
    return ' '.join(output)

def cipher_text(plain_text):
    
    output = normalize(plain_text)
    
    if output:
        output = cipher(output)
    
    return output
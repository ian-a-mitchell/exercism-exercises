import string
import re

def code_create():
    
    output = {}
    
    for i, x in enumerate(string.ascii_lowercase):
        output[x] = string.ascii_lowercase[-(i + 1) % 26]
        
    return output

def cipher_pad(cipher_text):
    
    output = list(cipher_text)
    
    i = 0
    count = 0
    
    while i < len(output):
        if count == 5:
            output.insert(i, ' ')
            count = 0
        else:
            count = count + 1
        i = i + 1
    
    return ''.join(output)

def code(text):
    
    stripped = re.sub(r'\W', '', text.lower())
            
    coded_text = stripped.translate(str.maketrans(code_create()))
    
    return coded_text
        

def encode(plain_text):
                    
    cipher_text = cipher_pad(code(plain_text))
    
    return cipher_text

def decode(ciphered_text):
    
    plain_text = code(ciphered_text)
    
    return plain_text

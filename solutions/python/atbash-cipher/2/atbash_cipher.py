from string import ascii_lowercase
from re import sub

KEY = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def cipher_pad(cipher_text):
    
    output = ' '.join(cipher_text[i:i+5] for i in range(0, len(cipher_text), 5))
    
    return output

def code(text):
                
    coded_text = sub(r'\W', '', text.lower()).translate(KEY)
    
    return coded_text  

def encode(plain_text):
                    
    cipher_text = cipher_pad(code(plain_text))
    
    return cipher_text

def decode(ciphered_text):
    
    plain_text = code(ciphered_text)
    
    return plain_text

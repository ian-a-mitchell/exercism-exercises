from itertools import groupby
from re import sub

def group_con(key, group):
    
    size = len(list(group))
    
    return key if size == 1 else str(size) + key
        
def decode(encoded):
    
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), encoded)

def encode(string):
        
    return ''.join([group_con(key, group) for key, group in groupby(string)])

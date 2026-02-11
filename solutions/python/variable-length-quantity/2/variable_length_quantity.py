from functools import reduce
from operator import concat

BYTE_LENGTH = 7

VALUE_MASK = 0b1111111
CONTINUE_MASK = 1<<7


def proc_byte(value):
                
    return value & VALUE_MASK

def encode_single_value(value):
    
    output = [0x00]
    
    if value:
        output[0] = proc_byte(value)
        value = value >> BYTE_LENGTH
        
        while value:
            output.append(CONTINUE_MASK | proc_byte(value))
            value = value >> BYTE_LENGTH
        
    return output[::-1]

def encode(numbers):
    
    output = reduce(concat, map(encode_single_value, numbers))
    
    return output

def decode(bytes_):
    
    output = []
    next_value = 0
    terminal = not (CONTINUE_MASK & bytes_[0])
    
    for byte in bytes_:
        terminal = not (CONTINUE_MASK & byte)
        next_value = (next_value << BYTE_LENGTH) | (proc_byte(byte))
        
        if terminal:
            output.append(next_value)
            next_value = 0
            
    if not terminal:
        raise ValueError('incomplete sequence')
    
    return output
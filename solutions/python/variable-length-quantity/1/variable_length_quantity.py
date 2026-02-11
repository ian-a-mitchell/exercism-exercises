from functools import reduce
from operator import concat

BYTE_LENGTH = 7
TERMINAL_BASE = 0x00
MID_BASE = 0x01

MID_BYTE = 0b10000000


def proc_byte(value):
    byte = 0x00

    for i in range(BYTE_LENGTH - 1, -1, -1):
        byte = (byte << 1) | ((value >> i) & 1)
            
    return byte

def encode_single_value(value):
    
    output = [TERMINAL_BASE]
    
    if value:
        output[0] = proc_byte(value)
        value = value >> BYTE_LENGTH
        
        while value:
            next_byte = (MID_BASE << BYTE_LENGTH) | proc_byte(value)
            output.append(next_byte)
            value = value >> BYTE_LENGTH
        
    return output[::-1]

def encode(numbers):
    
    output = reduce(concat, map(encode_single_value, numbers))
    
    return output

def decode(bytes_):
    
    output = []
    next_value = 0
    terminal = not (MID_BYTE & bytes_[0])
    
    for byte in bytes_:
        terminal = not (MID_BYTE & byte)
        next_byte = proc_byte(byte)
        next_value = (next_value << BYTE_LENGTH) | (next_byte)
        
        if terminal:
            output.append(next_value)
            next_value = 0
            
    if not terminal:
        raise ValueError('incomplete sequence')
    
    return output
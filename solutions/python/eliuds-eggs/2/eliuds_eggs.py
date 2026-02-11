def egg_count(display_value):
    
    output = 0
        
    while display_value > 0:
        output += display_value & 1      
        display_value >>= 1
    
    return output
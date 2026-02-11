def egg_count(display_value):
    
    output = 0
        
    while display_value > 0:
        if display_value & 1 == 1:
            output += 1         
        display_value = display_value >> 1
    
    return output
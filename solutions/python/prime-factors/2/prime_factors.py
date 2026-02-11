def factors(value):
    
    output = []
    factor = 2
    
    while factor * factor <= value:
        if value % factor:
            factor += 1
        else:
            output.append(factor)
            value //= factor
            
    if value > 1: 
        output.append(value)
        
    return output
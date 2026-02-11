ACTIONS = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(binary_str):
    
    bin_num = int(binary_str, base = 2)
    
    output = []
    
    for i, j in enumerate(ACTIONS):
        if bin_num & 1 << i:
            output.append(j)
            
    if bin_num & 1 << 4:
        output = output[::-1]
        
    return output
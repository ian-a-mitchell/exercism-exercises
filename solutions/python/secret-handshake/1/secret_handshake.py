ACTIONS = {
    -4: 'jump',
    -3: 'close your eyes',
    -2: 'double blink',
    -1: 'wink'
}

def commands(binary_str):
    
    output = []
    
    for i in range(-1, -5, -1):
        if binary_str[i] == '1':
            output.append(ACTIONS[i])
            
    if binary_str[0] == '1':
        output = output[::-1]
        
    return output
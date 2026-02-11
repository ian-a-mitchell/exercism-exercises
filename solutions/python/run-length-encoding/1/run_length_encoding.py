def mini_encode(count, char):
    
    return [char] if count == 1 else [str(count), char]

def mini_decode(encoded, i):
    
    output = []
    
    j = 1
    while i + j < len(encoded) and encoded[i + j].isdigit():
        j = j + 1
        
    output = ([encoded[i + j] * int(encoded[i:i+j])], j + 1)
    
    return output
        
def decode(encoded):
    
    output = []
    
    i = 0
    while i < len(encoded):
        char = encoded[i]
        if char.isdigit():
            step = mini_decode(encoded, i)
            output.extend(step[0])
            i = i + step[1]
        else:
            output.append(char)
            i = i + 1
    
    return ''.join(output)

def encode(decoded):
    
    output = []
    
    i = 0
    while i < len(decoded):
        char = decoded[i]
        count = 1
        while i + count < len(decoded) and decoded[i + count] == char:
            count = count + 1
        output.extend(mini_encode(count, char))
        i = i + count
    
    return ''.join(output)

RESCOL = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

MAX_LENGTH = 2

def value(colors):
    output_list = []
    
    for color in colors:
        if len(output_list) < 2:
            output_list.append(RESCOL[color])
            
    return int(''.join(map(str, output_list)))

RESCODE = {
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

PREFIXES = {
    0: '',
    3: 'kilo',
    6: 'mega',
    9: 'giga',
}

def reduce_and_prefix(value):
    num_zeroes = len(str(value)) - len(str(value).rstrip('0'))
    
    prefix = ''
    power = 0
    
    for key in PREFIXES.keys():
        if num_zeroes >= key:
            prefix = PREFIXES[key]
            power = 10**key
    
    return (int(value / power), prefix)
    

def label(colors):
    first_digits = int(''.join([str(RESCODE[color]) for color in colors[:2]]))
    
    value = reduce_and_prefix(first_digits * 10**RESCODE[colors[2]])
                
    return f"{value[0]} {value[1] + 'ohms'}"

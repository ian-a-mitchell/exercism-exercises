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
    9: 'giga'
}

def label(colors):
    first_digits = int(''.join([str(RESCODE[color]) for color in colors[:2]]))
    power = RESCODE[colors[2]]
    
    value = first_digits * 10**power
    
    num_zeroes = len(str(value)) - len(str(value).rstrip('0'))
    
    prefix = ''
    
    for key in PREFIXES.keys():
        if num_zeroes >= key:
            prefix = PREFIXES[key]
            power = 10**key
    
    value = int(value / power)
                
    return f"{value} {prefix + 'ohms'}"

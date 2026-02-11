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

TOLCODE = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10,
}

PREFIXES = {
    0: '',
    3: 'kilo',
    6: 'mega',
    9: 'giga',
    12: 'tera',
    15: 'peta',
    18: 'exa',
    21: 'zetta',
    24: 'yotta',
    27: 'ronna',
    30: 'quetta'
}

def reduce_and_prefix(value):
    prefix = ''
    power = 0
    
    for key in PREFIXES.keys():
        if value / 10**key >= 1:
            prefix = PREFIXES[key]
            power = 10**key
    
    return (value / power, prefix)

def color_parse(colors):
    
    tolerance = TOLCODE[colors[-1]]
    first_digits = int(''.join([str(RESCODE[color]) for color in colors[0:-2:1]]))
    zeroes = RESCODE[colors[-2]]
    
    return (first_digits, zeroes, tolerance)
    

def resistor_label(colors):
    
    first_digits = 0
    zeroes = 0
    tolerance = 0
    
    value = 0
    prefix = ''
    
    if len(colors) > 3:
        first_digits, zeroes, tolerance = color_parse(colors)
        value, prefix = reduce_and_prefix(first_digits * 10**zeroes)
    
    if(int(value) == value):
        value = int(value)
        
    output = ''
    
    if len(colors) > 3:
        output = f"{value} {prefix}ohms ±{tolerance}%"
    else:
        output = f"{value} ohms"
        
    return output
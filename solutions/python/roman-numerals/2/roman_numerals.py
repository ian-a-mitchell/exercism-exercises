TRANS = {
    1000: 'M',
    900: 'CM',
    500: 'D',  
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def roman(number):
    
    output = []
    
    for k in TRANS:
        while number - k >= 0:
            output.append(TRANS[k])
            number = number - k
    
    return ''.join(output)
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

def roman(n):
    
    output = []
    
    for k, syb in TRANS.items():
        while n - k >= 0:
            output.append(syb)
            n = n - k
    
    return ''.join(output)
MIN_BASE = 2

def list_to_num(input_base, digits):
    
    output = 0
    
    for i in range(len(digits)):
        digit = digits[i]
        if digit < 0 or digit > (input_base - 1):
            raise ValueError('all digits must satisfy 0 <= d < input base')
        output += digit * input_base**(len(digits) - 1 - i)
        
    return output

def num_to_list(output_base, num):
    
    output = []
    max_power = 1
    
    while num % output_base**max_power != num:
        max_power += 1
    
    max_power -= 1
    
    while max_power > 0:
        digit = num // output_base**max_power
        num = num % output_base**max_power
        output.append(digit)
        max_power = max_power - 1
        
    output.append(num)
    
    return output

def rebase(input_base, digits, output_base):
    
    if input_base < MIN_BASE:
        raise ValueError('input base must be >= 2')
    
    if output_base < MIN_BASE:
        raise ValueError('output base must be >= 2')
        
    b10 = list_to_num(input_base, digits)
    
    return num_to_list(output_base, b10)

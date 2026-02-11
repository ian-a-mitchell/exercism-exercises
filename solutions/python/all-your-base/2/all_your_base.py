MIN_BASE = 2

def list_to_num(input_base, digits):
        
    return sum(d*input_base**i for i,d in enumerate(digits[::-1]))

def num_to_list(output_base, num):
    
    output = []
    
    if num == 0:
        output = [0]
    else:
        while num != 0:
            output.insert(0, num % output_base)
            num = num // output_base
    
    return output

def rebase(input_base, digits, output_base):
    
    if input_base < MIN_BASE:
        raise ValueError('input base must be >= 2')
    
    if output_base < MIN_BASE:
        raise ValueError('output base must be >= 2')
        
    if any(d < 0 for d in digits) or any(d >= input_base for d in digits):
        raise ValueError('all digits must satisfy 0 <= d < input base')
        
    b10 = list_to_num(input_base, digits)
    
    return num_to_list(output_base, b10)

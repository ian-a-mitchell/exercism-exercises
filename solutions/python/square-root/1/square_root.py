# Calculate the square root of the provided number.
# Only intended to work with perfect squares.

def power(number, exponent):
    
    output = 1
    
    for exp in range(0, exponent):
        output = output * number
        
    return output

def natural_root(number, exponent):
    
    upper = number // 2
    lower = 1
    
    root = 1
    
    while lower <= upper and lower <= number // 2:
        
        mid = (lower + upper) // 2
        
        if power(mid, exponent) > number:
            upper = mid - 1
        elif power(mid, exponent) < number:
            lower = mid + 1
        else:
            root = mid
            lower = upper + 1
            
    if power(root, exponent) != number:
        raise ValueError(f"{number} does not have a natural {exponent} root")
        
    return root

def square_root(number):
    
    return natural_root(number, 2)
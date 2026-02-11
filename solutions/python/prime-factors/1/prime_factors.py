# Uses trial division because it's conceptually simple to implement
# and numbers at hand will mostly not be large
# A better algorithm would help
# For natural numbers *only*
def is_prime(n):
    
    if n == 1:
        return False  
        
    f_max = int(n ** 0.5) + 1
    
    if f_max > 2:
        for i in range(2, f_max):
            if n % i == 0:
                return False
            
    return True

def factors(value):
    
    if value < 2:
        return []
        
    if is_prime(value):
        return [value]
    else:
        p_max = int(value ** 0.5) + 1
        for i in range(2, p_max):
            if is_prime(i) and value % i == 0:
                return [i] + factors(value // i)
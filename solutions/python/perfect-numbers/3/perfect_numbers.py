def factorization(number):
    """ Given a whole number, returns a list containing its factors.
        
    Uses trial division despite being inefficient due to ease of understanding.
    
    :param number: int a positive integer
    :return: list containing factors of number
    """
    
    output = [1] # All integers are divisible by one
    
    if number > 1:
        for divisor in range(2, number + 1):
            if number % divisor == 0:
                output.append(divisor)    
    
    return output

def aliquot_sum(number):
    """ Given a positive integer, returns its aliquot sum, that is, the sum
    of its divisors other than itself.
    
    :param number: int a positive integer
    :return: int the aliquot sum of that number
    """
    
    return sum(factorization(number)) - number

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1 or not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")
        
    x = aliquot_sum(number) - number
    
    output = "perfect"
    if (x < 0 or number == 1):
        output = "deficient"
    elif x > 0:
        output = "abundant"
    
    return output

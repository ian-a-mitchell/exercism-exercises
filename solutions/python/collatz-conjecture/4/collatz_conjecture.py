def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    
    n = number / 2 if number % 2 == 0 else number * 3 + 1
    
    return 1 + steps(n)

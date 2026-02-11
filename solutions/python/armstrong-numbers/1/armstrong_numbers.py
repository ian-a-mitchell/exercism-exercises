def is_armstrong_number(number):
    num = [int(x) for x in str(number)]
    k = len(num)
    
    num = sum([x**k for x in num])
        
    return num == number
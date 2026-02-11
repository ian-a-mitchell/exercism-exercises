def collatz(n, step):
    if n == 1:
        return step
    
    even = n % 2 == 0
        
    return collatz(n / 2, step + 1) if even else collatz(n * 3 + 1, step + 1)

def steps(number):
    return collatz(number, 0)

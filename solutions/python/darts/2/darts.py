SCORES = {
    100: 1,
    25: 5,
    1: 10
}

def score(x, y):
    rsq = x**2 + y**2
            
    points = 0
    
    for index in SCORES:
        if rsq <= index:
            points = SCORES[index]
            
    return points
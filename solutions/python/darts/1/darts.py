SCORE_RADII = {
    1: 5,
    5: 1,
    10: 0
}

def score(x, y):
    radsq = x**2 + y**2
            
    points = 10
    
    for index in SCORE_RADII:
        if radsq > index**2:
            points = SCORE_RADII[index]
            
    return points
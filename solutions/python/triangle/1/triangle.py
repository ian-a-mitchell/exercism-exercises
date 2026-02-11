def is_degenerate(sides):
    degenerate = False
    
    if(len(sides) != 3):
        degenerate = True
    else:
        a = sides[0]
        b = sides[1]
        c = sides[2]
        
        ab = (a + b) >= c
        ac = (a + c) >= b
        bc = (b + c) >= a
        
        abc = (a > 0) and (b > 0) and (c > 0)
        
        degenerate = ab and ac and bc and abc
        
    return degenerate

def equilateral(sides):
    
    equilateral = True
    
    if is_degenerate(sides):
        equilateral = False
    else:
        a = sides[0]
        b = sides[1]
        c = sides[2]
        
        if (a != b) or (b != c) or (a != c):
            equilateral = False
            
    return equilateral


def isosceles(sides):
    
    isosceles = True
    
    if is_degenerate(sides):
        isosceles = False
    else:
        a = sides[0]
        b = sides[1]
        c = sides[2]
        
        if (a != b) and (b != c) and (a != c):
            isosceles = False
        
    return isosceles


def scalene(sides):
    
    scalene = True
    
    if is_degenerate(sides):
        scalene = False
    else:
        scalene = not isosceles(sides)
        
    return scalene
    

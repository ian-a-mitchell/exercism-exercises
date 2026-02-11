def is_valid(sides):
    valid = True
    
    if(len(sides) != 3):
        valid = False
    else:        
        valid = (2 * max(sides) < sum(sides)) and all(sides)
        
    return valid

def equilateral(sides):
            
    return is_valid(sides) and len(set(sides)) == 1


def isosceles(sides):
        
    return is_valid(sides) and len(set(sides)) < 3


def scalene(sides):
            
    return is_valid(sides) and len(set(sides)) == 3
    

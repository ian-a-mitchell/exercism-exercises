def is_valid(sides):
    return len(sides) == 3 and (2 * max(sides) < sum(sides)) and all(sides)

def equilateral(sides):
    return is_valid(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_valid(sides) and len(set(sides)) < 3


def scalene(sides):
    return is_valid(sides) and len(set(sides)) == 3
    

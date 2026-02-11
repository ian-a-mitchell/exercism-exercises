import itertools

MAX = {
       1: 9,
       2: 17,
       3: 24,
       4: 30,
       5: 35,
       6: 39,
       7: 42,
       8: 44,
       9: 45
}
MIN = {
       1: 1,
       2: 3,
       3: 6,
       4: 10,
       5: 15,
       6: 21,
       7: 28,
       8: 36,
       9: 45
}

def combinations(target, size, exclude):
    
    if size > 9 or size < 1:
        raise ValueError('size is not possible')
    if target > MAX[size] or target < MIN[size]:
        raise ValueError('target value is not possible')
        
    available = [i for i in range(1, min(target, 9) + 1) if i not in exclude]
        
    output = [list(x) 
              for x in itertools.combinations(available, size) 
              if sum(x) == target]
                    
    if not output:
        raise ValueError('no valid solutions found')
                        
    return output

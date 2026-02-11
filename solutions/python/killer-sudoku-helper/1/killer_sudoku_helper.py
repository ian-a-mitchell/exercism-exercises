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

def solve(target, size, exclude):
        
    available = [digit for digit in range(1, 10) if digit not in exclude]
                    
    output = []
    
    valid_target = target <= MAX[size] and target >= MIN[size]
    
    if valid_target:
        if size == 1 and target not in exclude:
            output = [target]
        elif size > 1:
            for digit in available:
                new_exclude = exclude + [digit]
                candidate = [digit] + solve(target - digit, size - 1, new_exclude)
                if len(candidate) == size:
                    output = candidate
                    break
                
    return output

def combinations(target, size, exclude):
    
    if size > 9 or size < 1:
        raise ValueError('size is not possible')
    if target > MAX[size] or target < MIN[size]:
        raise ValueError('target value is not possible')
        
    available = [digit for digit in range(1, 10) if digit not in exclude]
        
    output = []
        
    if size == 1 and target not in exclude:
        output.append([target])
    elif size > 1:
        for digit in available:
            new_exclude = exclude + [digit]
            candidate = [digit] + solve(target - digit, size - 1, new_exclude)
            candidate.sort()
            if len(candidate) == size:
                try:
                    output.index(candidate)
                except ValueError:
                    output.append(candidate)
                    
    if not output:
        raise ValueError('no valid solutions found')
                        
    return output

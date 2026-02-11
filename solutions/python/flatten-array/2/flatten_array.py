def is_valid_iterable(x):
    try:
        iter(x)
        if not isinstance(x, str):
            return True
    except TypeError:
        return False
    
    return False

def flatten(iterable):
    
    output = []
    
    for x in iterable:
        if is_valid_iterable(x):
            output = output + flatten(x)
        else:
            output.append(x)
            
    output = list(filter(lambda x: x is not None, output))
        
    return output

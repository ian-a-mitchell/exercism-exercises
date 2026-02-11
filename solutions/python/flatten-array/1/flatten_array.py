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
        if x is None:
            pass
        elif not is_valid_iterable(x):
            output.append(x)
        else:
            output = output + flatten(x)
        
    return output

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
            output.extend(flatten(x))
        elif x is not None:
            output.append(x)
                    
    return output

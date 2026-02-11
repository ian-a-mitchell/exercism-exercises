def validate(series, length):
    errors = {
        'not series': 'series cannot be empty',
        'length == 0': 'slice length cannot be zero',
        'length < 0': 'slice length cannot be negative',
        'length > len(series)': 'slice length cannot be greater than series length'
    }
    
    for expression in errors:
        if eval(expression):
            raise ValueError(errors[expression])

def slices(series, length):
    
    validate(series, length)
    
    return [series[i:i + length] for i in range(len(series) - length + 1)]
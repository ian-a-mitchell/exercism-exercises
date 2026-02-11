from functools import reduce

def sub_series(series, size):
    
    length = len(series)
    
    return (series[i:i + size] for i in range(length) if i + size <= length)

def string_product(input_string):
    
    output = reduce(lambda x, y: x * y, map(lambda x: int(x), input_string))
    
    return output

def largest_product(series, size):
    
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if not series.isdecimal():
        raise ValueError("digits input must only contain digits")
            
    return max(map(string_product, sub_series(series, size)))
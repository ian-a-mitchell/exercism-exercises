def is_valid_iterable(x):
    try:
        iter(x)
        if not isinstance(x, str):
            return True
    except TypeError:
        return False
    
    return False

def append(list1, list2):
    
    output = list(range(0, length(list1) + length(list2), 1))
    
    for i in output:
        if i < length(list1):
            output[i] = list1[i]
        else:
            output[i] = list2[i - length(list1)]
            
    return output

def concat(lists):
    
    output = []
    
    for x in lists:
        if is_valid_iterable(x):
            output = append(output, x)
        elif x is not None:
            output = append(output, [x])
                    
    return output


def filter(function, list):
    
    output = []
    
    for x in list:
        if function(x):
            if is_valid_iterable(x):
                output = append(output, x)
            elif x is not None:
                output = append(output, [x])
                
    return output


def length(list):
    
    output = 0
    
    for x in list:
        output += 1
        
    return output


def map(function, list):
    
    output = []
    
    for x in list:
        y = function(x)
        if is_valid_iterable(y):
            output = append(output, y)
        elif y is not None:
            output = append(output, [y])
                
    return output


def foldl(function, list, initial):
    
    output = initial
    
    if list:
        output = foldl(function, list[1:], function(initial, list[0]))
    
    return output


def foldr(function, list, initial):
    
    output = initial
    
    if list:
        output = function(foldr(function, list[1:], initial), list[0])
    
    return output


def reverse(list):
    
    output = []
    
    if list:
        i = length(list) - 1
        while i > -1:
            output = append(output, [list[i]])
            i = i - 1
        
    return output

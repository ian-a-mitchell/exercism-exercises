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
    
    if lists:
        if is_valid_iterable(lists[0]):
            output = append(append(output, lists[0]), concat(lists[1:]))
        else:
            output = append(append(output, [lists[0]]), concat(lists[1:]))
                    
    return output


def filter(function, list):
    
    output = []
    
    if list:
        if function(list[0]):
            output = append(append(output, [list[0]]), filter(function, list[1:]))
        else:
            output = append(output, filter(function, list[1:]))
                
    return output


def length(list):
    
    output = 0
    
    if list:
        output = 1 + length(list[1:])
        
    return output


def map(function, list):
    
    output = []
    
    if list:
        output = append([function(list[0])], map(function, list[1:]))
                
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
        output = append([list[-1]], reverse(list[0:-1]))
        
    return output

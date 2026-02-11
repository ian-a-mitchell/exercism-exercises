def find(search_list, value):
    lower_guard = 0
    upper_guard = len(search_list)
    
    output = 0
    
    while search_list and lower_guard < upper_guard:        
        mid_index = (upper_guard - lower_guard) // 2 + lower_guard
        
        if mid_index == lower_guard or mid_index == upper_guard:
            lower_guard = upper_guard = mid_index
        
        if search_list[mid_index] > value:
            upper_guard = mid_index
        elif search_list[mid_index] < value:
            lower_guard = mid_index
        else:
            output = mid_index
            lower_guard = upper_guard = mid_index
            
    if search_list and (search_list[lower_guard] == value):
        output = lower_guard
    else:
        raise ValueError("value not in array")
        
    return output
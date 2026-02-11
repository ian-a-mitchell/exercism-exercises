def find(search_list, value):
    
    if not search_list:
        raise ValueError("value not in array")
    
    first = 0
    last = len(search_list)
    
    output = 0
    
    while first <= last and first < len(search_list):        
        mid = (first + last) // 2
                
        if search_list[mid] > value:
            last = mid - 1
        elif search_list[mid] < value:
            first = mid + 1
        else:
            output = mid
            first = last + 1
                
    if not (search_list[output] == value):
        raise ValueError("value not in array")
        
    return output
def spiral_matrix(size):
    
    output = []
    if not size:
        return output
    
    for i in range(size):
        output.append([0]*size)
        
    row = 0
    column = 0
    rowise = True
    increase = True
    shift = 0
        
    for num in range(1, size**2 + 1):
        output[row][column] = num
        
        if rowise and increase:
            column += 1
        elif rowise and not increase:
            column -= 1
        elif not rowise and increase:
            row += 1
        elif not rowise and not increase:
            row -= 1
            
        if row == shift and column == size - 1 - shift:
            rowise = not rowise
        elif row == size - 1 - shift and column == size - 1 - shift:
            rowise = not rowise
            increase = not increase
        elif column == shift and row == size - 1 - shift:
            rowise = not rowise
        elif column == shift and row == shift + 1 and not (row == 0 and column == 0):
            rowise = not rowise
            increase = not increase
            shift += 1
        
    return output

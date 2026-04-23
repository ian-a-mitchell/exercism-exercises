""" Method for solving the Exercism "Transpose" problem. """
def transpose(text: str) -> str:
    """
    Transposes a string as if it were a matrix where each line corresponds to
    a row.

    Parameters
    ----------
    text : str
        The string to be transposed.

    Returns
    -------
    str
        The transposed string.
    """
    
    output = []
    
    split_text = text.split("\n")
    
    # The number of new rows/lines is equal to the length of the longest 
    # row/line in the original string.
    num_new_rows = len(max(split_text, key=len))
    
    for idx in range(num_new_rows):
        new_row = []
        for row_idx, row in enumerate(split_text):
            if idx < len(row):
                new_row.append(row[idx])
            else:
                max_future_length = len(max(split_text[row_idx:], key=len))
                if max_future_length > idx:
                    # A future column will have a "real" character, so we
                    # should go ahead and pad here.
                    new_row.append(" ")
                
        new_row = "".join(new_row)
       
        output.append(new_row)
    
    return "\n".join(output)

def is_isogram(string):
    reduced_string = [char for char in string.lower() if char.isalpha()]
    
    return len(set(reduced_string)) == len(reduced_string)

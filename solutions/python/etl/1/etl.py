def transform(legacy_data):
    
    output = {}
    
    for point, letters in legacy_data.items():
        for letter in letters:
            output[letter.lower()] = point
    
    return output
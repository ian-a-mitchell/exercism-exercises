from string import punctuation

def abbreviate(words):
    
    trans = str.maketrans({k:(' ' if k in ['-', '_'] else '')
                           for k in punctuation})
    
    output = ''.join([word[0] for word in
                      words.translate(trans).upper().split()])
            
    return output
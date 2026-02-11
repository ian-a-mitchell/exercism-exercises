from string import punctuation

def abbreviate(words):
    
    trans_table = {k:'' for k in punctuation}
    trans_table['_'] = ' '
    trans_table['-'] = ' '
    
    output = words.translate(str.maketrans(trans_table)).upper().split()
    
    output = ''.join([word[0] for word in output])
    
    return output
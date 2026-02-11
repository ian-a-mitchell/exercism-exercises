from string import punctuation
from functools import reduce

def abbreviate(words):
    
    exceptions = {
        '-': ' ',
        '_': ' ',
        '&': ' AND ',
        '@': ' AT '
    }
    
    trans = str.maketrans({k:(exceptions[k] if k in exceptions else '')
                           for k in punctuation})
        
    output = reduce(lambda start, word: start + word[0],
                    words.translate(trans).upper().split(), '')
            
    return output
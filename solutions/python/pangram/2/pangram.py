from string import ascii_lowercase

def is_pangram(sentence):   
    return set(ascii_lowercase).issubset(sentence.lower())

import string

def is_pangram(sentence):
    reduced_sentence = [char for char in sentence.lower() if char.isalpha()]
    
    return set(reduced_sentence) == set(string.ascii_lowercase)

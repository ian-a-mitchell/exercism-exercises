def non_match(word, candidate):
    
    return word.casefold() != candidate.casefold()

def char_match(word, candidate):
    
    return sorted(word.casefold()) == sorted(candidate.casefold())

def is_anagram(word, candidate):
    
    return non_match(word, candidate) and char_match(word, candidate)

def find_anagrams(word, candidates):
        
    return list(filter(lambda x: is_anagram(word, x), candidates))
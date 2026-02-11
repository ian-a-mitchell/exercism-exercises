def non_match(word, candidate):
    
    return str.lower(word) != str.lower(candidate)

def char_match(word, candidate):
    
    return sorted(list(str.lower(word))) == sorted(list(str.lower(candidate)))

def is_anagram(word, candidate):
    
    return non_match(word, candidate) and char_match(word, candidate)

def find_anagrams(word, candidates):
        
    return list(filter(lambda x: is_anagram(word, x), candidates))
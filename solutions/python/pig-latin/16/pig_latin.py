VOWELS = ('a', 'e', 'i' ,'o', 'u')

R3_TRIGGER = ('qu',)
R4_TRIGGER = ('y',)

def vowel_start(word):    
    r1_triggers = ('xr', 'yt')
    return word.startswith(VOWELS + r1_triggers)

def consonant_translate(word):
    x = 0
    
    for n in range(1, len(word)):
        if word[n:].startswith(VOWELS + R4_TRIGGER):
            x = n
            if(word[(n-1):].startswith(R3_TRIGGER)):
                x = n + 1
            break
    
    return word[x:] + word[0:x]
        
def word_translate(word):
    
    output = word
    
    if not vowel_start(word):
        output = consonant_translate(word)
    
    output += 'ay'
    
    return output

def translate(text):
    text = text.lower().split()
    
    output = ' '.join([word_translate(word) for word in text])
    
    return output
            
VOWELS = ('a', 'e', 'i' ,'o', 'u')

R3_TRIGGER = ('qu',)
R4_TRIGGER = ('y',)

def rule_1_check(word):    
    r1_triggers = ('xr', 'yt')
    return word.startswith(VOWELS + r1_triggers)

def rule_3_check(word):
    output = word.startswith(R3_TRIGGER)
    
    if not output:
        for n in range(1, len(word)):
            if word[n:].startswith(VOWELS + R4_TRIGGER):
                break
            elif word[n:].startswith(R3_TRIGGER):
                output = True
                break
    
    return output

def rule_2(word):
    x = 0
    
    for n in range(1, len(word)):
        if word[n:].startswith(VOWELS + R4_TRIGGER):
            x = n
            break
    
    return word[x:] + word[0:x]
    
def rule_3(word):
    x = 0
    
    for n in range(0, len(word)):
        if word[n:].startswith(R3_TRIGGER):
            x = n
            break
        
    return word[x+2:] + word[0:x+2]
        
def word_translate(word):
    
    output = word
    
    if not rule_1_check(word):
        if rule_3_check(word):
            output = rule_3(word)
        else:
            output = rule_2(word)
    
    output += 'ay'
    
    return output

def translate(text):
    text = text.lower().split()
    
    output = ' '.join([word_translate(word) for word in text])
    
    return output
            
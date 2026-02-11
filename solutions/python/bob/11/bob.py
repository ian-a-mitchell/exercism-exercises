OUTPUTS = ('Whatever.', 'Sure.', 'Whoa, chill out!',
            'Calm down, I know what I\'m doing!', 'Fine. Be that way!')

def response(hey_bob):
    stripped = hey_bob.rstrip()
    
    output_index = 0
        
    if not stripped:
        output_index = -1
    else:
        output_index += 2 if stripped.isupper() else 0
        output_index += 1 if stripped.endswith('?') else 0
    
    return OUTPUTS[output_index]

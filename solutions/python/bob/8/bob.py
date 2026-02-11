import string

outputs = {
    'default': 'Whatever.',
    'silent': 'Fine. Be that way!',
    'yell_q': 'Calm down, I know what I\'m doing!',
    'question': 'Sure.',
    'yell': 'Whoa, chill out!'
    }

def is_question(hey_bob):
    return hey_bob[-1] in ["?"]

def is_yelling(hey_bob):
    return hey_bob.isupper()

def is_silent(hey_bob):
    return not hey_bob

def response(hey_bob):
    del_map = str.maketrans('', '', string.whitespace)
    hey_bob = hey_bob.translate(del_map)
    
    output = outputs['default']
        
    if is_silent(hey_bob):
        output = outputs['silent']
    elif is_question(hey_bob) and is_yelling(hey_bob):
        output = outputs['yell_q']
    elif is_question(hey_bob):
        output = outputs['question']
    elif is_yelling(hey_bob):
        output = outputs['yell']
    
    return output

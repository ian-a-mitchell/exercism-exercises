import string

def is_question(hey_bob):
    return hey_bob[-1] in ["?"]

def is_yelling(hey_bob):
    return hey_bob.isupper()

def is_silent(hey_bob):
    return  hey_bob == ''

def response(hey_bob):
    del_map = str.maketrans('', '', string.whitespace)
    hey_bob = hey_bob.translate(del_map)
    
    if is_question(hey_bob) and is_yelling(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif is_question(hey_bob):
        return "Sure."
    elif is_yelling(hey_bob):
        return "Whoa, chill out!"
    elif is_silent(hey_bob):
        return "Fine. Be that way!"
    else:
        return "Whatever."

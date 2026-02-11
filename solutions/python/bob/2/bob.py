import re

def is_question(hey_bob):
    return hey_bob[-1] in ["?"]

def is_yelling(hey_bob):
    return hey_bob.isupper()

def is_silent(hey_bob):
    stripped = re.sub('\s', '', hey_bob)
    
    return stripped == ''

def response(hey_bob):
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

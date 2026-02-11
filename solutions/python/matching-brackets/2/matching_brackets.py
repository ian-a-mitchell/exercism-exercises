BRACKET_MAP = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def is_paired(input_string):
    
    brackets = []
    
    for x in input_string:
        if x in BRACKET_MAP.values():
            brackets.append(x)
        if x in BRACKET_MAP:
            if not brackets or (brackets.pop() != BRACKET_MAP[x]):
                return False
                
    return not brackets
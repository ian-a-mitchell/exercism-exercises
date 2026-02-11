import re
from string import punctuation

OPS = {
       'is': 'is',
       'by': '',
       'plus': '+',
       'minus': '-',
       'multiplied': '*',
       'divided': '/'
}

# Takes a string and returns a list of operators and numbers after validation
def parse_problem(question):
    
    mod_punctuation = punctuation.translate(str.maketrans({'-': ''}))    
    output = question.translate(str.maketrans({x:'' for x in mod_punctuation})).split()
    
    output = list(filter(None, [OPS[x] if x in OPS else x for x in output]))
        
    for i in range(len(output)):
        if output[i] in OPS:
            output = output[i:]
            break
        
    output = [numberfy(x) for x in output]
    
    validate(output)
    
    return output

def numberfy(input_string):
    
    num = input_string
    
    try: 
        num = int(num)
    except ValueError:
        num = input_string
        
    return num

def validate(parsed_input):
    
    for s in parsed_input:
        if not isinstance(s, int) and s not in OPS.values():
            raise ValueError('unknown operation')
            
    for i in range(len(parsed_input)):
        if parsed_input[i] in OPS.values() and parsed_input[i - 1] in OPS.values():
            raise ValueError('syntax error')
        elif isinstance(parsed_input[i], int) and isinstance(parsed_input[i - 1], int):
            raise ValueError('syntax error')

def execute(parsed_input):
    
    output = parsed_input[1]
    
    i = 2
    while i < len(parsed_input):
        output = eval(str(output) + parsed_input[i] + str(parsed_input[i + 1]))
        i += 2
    
    return output

def answer(question):
    
    parsed_input = parse_problem(question)
    
    output = execute(parsed_input)
    
    return output

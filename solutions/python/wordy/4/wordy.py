from string import punctuation
from operator import add, mul, sub
from operator import floordiv as div
from functools import reduce

OPS = {
       'What': '',
       'is': 'is',
       'by': '',
       'plus': add,
       'minus': sub,
       'multiplied': mul,
       'divided': div
}

# Takes a string and returns a list of operators and numbers after validation
def parse_problem(question):
    
    mod_punctuation = punctuation.translate(str.maketrans({'-': ''}))    
    output = question.translate(str.maketrans({x:'' for x in mod_punctuation})).split()
    
    output = list(filter(None, [OPS[x] if x in OPS else x for x in output]))
    
    output = list(map(numberfy, output))
            
    validate(output)
    
    return output

def numberfy(input_string):
    
    num = input_string
    
    try: 
        num = int(num)
    except:
        num = input_string
        
    return num

def validate(parsed_input):
        
    if list(filter(lambda x: not isinstance(x, int) and x not in OPS.values(), 
                   parsed_input)): 
        raise ValueError('unknown operation')
            
    for i in range(len(parsed_input)):
        if parsed_input[i] in OPS.values() and parsed_input[i - 1] in OPS.values():
            raise ValueError('syntax error')
        elif isinstance(parsed_input[i], int) and isinstance(parsed_input[i - 1], int):
            raise ValueError('syntax error')

def execute(parsed_input):
        
    nums = list(filter(lambda x: isinstance(x, int), parsed_input))
    ops = (x for x in parsed_input if x in OPS.values() and x != 'is')
    
    output = reduce(lambda x, y: next(ops)(x, y), nums)
    
    return output

def answer(question):
        
    output = execute(parse_problem(question))
    
    return output

from string import punctuation

OPS = {
       'What': '',
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
    
    test_input = list(map(numberfy, parsed_input))
    
    if list(filter(lambda x: not isinstance(x, int) and x not in OPS.values(), 
                   test_input)): 
        raise ValueError('unknown operation')
            
    for i in range(len(test_input)):
        if test_input[i] in OPS.values() and test_input[i - 1] in OPS.values():
            raise ValueError('syntax error')
        elif isinstance(test_input[i], int) and isinstance(test_input[i - 1], int):
            raise ValueError('syntax error')

def execute(parsed_input):
        
    output = int(parsed_input[1])
    
    for i in range(2, len(parsed_input), 2):
        output = eval(str(output) + parsed_input[i] + parsed_input[i + 1])
    
    return output

def answer(question):
        
    output = execute(parse_problem(question))
    
    return output

import re

OPENING = ("(", "[", "{")

CLOSING = {
    "(": ")",
    "[": "]",
    "{": "}"
}

# These two functions are from the "flatten list" exercise
def is_valid_iterable(x):
    try:
        iter(x)
        if not isinstance(x, str):
            return True
    except TypeError:
        return False
    
    return False

def flatten(iterable):
    
    output = []
    
    for x in iterable:
        if is_valid_iterable(x):
            output.extend(flatten(x))
        elif x is not None:
            output.append(x)
                    
    return output

# This function takes an input string and returns a list of strings that
# only includes the brackets specified in the problem statement: () [] {}
def strip_input(input_string):
    
    expr = re.compile(r"[\[\(\{\]\)\}]+")
    
    output = flatten([list(x) for x in expr.findall(input_string)])
    
    return output

# Given an input list starting with an opening bracket,
# this function then finds the list index of the matching closing bracket or,
# if there is no matching closing bracket, the length of the input list
def match_index(input_list):
    
    output = len(input_list)
    
    start_bracket = input_list[0]
    
    count = 1
    i = 1
    
    while i < len(input_list) and output == len(input_list):
        if input_list[i] == start_bracket:
            count = count + 1
        elif input_list[i] == CLOSING[start_bracket]:
            count = count - 1
            if count == 0:
                output = i
        i = i + 1
    
    return output

# This function actually does the analysis. Given the processed input list
# from strip_input it:
#   * Returns True if the list is empty;
#   * Returns False if the the first character is not an opening bracket;
#   * Returns False if the list has only a single character;
#   * Returns False if a matching closing bracket for the first bracket
#     could not be found by match_index;
#   * or returns the Boolean AND of the analysis of the sub-list of strings
#     contained within the matched brackets and the sub-list following the
#     closing bracket of the matched pair.
def pair_stripped(input_list):
    
    output = True
    
    if input_list:
        if input_list[0] not in OPENING:
            output = False
        elif len(input_list) == 1:
            output = False
        else:
            i = match_index(input_list)
            if i == len(input_list):
                output = False
            else:
                output = pair_stripped(input_list[1:i]) and pair_stripped(input_list[i+1:])
                
    return output

def is_paired(input_string):
    
    return pair_stripped(strip_input(input_string))

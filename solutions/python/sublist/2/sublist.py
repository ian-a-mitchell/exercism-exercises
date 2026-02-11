"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'Sublist'
SUPERLIST = 'Superlist'
EQUAL = 'Equal'
UNEQUAL = 'Unequal'

def check_subsets(long_list, short_list):
    n1 = len(long_list)
    n2 = len(short_list)
    
    return any(long_list[i:i+n2] == short_list for i in range(n1 - n2 + 1))

def sublist(list_one, list_two):
    
    output = UNEQUAL
    
    if list_one == list_two:
        output = EQUAL
    else:
        long_list = []
        short_list = []
        
        if len(list_one) > len(list_two):
            long_list = list_one
            short_list = list_two
        else:
            long_list = list_two
            short_list = list_one
            
        output = check_subsets(long_list, short_list)
        
        if output:
            if len(list_one) > len(list_two):
                output = SUPERLIST
            else:
                output = SUBLIST
        else:
            output = UNEQUAL
    
    return output

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

def sublist(list_one, list_two):
    
    output = UNEQUAL
    
    if not list_one or not list_two:
        if not list_one and not list_two:
            output = EQUAL
        elif not list_two:
            output = SUPERLIST
        else:
            output = SUBLIST
            
    if output == UNEQUAL:        
        long_list = []
        short_list = []
        
        if len(list_one) >= len(list_two):
            long_list = list_one
            short_list = list_two
        else:
            long_list = list_two
            short_list = list_one
            
        is_subset = False
            
        for i in range(len(long_list)):
            if long_list[i] == short_list[0] and len(long_list) - i >= len(short_list):
                for j in range(len(short_list)):
                    if long_list[i + j] == short_list[j]:
                        is_subset = True
                    else:
                        is_subset = False
                        break
                if is_subset:
                    break
                
        if is_subset:
            if len(list_one) == len(list_two):
                output = EQUAL
            elif long_list == list_one:
                output = SUPERLIST
            else:
                output = SUBLIST
    
    return output

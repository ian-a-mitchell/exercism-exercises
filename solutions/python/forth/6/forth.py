"""Contains classes and methods for solving the Exercism Forth exercise"""

import re
import inspect
from itertools import chain

class StackUnderflowError(Exception):
    """ A special exception class to report errors involving a Forth stack
    running out of values to supply to its operators.
    """
    
    def __init__(self: Exception, message: str):
        self.message = message
        
class ForthInterpreter:
    """
    A class that implements an interpreter for the subset of Forth used in the
    Exercism Forth exercise. Essentially, this can be divided into two parts:
        
        1: Static elements, corresponding to built-in commands and a handful
           of other methods and variables which do not depend on object state.
        2: Dynammic elements, corresponding to methods and variables which are
           modified by the user, particularly user-defined words.
           
    The basic approach is to initialize an object, using a list of user-defined
    words to create a translation table into the built-in commands. Then, the
    user may execute code by supplying a list of strings consisting of either
    numbers or words to the method "execute," which then handles
        
        1: Translating any user-defined words into their built-in counterparts;
        2: Converting any numerical strings into numbers;
        3: Calling the relevant methods to execute any commands.
        
    before returning a final list. Each object has the same built-ins, but the
    user-defined translation table may differ.
    """
    
    _SUFMSG = "Insufficient number of items in stack"
    
    # Effectively the translation table for built-ins.
    _OPERATORS = {
        "+": lambda x, y: [y + x],
        "-": lambda x, y: [y - x], 
        "*": lambda x, y: [y * x], 
        "/": lambda x, y: [y // x],
        "dup": lambda x: [x, x], 
        "drop": lambda _: [],
        "swap": lambda x, y: [x, y], 
        "over": lambda x, y: [y, x, y]
    }
    
    @staticmethod
    def _number_conversion(data: str) -> int:
        """Converts signed integers represented as strings into actual integers
        """
                    
        return -1 * int(data[1:]) if data[0] == "-" else int(data)
    
    _NUMBER_MATCH = re.compile(r"-?\d+")
    
    def __init__(self, user_defs: list[str]):
        """
        Creates a unique interpreter object including user-defined keywords to
        use when evaluating later supplied code/data stacks.

        Parameters
        ----------
        user_defs : list[str]
            A list of strings, each string corresponding to one attempted
            definition of a keyword.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if a definition is supplied .
        """
        
        self.translate = {}
                
        def_match = re.compile(r": [^ \t\n\r\f\v0-9]+ .+ ;")
        
        for definition in user_defs:
            if not def_match.match(definition):
                raise ValueError("illegal operation")
            
            working_def = definition[1:-1].split()
            word = working_def[0]
            working_def = working_def[1:]
            
            working_def = self._translate_stack(working_def)
            
            self.translate[word] = working_def
                
                
    def _translate_stack(self, stack: list[str]) -> list[str]:
        """
        Expands the stack with any user-defined translations.

        Parameters
        ----------
        stack : list[str]
            The raw stack, prior to numerical conversions.

        Returns
        -------
        list[str]
            A translated stack; all user-defined keywords have been replaced
            with their equivalents in the translation table. This may mean that
            the stack is longer due to the insertion of several values in place
            of one value at the location of the user-defined keyword.
        """
        
        return list(chain(*(self.translate[word] if word in self.translate
                            else [word] for word in stack)))
    
    def execute(self, stack: list[str]) -> list[int]:
        """
        Utilizing the built-in functions and user-defined word translations,
        executes the supplied stack.

        Parameters
        ----------
        stack : list[str]
            The stack to execute. Each string corresponds to either a numerical
            value; a built-in function; or a user-defined word translation.

        Returns
        -------
        list[str]
            The stack after:
                1: All user-defined translations have been executed;
                2: All numerical values have been converted into integers;
                3: All built-in functions have been executed.

        Raises
        ------
        ValueError
            ValueError is raised per spec if a keyword is used that does not
            correspond to either a user-defined translation or a built-in.
        """
        
        output = []
        
        stack = self._translate_stack(stack)
        
        for data in stack:
            if ForthInterpreter._NUMBER_MATCH.match(data):
                output.append(ForthInterpreter._number_conversion(data))
            elif data in ForthInterpreter._OPERATORS:
                built_in = ForthInterpreter._OPERATORS[data]
                param_num = len(inspect.signature(built_in).parameters)
                if len(output) < param_num:
                    raise StackUnderflowError(ForthInterpreter._SUFMSG)
                try:
                    output.extend(built_in(*(output.pop() 
                                       for param in range(param_num))))
                except ZeroDivisionError as exc:
                    raise ZeroDivisionError("divide by zero") from exc
            else:
                raise ValueError("undefined operation")
            
        return output

def evaluate(input_data: list[str]) -> list[int]:
    """
    Takes in a list of strings corresponding to user definitions, integer data,
    and "Forth" instructions, and processes them to put them all in a single
    case and separate out user definitions from the user-supplied stack of data
    and instructions. The former are used to build a unique Forth interpreter,
    which the latter is sent to for interpretation.

    Parameters
    ----------
    input_data : list[str]
        A list of strings. Each string that matches a certain pattern
        ": word def ;" corresponds to an (attempted) definition of a new word,
        while other strings are interpreted as stack contents.

    Returns
    -------
    list[int]
        A list of integers corresponding to the results of applying the
        words listed in the stack (including user-defined words) with the
        integers provided in the stack.
    """
    
    stack = []
    
    user_words = []
    
    possible_def = re.compile(r": .+ ;")
    
    for string in input_data:
        if possible_def.match(string):
            user_words.append(string.casefold())
        else:
            stack.extend(string.casefold().split())
    
    my_interpreter = ForthInterpreter(user_words)
    
    return my_interpreter.execute(stack)

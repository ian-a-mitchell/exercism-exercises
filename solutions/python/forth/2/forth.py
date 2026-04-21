"""Contains classes and methods for solving the Exercism Forth exercise"""

import re
import operator as op

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
    
    The static methods all use an identical input/output signature so that they
    can be agnostically executed by a single "_act" method when it comes
    across them in the code, using the _OPERATORS lookup table to select the
    correct method instead of requiring logic in the method itself.
    """
    
    _SUFMSG = "Insufficient number of items in stack"
    
    @staticmethod
    def _math_evaluate(operator, stack: list[int]) -> list[int]:
        """
        A method to evaluate an arithmetic operator on the top two values of a
        Forth stack. All of the arithmetic functions require substantially the
        same "back-end" code, so having a method they can call to do the actual
        work reduces code duplication.

        Parameters
        ----------
        operator : operator
            The arithmetic operator to apply to the stack.
        stack : list[int]
            A list of integers to apply the operator to.

        Returns
        -------
        list[int]
            The stack after applying the operator.

        Raises
        ------
        ZeroDivisionError
            Error raised if the division operator is provided and the top of
            the stack (the divisor) is zero, i.e. an attempt is made to divide
            by zero.
        StackUnderflowError
            Error raised if there are insufficient variables on the stack to
            actually execute any arithmetic operations, i.e. zero or one.
        """
        
        result = 0
        
        try:
            param_2 = stack.pop()
            param_1 = stack.pop()
            if param_2 == 0 and operator is op.floordiv:
                raise ZeroDivisionError("divide by zero")
            result = operator(param_1, param_2)
        except IndexError as exc:
            raise StackUnderflowError(ForthInterpreter._SUFMSG) from exc
            
        stack.append(result)
            
        return stack
    
    @staticmethod
    def _add(stack: list[int]) -> list[int]:
        """Wrapper function for addition on a stack"""
        
        return ForthInterpreter._math_evaluate(op.add, stack)
    
    @staticmethod
    def _sub(stack: list[int]) -> list[int]:
        """Wrapper function for subtraction on a stack"""
        
        return ForthInterpreter._math_evaluate(op.sub, stack)
    
    @staticmethod
    def _mul(stack: list[int]) -> list[int]:
        """Wrapper function for multiplication on a stack"""
        
        return ForthInterpreter._math_evaluate(op.mul, stack)
    
    @staticmethod
    def _floordiv(stack: list[int]) -> list[int]:
        """Wrapper function for integer division on a stack"""
        
        return ForthInterpreter._math_evaluate(op.floordiv, stack)
    
    @staticmethod
    def _dup(stack: list[int]) -> list[int]:
        """
        Implements the Forth "dup" function, which adds another copy of the
        last item on the stack to the end of the stack. [1 dup] -> [1 1]

        Parameters
        ----------
        stack : list[int]
            A stack of data to apply the "dup" function to.

        Returns
        -------
        list[int]
            A stack of data with the final item duplicated as above.

        Raises
        ------
        StackUnderflowError
            StackUnderflowError is raised if there is no data to duplicate.
        """
        
        output = stack
        
        try:
            output.append(stack[-1])
        except IndexError as exc:
            raise StackUnderflowError(ForthInterpreter._SUFMSG) from exc
            
        return output

    @staticmethod
    def _drop(stack: list[int]) -> list[int]:
        """
        Implements the Forth "drop" function, which removes the last item from
        the stack. [1 drop] -> []

        Parameters
        ----------
        stack : list[int]
            A stack of data to apply the "drop" function to.

        Returns
        -------
        list[int]
            A stack of data with the final item removed as above.

        Raises
        ------
        StackUnderflowError
            StackUnderflowError raised if there is no data to remove.
        """
        
        output = stack
        
        try:
            output.pop()
        except IndexError as exc:
            raise StackUnderflowError(ForthInterpreter._SUFMSG) from exc
            
        return output
    
    @staticmethod
    def _swap(stack: list[int]) -> list[int]:
        """
        Implements the Forth "swap" function, which swaps the last and 
        next-to-last items on the stack. [1 2 swap] -> [2 1]

        Parameters
        ----------
        stack : list[int]
            A stack of data to apply the "swap" function to.

        Returns
        -------
        list[int]
            A stack of data with the indices of the final two items swapped.

        Raises
        ------
        StackUnderflowError
            StackUnderflowError raised if there are fewer than two items on the
            stack.
        """
        
        output = stack
        
        try:
            param_2 = output[-1]
            param_1 = output[-2]
            output[-2] = param_2
            output[-1] = param_1
        except IndexError as exc:
            raise StackUnderflowError(ForthInterpreter._SUFMSG) from exc
            
        return output
    
    @staticmethod
    def _over(stack: list[int]) -> list[int]:
        """
        Implements the Forth "over" method, which is similar to dup but copies
        the next-to-last value to the end instead of the last value.
        [1 2 3 over] -> [1 2 3 2]

        Parameters
        ----------
        stack : list[int]
            A stack of data to apply the "over" method to.

        Returns
        -------
        list[int]
            A stack of data with another copy of the next-to-last data value
            appended to the end of the stack.

        Raises
        ------
        StackUnderflowError
            StackUnderflowError raised if there are fewer than two items on the
            stack.
        """
        
        output = stack
        
        try:
            output.append(stack[-2])
        except IndexError as exc:
            raise StackUnderflowError(ForthInterpreter._SUFMSG) from exc
            
        return output
    
    # Effectively the translation table for built-ins, mapping the strings used
    # in the input to the above methods for actual execution.
    _OPERATORS = {
        "+": _add,
        "-": _sub, 
        "*": _mul, 
        "/": _floordiv,
        "dup": _dup, 
        "drop": _drop,
        "swap": _swap, 
        "over": _over
    }
    
    @staticmethod
    def _act(operator: str, stack: list[int]) -> list[int]:
        """
        Actually executes built-in operators that appear on the stack. WHenver
        self.execute finds a string which is a key in _OPERATORS it calls _act
        to execute it with the so-far built stack.

        Parameters
        ----------
        operator : str
            A string corresponding to one of the keys in _OPERATORS. This is
            guaranteed because _act is only called by self.execute, and
            self.execute only calls _act when it finds a keyword which is a key
            in _OPERATORS.
        stack : list[int]
            The stack to apply the method operator to.

        Returns
        -------
        list[int]
            The updated stack after applying the supplied operator.
        """
                
        return ForthInterpreter._OPERATORS[operator](stack)
    
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
                
        # A keyword definition cannot be a numerical value and must have
        # non-whitespace characters.
        def_match = re.compile(r": [^ \t\n\r\f\v0-9]+ .+ ;")
        
        for definition in user_defs:
            if not def_match.match(definition):
                raise ValueError("illegal operation")
            
            # identifies the keyword to be used and splits it from the 
            # actual definition.
            working_def = definition[1:-1].split()
            word = working_def[0]
            working_def = working_def[1:]
            
            # This is needed to allow the use of other user-defined
            # keywords in defining a keyword, as well as to pass certain
            # tests in the track involving redefinition of keywords while
            # using the keyword in the redefinition.
            working_def = self._translate_stack(working_def)
            
            # Note that self.translate becomes a dictionary of lists of
            # strings with strings as keys.
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
        
        if not self.translate:
            return stack
        
        output = []
        
        for word in stack:
            if word in self.translate:
                output.extend(self.translate[word])
            else:
                output.append(word)
                
        return output
    
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
                output = ForthInterpreter._act(data, output)
            else:
                raise ValueError("undefined operation")
            
        return output

def evaluate(input_data: list[str]) -> list[int]:
    '''
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
    '''
    
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

"""
Module solving the SGF Parsing problem from Exercism. Solution largely copied
from stOneSkull's solution as my initial attempt using regular expressions
ran into intractable problems.
"""

from string import whitespace

class SgfTree:
    """ 
    Class storing data from a Smart Game Format string. This is provided, the
    only change I made was adding the __hash__ function to suppress a linter
    complaint that would otherwise occur.
    """
    def __init__(self, properties=None, children=None):
        """
        Sets up the object with optional properties and children parameters to
        start off with those data fields filled.
        """
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        """ Tests equality between SgfTrees. """
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        if any(child != other_child 
               for (child, other_child) in zip(self.children, other.children)):
            return False
        return True

    def __ne__(self, other):
        """ The logical negation of an equality dunder method... """
        return not self == other
    
    def __hash__(self):
        """ 
        Creates a hash value for the tree to suppress linter complaints.
        """
        return hash(self.properties.items()) + hash(tuple(self.children))
    
class SgfParser:
    """
    Class implementing a parser for a string encoding a board game state in
    Smart Game Format form. Essentially it eats a string and returns an SgfTree
    object that encodes the same state in more "program-friendly" form.
    """
    
    @staticmethod
    def _parse_value(raw_value: str) -> str:
        """
        Given a "raw" string encoding a value associated with an SGF property,
        takes care of certain processing steps required by the tests to return
        the "true" value. Mainly this means dealing with escape sequences and
        whitespace.

        Parameters
        ----------
        raw_value : str
            A string that encodes the value for an SGF property, but without
            escape sequences and whitespace having been processed.

        Returns
        -------
        str
            The same string, but with escape sequences and whitespace processed
            correctly according to the tests. This mainly means escaping escape
            sequences and converting whitespace characters other than newlines
            to spaces.
        """
        
        value = ""
        
        kdx = 0
        while kdx < len(raw_value):
            if raw_value[kdx] == "\\":
                kdx += 1
                if kdx < len(raw_value):
                    if raw_value[kdx] == "\n":
                        pass
                    elif raw_value[kdx] in whitespace:
                        value += " "
                    else:
                        value += raw_value[kdx]
            elif raw_value[kdx] == "\t":
                value += " "
            else:
                value += raw_value[kdx]
            kdx += 1
        
        return value
    
    def __init__(self):
        """ Creates an SgfParser object by setting "self._idx" to 0. """
        self._idx = 0
        
    def reset(self):
        """
        Resets self._idx to 0 in the hypothetical case of wanting to use
        an SgfParser object to process multiple SGF format strings.
        """
        self._idx = 0
        
    def parse_tree(self, input_string: str) -> SgfTree:
        """
        Processes a Smart Game Format-encoding string into an SgfTree object.
        Note that it is called recursively indirectly. Encapsulating this
        function and its collaborator functions into an object means that the
        "idx" variable can be made into a shared variable without explicit
        value-passing.

        Parameters
        ----------
        input_string : str
            A string in SGF format to be encoded into an SgfTree object.

        Returns
        -------
        SgfTree
            An object encoding the specified board game state.

        Raises
        ------
        ValueError
            Raised if the input string is broken in such a way that a tree is
            left unterminated or the correct syntax to open a tree is not
            present.
        """
        
        if self._idx >= len(input_string) or input_string[self._idx] != "(":
            raise ValueError("tree missing")
            
        self._idx += 1
        tree = self._parse_sequence(input_string)
        self._idx += 1
        
        return tree
    
    def _parse_sequence(self, input_string: str) -> SgfTree:
        """
        Collaborator function for parse_tree that identifies properties and
        sub-trees and calls the appropriate functions to process them and build
        up an SgfTree object.

        Parameters
        ----------
        input_string : str
            A string in SGF format to be encoded into an SgfTree object.

        Returns
        -------
        SgfTree
            An object encoding the specified board game state.

        Raises
        ------
        ValueError
            Raised under two conditions:
                1: A property key includes lowercase characters;
                2: No nodes, that is, sequences which start with ";" and end
                   with:
                       1: ";", signaling the start of a child node;
                       2: "(", signaling the start of another tree;
                       3: ")", signaling the end of this tree
                   are present in the input_string.
        """
        
        nodes = []
        
        while input_string[self._idx] == ";":
            self._idx += 1
            prop_key_start = self._idx
            
            while input_string[self._idx].isalpha():
                if not input_string[self._idx].isupper():
                    raise ValueError("property must be in uppercase")
                self._idx += 1
                
            self._idx = prop_key_start
            
            properties = self._parse_properties(input_string)
            
            children = []
            
            while input_string[self._idx] == "(":
                child_tree = self.parse_tree(input_string)
                children.append(child_tree)
            
            nodes.append(SgfTree(properties, children))
            
        if not nodes:
            raise ValueError("tree with no nodes")
        
        # Stuffs all of the generated subtrees into the most parental tree.
        for jdx in range(len(nodes) - 1):
            nodes[jdx].children.append(nodes[jdx + 1])
            
        return nodes[0]
    
    def _parse_properties(self, input_string: str) -> dict[str: list]:
        """
        Given an input_string in SGF format, identifies the properties
        linked to a particular node. "Properties" consist, in the exercise, of
        a dictionary of keys represented as all-uppercase character strings
        (the uppercase-ness of them was already verified) and values
        represented as a list (in the exercise, of strings).
        
        In the input, there may be an arbitrary number of values for a given
        property key, with a fairly arbitrary form except that they must be
        enclosed in square brackets "[" and "]". However, within such brackets
        further square brackets have no further meaning, and a long series of
        such brackets may be present representing different values for the list
        associated with the key, that is,
            A[b][c][d]... -> {A: [b, c, d...]}
            
        There are certain rules for handling whitespace and escape ("\")
        characters in the values which are handled by the class function
        _parse_value.

        Parameters
        ----------
        input_string : str
            A string in SGF format to be encoded into an SgfTree object.

        Returns
        -------
        dict
            A dictionary encoding the properties for a given node in the
            input_string. It is formatted with keys consisting of uppercase
            characters and values consisting of lists of more or less arbitrary
            strings.

        Raises
        ------
        ValueError
            Raised if square brackets "[" are missing to separate values from
            keys.
        """
        
        properties = {}
        
        while input_string[self._idx] not in (";()"):
            key_start = self._idx
            while input_string[self._idx].isupper():
                self._idx += 1
            key = input_string[key_start:self._idx]
            
            if input_string[self._idx] != "[":
                raise ValueError("properties without delimiter")
                
            values = []
            
            while input_string[self._idx] == "[":
                self._idx += 1
                val_start = self._idx
                while input_string[self._idx] != "]":
                    if input_string[self._idx] == "\\":
                        self._idx += 1
                    self._idx += 1
                
                raw_value = input_string[val_start:self._idx]
                value = SgfParser._parse_value(raw_value)
                values.append(value)
                self._idx += 1
                
            properties[key] = values
            
        return properties

def parse(input_string: str) -> SgfTree:
    """
    Given a string encoding a board game state using Smart Game Format syntax,
    parse it to produce an SgfTree object also encoding the board game state.

    Parameters
    ----------
    input_string : str
        A string in SGF format to be encoded into an SgfTree object.

    Returns
    -------
    SgfTree
        An object encoding the specified board game state.
    """
    
    parser = SgfParser()
    
    return parser.parse_tree(input_string)
""" Module containing solution to Robot Name exercise on Exercism. """
import random as rd
import string

class Robot:
    """
        Class for creating and storing the name of a robot. Name format is two 
        upper-case ASCII letters followed by three digits. Names are randomly
        generated. Names are not allowed to be reused.
    """
    
    # Allows rejecting generated names that have already been used.
    _assigned_names = []
    
    @staticmethod
    def _name_generator() -> str:
        """
        Creates a random name following the previous described format of two
        upper-case ASCII letters followed by three digits.

        Returns
        -------
        str
            A string containing the name of a robot.
        """
        # Protects against seed manipulation
        rd.seed(None)
        
        output = []
        
        output.extend(rd.choices(string.ascii_uppercase, k = 2))
        output.extend(rd.choices(string.digits, k = 3))
        
        return "".join(output)
    
    @staticmethod
    def _name_set() -> str:
        """
        Using _name_generator, makes sure that a name is provided which has not
        yet been used.

        Returns
        -------
        str
            A robot name that has not been used.
        """
        
        candidate_name = Robot._name_generator()
        if candidate_name in Robot._assigned_names:
            while candidate_name in Robot._assigned_names:
                candidate_name = Robot._name_generator()
                
        return candidate_name
        
    def __init__(self) -> None:
        """
        Constructor for a robot. Just calls reset() to avoid duplicating code.

        Returns
        -------
        None
        """
        
        self.reset()
        
    def reset(self) -> None:
        """
        Assigns a name to a robot and adds it to the used names list.

        Returns
        -------
        None
        """
        
        self.name = Robot._name_set()
        Robot._assigned_names.append(self.name)

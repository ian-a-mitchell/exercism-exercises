""" Module containing solution to Robot Name exercise on Exercism. """
from random import seed, choices
from string import ascii_uppercase, digits

class Robot:
    """
        Class for creating and storing the name of a robot. Name format is two 
        upper-case ASCII letters followed by three digits. Names are randomly
        generated. Names are not allowed to be reused.
    """
    
    _NUM_LETT = 2
    _NUM_DIG = 3
    
    _MAX_LEN = len(ascii_uppercase) ** _NUM_LETT + len(digits) ** _NUM_DIG
    
    # Allows rejecting generated names that have already been used.
    _assigned_names = set()
    
    @staticmethod
    def _generate_name() -> str:
        """
        Creates a random name following the previous described format of two
        upper-case ASCII letters followed by three digits.

        Returns
        -------
        str
            A string containing the name of a robot.
        """
        # Protects against seed manipulation
        seed(None)
        
        output = []
        
        output.extend(choices(ascii_uppercase, k = Robot._NUM_LETT))
        output.extend(choices(digits, k = Robot._NUM_DIG))
        
        return "".join(output)     
        
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
        
        if len(Robot._assigned_names) == Robot._MAX_LEN:
            raise RuntimeError("Robot namespace is full!")
        
        while (name := Robot._generate_name()) in Robot._assigned_names:
            pass
                        
        self.name = name
        Robot._assigned_names.add(self.name)

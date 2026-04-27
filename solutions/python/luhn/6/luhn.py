""" Class implementing methods to solve the Luhn exercise for Exercism. """

import re

class Luhn:
    """
        Class implementing methods to solve the Luhn exercise for Exercism.
    """
    
    @staticmethod
    def _check_valid(num: str) -> bool:
        """"
        Runs through the Luhn checksum formula for the supplied number.
        
        Parameters
        ----------
        num : str
            Number to verify using the Luhn function.

        Returns
        -------
        bool
            True if the number is a valid number by the Luhn formula. False
            otherwise.
        """
        output = False
                        
        if not (len(num) < 2 or re.search(r'\D+', num)):
            reverse_num = [int(digit) for digit in reversed(num)]
                                
            reverse_num[1::2] = [2 * digit - 9 * (digit > 4) 
                           for digit in reverse_num[1::2]]
                                
            output = sum(reverse_num) % 10 == 0
            
        return output
    
    def __init__(self, card_num: str):
        """
        Creates Luhn object given a string for a number to verify.

        Parameters
        ----------
        card_num : str
            Number to verify using the Luhn function. Constructor removes
            spaces.

        Returns
        -------
        None
        """
        
        self.is_valid = Luhn._check_valid(re.sub(' ', '', card_num))

    def valid(self) -> bool:
        """
        Accesses the Luhn checksum result for the supplied number

        Returns
        -------
        bool
            True if the object is a valid number by the Luhn formula. False
            otherwise.
        """
        
        return self.is_valid

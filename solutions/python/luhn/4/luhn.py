""" Class implementing methods to solve the Luhn exercise for Exercism. """

import re

class Luhn:
    """
        Class implementing methods to solve the Luhn exercise for Exercism.
    """
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
        
        self.card_num = re.sub(' ', '', card_num)

    def valid(self) -> bool:
        """
        Runs through the Luhn checksum formula for the number provided to the
        constructor.

        Returns
        -------
        bool
            True if the object is a valid number by the Luhn formula. False
            otherwise.
        """
        
        output = False
                        
        if not (len(self.card_num) < 2 or re.search(r'\D+', self.card_num)):
            reverse_num = [int(digit) for digit in reversed(self.card_num)]
                                
            reverse_num[1::2] = [2 * digit - 9 * (digit > 4) 
                           for digit in reverse_num[1::2]]
                                
            output = sum(reverse_num) % 10 == 0
            
        return output

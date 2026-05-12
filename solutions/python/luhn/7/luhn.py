""" Class implementing methods to solve the Luhn exercise for Exercism. """

class Luhn:
    """
        Class implementing methods to solve the Luhn exercise for Exercism.
    """
    
    _RESULTS = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    
    @staticmethod
    def _valid_num(num: str) -> bool:
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
        
        num = num.replace(" ", "")
        
        try:
            reverse_num = [int(digit) for digit in reversed(num)]
        except ValueError:
            return False
        else:
            reverse_num[1::2] = [Luhn._RESULTS[digit] 
                                 for digit in reverse_num[1::2]]
            return len(num) > 1 and sum(reverse_num) % 10 == 0
                
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
        
        self.is_valid = Luhn._valid_num(card_num)

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

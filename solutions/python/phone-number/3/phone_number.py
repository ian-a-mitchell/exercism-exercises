""" Module for solving the Phone Number problem on Exercism. """

import re

class PhoneNumber:
    """ Class to validate and store a phone number. """
    
    _ALLOW_PUNC = {"+", ".", "(", ")", "-"}
    
    @staticmethod
    def _validate_number(number: str) -> str:
        """
        Takes a possible NANP phone number, validates that it is indeed such a
        number (or raises errors if it finds specific flaws), and provides a 
        cleaned-up version with just the digits to the caller.

        Parameters
        ----------
        number : str
            A possible NANP phone number.

        Returns
        -------
        str
            A cleaned up, valid, 10 digit NANP phone number.

        Raises
        ------
        ValueError
            Raises ValueErrors for any invalidity found, e.g. improper chars.
        """
        
        non_digits = re.findall(r"\D", number)
        
        if any(char.isalpha() for char in non_digits):
            raise ValueError("letters not permitted")
            
        if any(char not in PhoneNumber._ALLOW_PUNC for char in non_digits):
            raise ValueError("punctuations not permitted")
            
        clean_number = re.sub(r"\D", "", number)
        
        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")
            
        if len(clean_number) == 11:
            if clean_number[0] != "1":
                raise ValueError("11 digits must start with 1")
            clean_number = clean_number[1:]
            
        area_code = clean_number[:3]
        exchange_code = clean_number[3:6]
        subscriber = clean_number[6:]
        
        if area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if area_code[0] == "1":
            raise ValueError("area code cannot start with one")
            
        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one") 
        
        return [area_code, exchange_code, subscriber]
    
    def __init__(self, number: str) -> None:
        """
        Sets up the internal parameters of the object using the
        _validate_number method above.

        Parameters
        ----------
        number : str
            A possible NANP phone number.

        Returns
        -------
        None--but it sets up four internal variables:
        
        number : str
            An NANP-valid phone number (without country code)
            
        area_code : str
            The area code (first three digits) for number
            
        exchange_code : str
            The exchange code (second three digits) for number
            
        subscriber : str
            The last four digits of number
        """
        
        clean_num = PhoneNumber._validate_number(number)
        self.area_code, self.exchange_code, self.subscriber = clean_num
        self.number = "".join(clean_num)
        
    def pretty(self) -> str:
        """
        Returns the phone number in "pretty" format. For some reason Exercism
        includes a "-" between the area code and exchange code, which is
        non-standard. The country code is always omitted.

        Returns
        -------
        str
            A "pretty" phone number.
        """
        
        return f'({self.area_code})-{self.exchange_code}-{self.subscriber}'

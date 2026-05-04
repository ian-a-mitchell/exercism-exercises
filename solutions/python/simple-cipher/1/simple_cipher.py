""" Module for solving the Simple Cipher exercise on Exercism. """

import secrets
from string import ascii_lowercase as acl
from itertools import cycle

class Cipher:
    """
    Class that performs Vigenère enciphering/deciphering of strings. Only
    allows ASCII (English) letters.
    
    This functions by calculating a letter index shift (represented by a
    letter, so that the shift is equal to the index of the letter in the
    ascii_lowercase list) and then adding (enciphering) or subtracting
    (deciphering) that shift from the index of a given letter to convert it.
    
    The only complication is dealing with the wrap-around if the shift would
    put the new letter's index outside of the ascii_lowercase list's indices.
    """
    
    # Default key length
    _KEY_LEN = 100
    
    @staticmethod
    def _keygen() -> str:
        """ 
        Generates key (random string of letters of length _KEY_LEN) if none
        provided to constructor.
        """
        
        key = [secrets.choice(acl) for _ in range(Cipher._KEY_LEN)]
        
        return "".join(key)
    
    def __init__(self, key=None) -> None:
        """
        Sets the key for this enciphering/deciphering object.

        Parameters
        ----------
        key : str, optional
            Key to use in enciphering/deciphering. The default is None. If the
            default value or an invalid value (key containing characters other
            than lowercase ASCII letters) is provided, one is generated.

        Returns
        -------
        None
        """
        
        self.key = key
        
        if not key or any(char not in acl for char in key):
            self.key = Cipher._keygen()

    def encode(self, text: str) -> str:
        """
        Enciphers a provided plaintext using the object's key.

        Parameters
        ----------
        text : str
            A plaintext to encipher.

        Returns
        -------
        str
            The ciphertext using the key.
        """
        
        text = tuple(text.lower())
        key = cycle(self.key)
        
        output = [acl[(acl.index(char) + acl.index(key_char)) % len(acl)]
                  for char, key_char in zip(text, key)]
            
        return "".join(output)

    def decode(self, text: str) -> str:
        """
        Deciphers a provided ciphertext using the object's key.

        Parameters
        ----------
        text : str
            A ciphertext to decipher.

        Returns
        -------
        str
            The plaintext corresponding to the provided ciphertext and the
            object's key.
        """
        
        text = tuple(text.lower())
        key = cycle(self.key)
        
        output = [acl[acl.index(char) - acl.index(key_char)]
                  for char, key_char in zip(text, key)]
            
        return "".join(output)

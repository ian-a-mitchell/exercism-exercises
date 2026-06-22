"""
Module solving the Affine Cipher problem from Exercism.
https://en.wikipedia.org/wiki/Affine_cipher
"""

from math import gcd
from string import ascii_lowercase as as_lower

def validate_key(a: int) -> None:
    """
    Validates the supplied key number a for the affine cipher. The key number a
    is valid if a and m, m being the number of characters in the alphabet, are
    coprime, that is, gcd(a, m) == 1.

    Parameters
    ----------
    a : int
        The key number a for the affine ciphere (see below for an explanation
        of the use of a).

    Returns
    -------
    None

    Raises
    ------
    ValueError
        Raised if gcd(a, m) != 1, that is, the two are not coprime, in which
        case the encryption method cannot be used.
    """
    
    if gcd(a, len(as_lower)) != 1:
        raise ValueError("a and m must be coprime.")
        
def preprocessor(text: str) -> str:
    """
    Carries out common preprocessing steps for encrypting and decrypting text.
    These consist of:
        1: Removing non-alphanumerical characters;
        2: Changing the input to lower case.

    Parameters
    ----------
    text : str
        The text to be modified before encryption or decryption.

    Returns
    -------
    str
        The output text, with non-alphanumeric characters removed and
        alphabetical characters reduced to lower case.
    """
    
    return "".join((char for char in text.lower() if char.isalnum()))
        
def encode_generator(char: str, a: int, b: int) -> str:
    """
    Given key numbers a, b and a character, determines the affine cipher
    mappping of char to a new character. The affine cipher formula is
        new_idx = (a * char_idx + b) % m
    where
        new_idx = the index of the replacement character in a list of
                  alphabetical characters (which is zero-indexed);
        char_idx = the index of the original character in that list;
        a = the first key number;
        b = the second key number;
        m = the number of characters in the alphabet.
        
    Digits are left as-is per problem statement.

    Parameters
    ----------
    char : str
        The character to map onto the cipher character using key a, b.
    a : int
        The first key number, as above.
    b : int
        The second key number, as above.

    Returns
    -------
    str
        The character which input char maps to given the key a, b.

    Raises
    ------
    ValueError
        Raised if somehow a non-alphanumerical character makes it through.
    """
    
    new_char = ""
    
    if char.isalpha():
        new_char = as_lower[(a * as_lower.index(char) + b) % len(as_lower)]
    elif char.isdigit():
        new_char = char
    else:
        raise ValueError("Unencryptable text provided.")
    
    return new_char

def encode(plain_text: str, a: int, b: int) -> str:
    """
    Encodes a provided plaintext with the key a, b according to the affine
    cipher method. The main complication is the need to chunk the ciphertext
    into five character groups separated by spaces.

    Parameters
    ----------
    plain_text : str
        Plaintext to be encoded.
    a : int
        First key number.
    b : int
        Second key number.

    Returns
    -------
    str
        Ciphertext after encoding plaintext with a, b and chunking as described
        above.
    """
    
    validate_key(a)
        
    encoder = str.maketrans({char: encode_generator(char, a, b) 
                             for char in as_lower})
        
    def chunk(text: str):
        """ 
        Chunks provided text into blocks of 5 characters separated by spaces.
        """
        return " ".join(text[idx:idx+5] for idx in range(0, len(text), 5))
            
    return chunk("".join(preprocessor(plain_text).translate(encoder)))

def decode(ciphered_text: str, a: int, b: int) -> str:
    """
    Decodes a provided cipher text with the key a, b.

    Parameters
    ----------
    ciphered_text : str
        Ciphertext using the key a, b.
    a : int
        First key number.
    b : int
        Second key number.

    Returns
    -------
    str
        The plain text corresponding to the provided cipher text for the key
        a, b.
    """
    
    validate_key(a)
        
    # Note that this is the same as the encoder above except that the key and
    # value in the dictionary are reversed.
    decoder = str.maketrans({encode_generator(char, a, b): char 
                             for char in as_lower})
    
    return preprocessor(ciphered_text).translate(decoder)

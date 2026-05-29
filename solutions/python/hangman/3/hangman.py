""" Module solving the Exercism Hangman exercise. """
# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:
    """ A class representing a Hangman game. """
    def __init__(self, word: str):
        """
        Sets up the Hangman object by initializing the status, word, and number
        of guesses left.

        Parameters
        ----------
        word : str
            The word that the player is supposed to try to guess.
        """
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.my_word = word
        self.known_chars = set()

    def guess(self, char: str):
        """
        Handles taking guesses and determining whether they are in the word or
        not. If not, then the number of guesses remaining is decremented by 1.
        It also handles updating the status when the number of guesses declines
        below zero or the player guesses all of the characters.

        Parameters
        ----------
        char : str
            A character which the player guesses might be in the word.

        Raises
        ------
        ValueError
            Raised if the player attempts to keep guessing after the game has
            been won or lost.
        """
        
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        
        if char in self.my_word and not char in self.known_chars:
            self.known_chars.add(char)
        else:
            self.remaining_guesses -= 1
            
        if self.known_chars == set(self.my_word):
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        
    def get_masked_word(self) -> str:
        """
        Prints a copy of the word which is "masked," i.e. has all characters
        which have not yet been guessed replaced with "_".

        Returns
        -------
        str
            The masked word.
        """
        
        return "".join([char if char in self.known_chars else "_" 
                               for char in self.my_word])
                
    def get_status(self):
        """
        Returns the current status of the game.

        Returns
        -------
        str
            A string (or other object) that indicates whether the game is
            ongoing or has ended in loss or victory.
        """
        
        return self.status

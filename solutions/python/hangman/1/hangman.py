# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.my_word = word
        self.known_chars = set()

    def guess(self, char):
        
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
        
    def get_masked_word(self):
        
        masked_word = list(self.my_word)
        
        for idx, char in enumerate(masked_word):
            if char not in self.known_chars:
                masked_word[idx] = "_"
                
        return "".join(masked_word)

    def get_status(self):
        
        return self.status

""" Module for solving the Bowling problem in Exercism. """

class BowlingGame:
    """ Class representing a bowling game. """
    
    GAME_LENGTH = 10
    STRIKE = 10
    
    BAD_SCORE = "Reported score is impossible!"
    BAD_BONUS = "Too many bonus rolls reported."
    TOO_LONG = f"Bowling matches last {GAME_LENGTH} frames."
    TOO_SHORT = "All required rolls have been made."
        
    def __init__(self):
        """
        Creates the frames list used to store the, well, frames.

        Returns
        -------
        None
        """
        
        self.frames = []
        
    def _validate_rolls(self, pins: int):
        """
        Validates that the reported scores for a roll are acceptable.
        Unacceptable rolls are:
            1: Negative scores (did more pins show up...?);
            2: Scores > 10;
            3: Attempts to roll once ten full frames have been rolled, if the
               final frame did not earn bonus rolls;
            4: Attempts to roll more than 1 (spare) or 2 (strike) bonus rolls.

        Parameters
        ----------
        pins : int
            The reported score (pins knocked down) for a roll.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised in the event of any of the aforementioned issues.
        """
        
        if pins < 0 or pins > BowlingGame.STRIKE:
            raise ValueError(BowlingGame.BAD_SCORE)
            
        if len(self.frames) >= BowlingGame.GAME_LENGTH:
            final_frame = self.frames[BowlingGame.GAME_LENGTH - 1]
            sp_str = sum(final_frame) == BowlingGame.STRIKE
            
            if not sp_str and len(final_frame) == 2:
                raise ValueError(BowlingGame.TOO_LONG)
            if sp_str:
                bonus_frames = self.frames[BowlingGame.GAME_LENGTH:]
                bonus_rolled = sum((len(frame) for frame in bonus_frames))
                if len(final_frame) == 2 and bonus_rolled > 0:
                    raise ValueError(BowlingGame.BAD_BONUS)
                if len(final_frame) == 1 and bonus_rolled > 1:
                    raise ValueError(BowlingGame.BAD_BONUS)
                    
    def _validate_score(self):
        """
        Validates that scoring is possible. Mainly, this means:
            1: All ten frames have been played;
            2: All bonus rolls have been played.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised in the event of either of the problems above.
        """
        
        bad_game = False
        
        if len(self.frames) < BowlingGame.GAME_LENGTH:
            bad_game = True
            
        if not bad_game:
            final_frame = self.frames[BowlingGame.GAME_LENGTH - 1]
            sp_str = sum(final_frame) == BowlingGame.STRIKE
        
            if sp_str:
                bonus_frames = self.frames[BowlingGame.GAME_LENGTH:]
                bonus_rolled = sum((len(frame) for frame in bonus_frames))
            
                if len(final_frame) == 2 and bonus_rolled != 1:
                    bad_game = True
                elif len(final_frame) == 1 and bonus_rolled != 2:
                    bad_game = True
                
        if bad_game:
            raise ValueError(BowlingGame.TOO_SHORT)
                                        
    def roll(self, pins: int):
        """
        Given a reported score for a roll, updates the frames list so that it
        contains a list of tuples (frames) representing the reported state of
        the game so far.
        
        The main trick is determining when to have a two roll frame and when to
        have a one roll frame. This can be done by looking back to see if the
        previous roll and this roll form a frame.

        Parameters
        ----------
        pins : int
            The number of pins reported as knocked down by a roll.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if a frame with a score > 10 is reported (this is better
            done here than in _validate_rolls because it is context-dependent).
        """
        
        self._validate_rolls(pins)
            
        if self.frames and len(self.frames[-1]) == 1 and self.frames[-1][0] != BowlingGame.STRIKE:
            next_frame = (self.frames[-1][0], pins) 
            if sum(next_frame) > BowlingGame.STRIKE:
                raise ValueError(BowlingGame.BAD_SCORE)
            self.frames[-1] = next_frame
        else:
            self.frames.append((pins,))
                    
    def score(self) -> int:
        """
        Scores a bowling game. This requires validating the game to check 
        whether it is capable of being scored (essentially, ten frames and any
        required bonus rolls have been played). Then, it iterates over the
        frames and checks whether the special count-ahead rules for spares and
        srikes apply. If they do, it applies them (with a doubly-special rule
        for strikes so that it can count over subsequent strikes if there are
        any to count over).
        
        Note that it only scores frames in the main game--bonus rolls are only
        counted as part of the count-ahead rules.

        Returns
        -------
        int
            The total score of the game.
        """
                                
        self._validate_score()
        
        score = 0
        
        for idx, frame in enumerate(self.frames):
            if idx < BowlingGame.GAME_LENGTH:
                if len(frame) == 1:
                    score += BowlingGame.STRIKE
                    bonus = sum(self.frames[idx + 1])
                    if len(self.frames[idx + 1]) == 2:
                        score += bonus
                    else: # handles the "next roll is a strike" case
                        score += bonus + self.frames[idx + 2][0]
                elif sum(frame) == BowlingGame.STRIKE:
                    score += BowlingGame.STRIKE + self.frames[idx + 1][0]
                else:
                    score += sum(frame)
        
        return score

""" Module implementing a solution to the Camicia exercise for Exercism. """

import copy

class CamiciaGame:
    """ 
    Class storing a state of a game of "Camicia," to make it easier to compare
    to past iterations of the game. A class object can also compute the next
    state implied by itself.
    """
    
    PENALTIES = {
        "J": 1,
        "Q": 2,
        "K": 3,
        "A": 4
    }
    
    A_PLAYER = "a"
    B_PLAYER = "b"
    
    @staticmethod
    def _flip_player(cur_player: str) -> str:
        """
        Returns the player who is the opposite of a "current" player in some
        context. I found that I was doing this a lot so a method to do it made
        sense...

        Parameters
        ----------
        cur_player : str
            The "current" player in some context.

        Returns
        -------
        str
            The "other" player.
        """
        
        new_player = ""
        if cur_player == CamiciaGame.A_PLAYER:
            new_player = CamiciaGame.B_PLAYER
        else:
            new_player = CamiciaGame.A_PLAYER
            
        return new_player
    
    @staticmethod
    def _proc_hand(hand: list[str]) -> list[str]:
        """
        Non-face cards in "Camicia" are irrelevant, so to accurately determine
        whether two snapshots of the game are equivalent it is helpful to erase
        the differences between them.

        Parameters
        ----------
        hand : list[str]
            A list of strings, each string corresponding to a card in a
            52-card deck.

        Returns
        -------
        list[str]
            A list of strings. Strings corresponding to non-face (non-payment)
            cards in the input list have been replaced with "-" to represent
            their unimportance and equivalence.
        """
        
        return ["-" if card not in CamiciaGame.PENALTIES 
                else card for card in hand]
    
    def __init__(self, 
                 player_a: list[str], 
                 player_b: list[str], 
                 next_player: str = A_PLAYER
                 ):
        """
        Sets up a Camicia game state object. The game state consists of:
            1: Player A's deck at the start of a round;
            2: Player B's deck at the start of a round;
            3: The player to go next (or Player A if not specified).
            
        Auxiliary data includes:
            1: A copy of Player A's deck for manipulation while updating
               the game state;
            2: A copy of Player B's deck for the same purpose;
            3: A count of the cards moved during the next round of play.

        Parameters
        ----------
        player_a : list[str]
            The deck of cards player_a has at the start of a round.
        player_b : list[str]
            The deck of cards player_b has at the start of a round.
        next_player : str, optional
            The identity of the player to start the next round. The default is 
            A_PLAYER.

        Returns
        -------
        None
        """
        
        self.player_a = CamiciaGame._proc_hand(player_a)
        self.player_b = CamiciaGame._proc_hand(player_b)
        
        # The whole point of the object is to safely store the state of the
        # game at the start of a round, but computing the outcome of a round
        # is most straightforwardly done with popping. Therefore, it is useful
        # to have a separate copy of the hands which can be modified at will.
        self.a_hand = copy.deepcopy(self.player_a)
        self.b_hand = copy.deepcopy(self.player_b)
        
        self.next_player = next_player
        
        self.cards = 0
        
    def __eq__(self, other):
        """
        Defines equivalence between different game states. The starting state
        of two different rounds of Camicia are identical if:
            1: Player A in both rounds has the same face cards in the same
               positions in the deck;
            2: Player B in both rounds has the same face cards in the same
               positions in the deck;
            3: The next player to go is the same.

        Parameters
        ----------
        other : CamiciaGame
            The game state to compare self to.

        Returns
        -------
        Bool
            True if all three elements listed above are the same, that is,
            this object represents the same game state as other. Otherwise
            False.
        """
        
        same_a = self.player_a == other.player_a
        same_b = self.player_b == other.player_b
        same_next_player = self.next_player == other.next_player
        
        return same_a and same_b and same_next_player
    
    def __hash__(self):
        """
        Dunder method for calculating the hash of a CamiciaGame object. Mostly
        because the Exercism linter complains if __eq__ is defined but
        __hash__ is not.

        Returns
        -------
        ???
            The hash of this object, or rather the hash of the tuple of the two
            starting game decks.
        """
        
        return hash((self.player_a, self.player_b, self.next_player))
    
    def finished(self) -> bool:
        """
        Reports whether this game state corresponds to a finished game. A
        finished game is one where one player has all of the cards, which
        necessarily means that the other has none.

        Returns
        -------
        Bool
            True if the game is finished, False otherwise.
        """
        
        return not self.player_a or not self.player_b
    
    def play_round(self) -> tuple:
        """
        Determines the state of a game of Camicia after applying the rules to
        the state stored in this object, and tracks the number of cards moved
        in the process.

        Returns
        -------
        tuple[CamiciaGame, int]
            A tuple containing the state of the game at the start of the next
            round and an integer showing how many cards were moved between the
            start and end of this round.
        """
        
        pot = []
        trick_taker = ""
        
        while not trick_taker:
            if self.next_player == CamiciaGame.A_PLAYER:
                if self.a_hand:
                    pot.append(self.a_hand.pop(0))
                    self.next_player = CamiciaGame.B_PLAYER
                    self.cards += 1
                else:
                    trick_taker = CamiciaGame.B_PLAYER
            elif self.next_player == CamiciaGame.B_PLAYER:
                if self.b_hand:
                    pot.append(self.b_hand.pop(0))
                    self.next_player = CamiciaGame.A_PLAYER
                    self.cards += 1
                else:
                    trick_taker = CamiciaGame.A_PLAYER
            if pot[-1] in CamiciaGame.PENALTIES:
                payment = self._payment_cards(pot[-1], self.next_player)
                pot.extend(payment[0])
                trick_taker = payment[1]
                            
        new_a_hand = copy.deepcopy(self.a_hand)
        new_b_hand = copy.deepcopy(self.b_hand)
        
        if trick_taker == CamiciaGame.A_PLAYER:
            new_a_hand.extend(pot)
        else:
            new_b_hand.extend(pot)
            
        next_round_start = CamiciaGame(new_a_hand, new_b_hand, trick_taker)
        
        return (next_round_start, self.cards)
        
    def _payment_cards(self, pay_card: str, pay_player: str) -> tuple:
        """
        Handles the payment card rules for a round of Camicia. These rules
        were (to me anyway) naturally recursive, so a separate method for them
        made sense.

        Parameters
        ----------
        pay_card : str
            The payment card which is currently acting.
        pay_player : str
            The player who needs to pay cards into the pot.

        Returns
        -------
        tuple(list[str], str)
            A tuple containing a list of cards paid into the pot and the
            identity of the trick-taker implied by this payment request.
        """
        
        lim = CamiciaGame.PENALTIES[pay_card]
        payer_hand = []
        if pay_player == CamiciaGame.A_PLAYER:
            payer_hand = self.a_hand
        else:
            payer_hand = self.b_hand
        count = 0
        trick_taker = ""
        paid_cards = []
        
        while payer_hand and count < lim:
            paid_cards.append(payer_hand.pop(0))
            self.cards += 1
            count += 1
            # The recursive bit: triggers a new round of payment if a payment
            # card comes up.
            if paid_cards[-1] in CamiciaGame.PENALTIES:
                new_payer = CamiciaGame._flip_player(pay_player)
                sub_paid = self._payment_cards(paid_cards[-1], new_payer)
                paid_cards.extend(sub_paid[0])
                trick_taker = sub_paid[1]
                break # The original payment does not need to be finished.
            
        # Handles the cases of the payer running out of cards or successfully
        # finishing the payment.
        if not trick_taker:
            trick_taker = CamiciaGame._flip_player(pay_player)
            
        return (paid_cards, trick_taker)
            

def simulate_game(player_a: list[str], player_b: list[str]) -> dict:
    """
    The access function that simulates a game as a whole. It keeps track of
    the number of tricks taken and total cards played, as well as maintaining a
    list of previously visited states so that it can identify loops.

    Parameters
    ----------
    player_a : list[str]
        The hand which player A starts the game with.
    player_b : list[str]
        The hand which player B starts the game with.

    Returns
    -------
    dict{str: str, str: int, str: int}
        A dictionary containing string labels and, respectively,
            1: The final status of the game (finished or loop) as a string;
            2: The number of cards played in the game as an int;
            3: The number of tricks taken in the game as an int.
    """
    
    visited_states = []
    status = ""
    cards_played = 0
    tricks_taken = 0
    continue_game = True
    
    start_state = CamiciaGame(player_a, player_b)
    visited_states.append(start_state)
    
    while continue_game:
        next_state, cards = visited_states[-1].play_round()
        tricks_taken += 1
        cards_played += cards
        if next_state in visited_states:
            continue_game = False
            status = "loop"
        elif next_state.finished():
            continue_game = False
            status = "finished"
        visited_states.append(next_state)
            
    return {"status": status, "cards": cards_played, "tricks": tricks_taken}

""" Methods for solving the Poker exercise on Exercism. """

class PokerHand:
    """ 
    A class that represents a hand in poker, including knowing what kind of 
    hand it is and being able to score itself against other hands.
    """
    
    _VALUES = {
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 3,
        "6": 4,
        "7": 5,
        "8": 6,
        "9": 7,
        "10": 8,
        "J": 9, 
        "Q": 10,
        "K": 11,
        "A": 12
    }
    
    _LOW_STRAIGHT = ("A", "5", "4", "3", "2")
    
    @staticmethod
    def _straight_score(me, you):
        """ 
        Finds the winner between the PokerHands me and you if they are both
        "straights". This is largely the same as the high card method, except
        that the low-ace straight above is allowed, so it needs to be handled
        specially.
        
        Parameters
        ----------
        me: PokerHand
            A PokerHand.
        you: PokerHand
            Another PokerHand.

        Returns
        -------
        PokerHand
            The winning PokerHand, or None if neither wins.
        """
        
        output = None
        
        i_low_st = (set(me.values) == set(PokerHand._LOW_STRAIGHT))
        you_low_st = (set(you.values) == set(PokerHand._LOW_STRAIGHT))
        
        if i_low_st and not you_low_st:
            output = you
        elif you_low_st and not i_low_st:
            output = me
                        
        if not output:
            output = PokerHand._high_card_score(me, you)
                        
        return output
    
    @staticmethod
    def _ns_score(me, you, num: int):
        """ 
        Finds the winner between the PokerHands me and you if they are both
        using the same "n" method, i.e. four of a kind, three of a kind, two
        pairs, or pair.
        
        Parameters
        ----------
        me: PokerHand
            A PokerHand.
        you: PokerHand
            Another PokerHand.
        num: int
            The size of the special sublist, e.g. 4 for four of a kind or 2
            for either two pairs or pair.

        Returns
        -------
        PokerHand
            The winning PokerHand, or None if neither wins.
        """
        
        my_ns = me.get_n_set(num)
        your_ns = you.get_n_set(num)
        
        return PokerHand._subhand_compare(me, you, my_ns, your_ns)
    
    @staticmethod
    def _high_card_score(me, you):
        """ 
        Finds the winner between the PokerHands me and you using the high card
        method, i.e. finding which one has the highest-value card not matched
        by the other PokerHand.
        
        Parameters
        ----------
        me: PokerHand
            A PokerHand.
        you: PokerHand
            Another PokerHand.

        Returns
        -------
        PokerHand
            Whichever PokerHand wins in a high card comparison, or None if
            they are tied.
        """
                        
        return PokerHand._subhand_compare(me, you, me.values, you.values)
    
    @staticmethod
    def _subhand_compare(me, you, my_cards, your_cards):
        """ 
        Compares two "subhands" to find which one "wins" (has the highest-value
        card not matched by the other subhand), then matches the winning
        subhand to whichever PokerHand it came from.
        
        Note that in the event of a tie it returns nothing.
        
        Parameters
        ----------
        me: PokerHand
            The PokerHand from which my_cards came from.
        you: PokerHand
            The PokerHand from which your_cards came from.
        my_cards: list[str]
            A list of card values from the PokerHand me that need to be scored
            against a corresponding list from the PokerHand you.
        your_cards: list[str]
            A list of card values from the PokerHand you that need to be scored
            against a corresponding list from the PokerHand me.

        Returns
        -------
        list[PokerHand]
            The PokerHand that the "winning" subhand came from, or the empty
            list if there is a tie.
        """
        
        output = []
        
        winner = []
        
        for my_card, your_card in zip(my_cards, your_cards):
            if not winner:
                my_value = PokerHand._VALUES[my_card]
                your_value = PokerHand._VALUES[your_card]
                if my_value > your_value:
                    winner = my_cards
                elif my_value < your_value:
                    winner = your_cards
                
        if winner == my_cards:
            output = me
        elif winner == your_cards:
            output = you
            
        return output
    
    _HAND_FUNCS = {
            0: lambda me, you: PokerHand._straight_score(me, you),
            1: lambda me, you: PokerHand._ns_score(me, you, 4),
            2: lambda me, you: PokerHand._ns_score(me, you, 3),
            3: lambda me, you: PokerHand._high_card_score(me, you),
            4: lambda me, you: PokerHand._straight_score(me, you),
            5: lambda me, you: PokerHand._ns_score(me, you, 3),
            6: lambda me, you: PokerHand._ns_score(me, you, 2),
            7: lambda me, you: PokerHand._ns_score(me, you, 2),
            8: lambda me, you: PokerHand._high_card_score(me, you)
    }
    
    def __init__(self, hand: str) -> None:
        """ 
        The initalization function processes the hand to be more useful for
        later comparisons, identifies what sort of hand this is, for example
        a straight flush, and sets up the correct tie-breaking comparison
        function for this specific poker hand.
        
        Note that proc_hand and thus values are sorted by value, highest first.
        
        Parameters
        ----------
        hand: str
            A string containing the cards of a poker hand, encoded as 1 or 2
            characters designating the value (2 in the case of a 10) and 1
            character encoding the suite.

        Returns
        -------
        None
        """
        
        self.hand = hand
        
        list_hand = hand.split()
        
        self.proc_hand = [(card[0:-1], card[-1]) for card in list_hand]
        self.proc_hand = sorted(self.proc_hand, 
                         key = lambda card: (PokerHand._VALUES[card[0]],
                                             card[1]), reverse = True)
        self.values = [card[0] for card in self.proc_hand]
                            
        flush = len({card[1] for card in self.proc_hand}) == 1
        
        hand_type = [self._straight() and flush, self.get_n_set(4),
                     self._full_house(), flush, self._straight(), 
                     self.get_n_set(3), len(self.get_n_set(2)) == 2,
                     len(self.get_n_set(2)) == 1, True]
        
        self.category = len(hand_type)
        
        for idx, cat in enumerate(hand_type):
            if cat and self.category == len(hand_type):
                self.category = idx
        
        self.my_score = lambda other: PokerHand._HAND_FUNCS[self.category](self, other)
    
    def __hash__(self):
        """ Support function needed to inject PokerHands into hashables. """
        
        return hash(self.hand)
    
    def __eq__(self, other) -> bool:
        """ 
        A hand is equal to another hand if it ties with it in scoring. Note
        that two tied hands *do not* necessarily have the same card; this is
        intentional, to support the specification's request to support ties.
        
        Parameters
        ----------
        other: PokerHand
            The other hand to compare this one to.

        Returns
        -------
        bool
            True if this hand and "other" tie, false otherwise.
        """
        
        winners = self.score(other)
        
        if len(winners) == 2:
            return True
        
        return False
    
    def __ne__(self, other):
        """ Inverse of equality method. """
        
        return not self == other
    
    def __gt__(self, other):
        """ 
        A hand is "greater than" another hand if it beats it, that is, has a
        higher rank.
        
        Parameters
        ----------
        other: PokerHand
            The other hand to compare this one to.

        Returns
        -------
        bool
            True if this hand beats the "other" hand, false if it loses or they
            are tied.
        """
        
        winners = self.score(other)
                
        if len(winners) == 1 and self.has_same_hand(winners[0]):
            return True
        
        return False
    
    def __ge__(self, other) -> bool:
        """
        Dunder method for implementing greater than or equal comparisons using
        greater than and equal comparison dunder methods.
        """
        
        return self > other or self == other
    
    def __lt__(self, other) -> bool:
        """ 
        A hand is "less than" another hand if it loses to it, that is, has a 
        lower rank.
        
        Parameters
        ----------
        other: PokerHand
            PokerHand to compare this PokerHand to.

        Returns
        -------
        bool
            True if this hand loses to the "other" hand, false if it wins or
            they are tied.
        """
        
        winners = self.score(other)
        
        if len(winners) == 1 and not self.has_same_hand(winners[0]):
            return True
        
        return False
        
    def __le__(self, other) -> bool:
        """ 
        Dunder method for less than or equal comparisons...uses less than and
        equal dunder methods to implement!
        """
        
        return self < other or self == other
    
    def _straight(self) -> bool:
        """ 
        Identifies whether this hand is a straight, that is, whether it
        consists of five cards that include all values between the lowest and
        highest values in the hand. Unlike most cases, aces can count as low
        here, but that only corresponds to one specific hand.
        
        Parameters
        ----------
        None

        Returns
        -------
        bool
            True if this hand is a straight, false otherwise.
        """
        
        is_straight = False
        
        start_index = PokerHand._VALUES[self.values[0]]
        end_index = PokerHand._VALUES[self.values[-1]]
        
        if len(set(self.values)) == 5 and (start_index - end_index) == 4:
            is_straight = True
        elif set(self.values) == set(PokerHand._LOW_STRAIGHT):
            is_straight = True
        
        return is_straight
        
    def _full_house(self) -> bool:
        """ 
        Identifies whether this hand is a full house, i.e. consists of a three
        of a kind and a pair. This is true if there it contains a three of a
        kind and only two distinct values.
        
        Parameters
        ----------
        None

        Returns
        -------
        bool
            True if this hand is a full house, false otherwise.
        """
                        
        return self.get_n_set(3) and len(set(self.values)) == 2
    
    def get_n_set(self, num: int) -> list[str]:
        """ 
        Provides a list of values which appear num times in this poker hand.
        A universal function for finding four of a kind, three of a kind, or
        pairs.
        
        Parameters
        ----------
        num: int
            The number of times a card should appear in the hand for its value
            to appear in the list.

        Returns
        -------
        list[str]
            A list of the values which appear num times in the hand.
        """
        
        output = []
        
        for value in set(self.values):
            if self.values.count(value) == num:
                output.append(value)
                  
        if output:
            output.sort(key = lambda value: PokerHand._VALUES[value],
                        reverse = True)
                                
        return output
    
    def has_same_hand(self, other) -> bool:
        """ 
        Identifies whether this PokerHand and other PokerHand have the exact
        same hand of cards.
        
        Parameters
        ----------
        other: PokerHand
            The other poker hand to compare this one to.

        Returns
        -------
        Bool
            True if the hands are *exactly* the same, false otherwise.
        """
        
        return self.proc_hand == other.proc_hand
    
    def score(self, other) -> list:
        """ 
        "Scores" two poker hands against each other, that is, determines which
        one is higher ranked. The basic rule is
            1: Whichever hand has a higher basic rank wins (is returned)
            2: If the two hands have the same basic rank, a tie-breaker
               function is invoked (each rank has a specific tie-breaker
               function, defined in PokerHand._HAND_FUNCS).
            3: As a fallback, the hands are scored via high card, i.e.
               the first card that one hand has that outranks a card in the
               other hand wins. This allows for ties, which are needed for the
               problem spec.
        
        Parameters
        ----------
        other: PokerHand
            The other PokerHand object to compare this one to.

        Returns
        -------
        list[PokerHand]
            A list containing one or two PokerHand objects, depending on how
            the two were scored and if any ties could be broken.
        """
        
        output = []
        
        if self.category < other.category:
            output = [self]
        elif self.category > other.category:
            output = [other]
        else:
            winner = self.my_score(other)
            if not winner:
                winner = PokerHand._high_card_score(self, other)
            if winner:
                output = [winner]
            else:
                output = [self, other]
                
        return output

def best_hands(hands: list[str]) -> list[str]:
    """ 
    Given a set of poker hands, returns the hands which "score" the highest.
    Can return multiple hands in the case of a tie. Uses "standard" ordering.
    
    Parameters
    ----------
    hands: list[str]
        List of poker hands to rank. Each hand is a string consisting of pairs
        separated by spaces, each pair consisting of 1 or 2 characters 
        identifying the card value and 1 character identifying the suite.

    Returns
    -------
    list[str]
        List of the highest-ranking hands from the provided set.
    """
    
    proc_hands = [PokerHand(hand) for hand in hands]
        
    return [hand.hand for hand in proc_hands if hand == max(proc_hands)]
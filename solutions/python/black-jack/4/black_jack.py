"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

BLACKJACK = 21
ACE_LOW = 1
ACE_HIGH = 11


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    card_dict = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
        }
    
    return card_dict[card]

def hand_value(card_one, card_two):
    """Calculate the total value of the hand.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - sum of the values for card_one and card_two.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11
    3.  '2' - '10' = numerical value.
    """
    card_one = value_of_card(card_one)
    card_two = value_of_card(card_two)
        
    card_sum = card_one + card_two
    if has_ace(card_one, card_two):
        card_sum = card_sum + (ACE_HIGH - ACE_LOW)
        
    return card_sum

def has_ace(card_one, card_two):
    """Calculate the total value of the hand.

    :param card_one, card_two: str - card dealt.
    :return: bool - does the hand contain an ace.
    """
    
    return ('A' in (card_one, card_two))
    

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    higher = card_two
    
    if value_one == value_two:
        higher = (card_one, card_two)
    elif value_one > value_two:
        higher = card_one

    return higher


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    card_sum = hand_value(card_one, card_two)
        
    ace_value = ACE_HIGH
    
    if (card_sum + ace_value) > BLACKJACK:
        ace_value = ACE_LOW
        
    return ace_value


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
        
    return hand_value(card_one, card_two) == BLACKJACK


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    
    return isinstance(higher_card(card_one, card_two), tuple)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
        
    card_sum = hand_value(card_one, card_two)
    
    if(has_ace(card_one, card_two)):
        card_sum = card_sum - ACE_HIGH + ACE_LOW
    
    return (card_sum > 8) and (card_sum < 12)
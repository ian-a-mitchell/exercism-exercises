import copy

class CamiciaGame:
    
    PENALTIES = {
        "J": 1,
        "Q": 2,
        "K": 3,
        "A": 4
    }
    
    A_PLAYER = "a"
    B_PLAYER = "b"
    
    @staticmethod
    def _proc_hand(hand: list[str]):
        
        return ["-" if card not in CamiciaGame.PENALTIES else card for card in hand]
    
    def __init__(self, 
                 player_a: list[str], 
                 player_b: list[str], 
                 next_player: str = A_PLAYER
                 ):
        
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
        
        same_a = self.player_a == other.player_a
        same_b = self.player_b == other.player_b
        same_next_player = self.next_player == other.next_player
        
        return same_a and same_b and same_next_player
    
    def hash(self):
        
        return hash((self.player_a, self.player_b))
    
    def finish_poll(self):
        
        return not self.player_a or not self.player_b
    
    def play_round(self) -> tuple:
        
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
                payment = self.payment_cards(pot[-1], self.next_player)
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
        
    def payment_cards(self, pay_card: str, pay_player: str) -> tuple:
        
        lim = CamiciaGame.PENALTIES[pay_card]
        payer = self.a_hand if pay_player == CamiciaGame.A_PLAYER else self.b_hand
        count = 0
        trick_taker = ""
        paid_cards = []
        
        while payer and count < lim:
            paid_cards.append(payer.pop(0))
            self.cards += 1
            count += 1
            if paid_cards[-1] in CamiciaGame.PENALTIES:
                new_payer = CamiciaGame.B_PLAYER if pay_player == CamiciaGame.A_PLAYER else CamiciaGame.A_PLAYER
                sub_paid = self.payment_cards(paid_cards[-1], new_payer)
                paid_cards.extend(sub_paid[0])
                trick_taker = sub_paid[1]
                break
            
        if not trick_taker:
            trick_taker = CamiciaGame.B_PLAYER if pay_player == CamiciaGame.A_PLAYER else CamiciaGame.A_PLAYER
            
        return (paid_cards, trick_taker)
            

def simulate_game(player_a: list[str], player_b: list[str]) -> dict:
    
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
        elif next_state.finish_poll():
            continue_game = False
            status = "finished"
        visited_states.append(next_state)
            
    return {"status": status, "cards": cards_played, "tricks": tricks_taken}

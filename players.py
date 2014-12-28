import random
from cards import *

victory_point_cards = nonkingdom_victory_point_cards
victory_point_cards["garden"] = lambda player: len(player.all_cards)/10


class Player(object):
    def __init__(self, game_space):
        self.game = game_space
        self.deck = 7*["copper"] + 3*["estate"]
        self.discard = []
        self.hand = []
        self.played = []
        self.set_aside = []
        random.shuffle(self.deck)
        self.draw(5)
        self.reset_turn_variables()
        
    def take_turn(self):
        """Method for taking a turn"""
        pass
    
    def draw(self, num_cards):
        """Draws num_cards from deck,
        putting them in hand.
        """
        for _ in range(num_cards):
            if not self.deck:
                if self.discard:
                    self.deck = self.discard
                    random.shuffle(self.deck)
                else:
                    return
            self.hand.append(self.deck.pop(0))
            
    def discard(self, card):
        """Discards the given card from the hand.
        Raises an exception if the card is not in hand.
        """
        if card not in self.hand:
            raise Exception("No {} in hand".format(card))
        self.hand.pop(self.hand.index(card))
        self.discard.append(card)
        
    def play_card(self, card):
        """Plays the given card and puts in the played area.
        Raises an exception if the card is not in hand.
        """
        if card not in self.hand:
            raise Exception("No {} in hand".format(card))
        self.hand.pop(self.hand.index(card))
        self.played.append(card)
        eval(card)(self)
    
    def buy(self, card):
        """Attempts to buy a card specified by
        given card string.  Returns False if unable to
        buy (not enough money or none remaining). Returns
        True if purchase is successful.
        """
        if self.buying_power < cost(card) or self.num_buys < 1:
            return False
        try:
            self.game.sell(card)
        except Exception as e:
            return False
        self.buying_power -= cost(card)
        self.num_buys -= 1
        self.discard.append(card)
        return True
    # Need to deal with cards costing potions
        
    def reset_turn_variables(self):
        self.buying_power = 0  # Available money
        self.num_buys = 1
        self.available_actions = 1
        self.available_potions = 0
        
    @property
    def all_cards(self):
        """Returns a list of all cards the player owns"""
        return self.deck + self.hand + self.set_aside + self.discard
        
    @property
    def victory_points(self):
        """Returns the player's current victory point total"""
        score = 0
        for card in self.all_cards:
            if card in victory_point_cards:
                score += victory_point_cards[card](self)
        return score

        
class HumanPlayer(Player):
    def __init__(self, game_space, name):
        super().__init__(game_space)
        self.name = name

    def take_turn(self):
        print("\n{}'s turn".format(self.name))
        played_cards = input("Cards you play affecting other players:\n").split()
        for card in played_cards:
            try:
                eval(card)(self)
            except Exception as e:
                print(e)
        while True:
            bought_cards = input("Cards you gained this turn, hit enter if done:\n").split()
            if not bought_cards:
                break
            for card in bought_cards:
                try:
                    self.game.sell(card)
                    self.discard.append(card)
                    print("{} purchased".format(card))
                except Exception as e:
                    print(e)
                    
                
    def __repr__(self):
        return self.name
        
    def __str__(self):
        return self.name
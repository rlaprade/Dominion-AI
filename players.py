import random
from cards import *
from errors import *

# victory_point_cards = nonkingdom_victory_point_cards
# victory_point_cards["garden"] = lambda player: len(player.all_cards)/10


class Player(object):
    def __init__(self, game_space):
        self.game = game_space
        self.deck = 7*[copper] + 3*[estate]
        self.discard = []
        self.hand = []
        self.played = []
        self.durations = []
        random.shuffle(self.deck)
        self.end_turn()
        
    def take_turn(self):
        """Method for taking a turn"""
        self.duration_effects()
        self.end_turn()
    
    def draw(self, num_cards):
        """Draws num_cards from deck,
        putting them in hand.
        """
        for _ in range(num_cards):
            if not self.deck:
                if self.discard:
                    self.deck = self.discard
                    self.discard = []
                    random.shuffle(self.deck)
                else:
                    return
            self.hand.append(self.deck.pop(0))
            
    def discard(self, card):
        """Discards the given card from the hand.
        Raises an exception if the card is not in hand.
        """
        if card not in self.hand:
            raise HandError(card)
        self.hand.pop(self.hand.index(card))
        self.discard.append(card)
        
    def trash_from_hand(self, card):
        """Trashes the given card from hand.
        Raises an exception if the card is not in hand.
        """
        if card not in self.hand:
            raise HandError(card)
        self.hand.pop(self.hand.index(card))
        self.game.trash.append(card)
        
    def play_card(self, card):
        """Plays the given card and puts in the played area.
        Raises an exception if the card is not in hand.
        """
        if card not in self.hand:
            raise HandError(card)
        if isinstance(card, ActionDuration):
            self.durations.append(card)
        
        if isinstance(card, Action):
            self.play_action(card)
        elif isinstance(card, Treasure):
            self.play_treasure(card)

    def play_action(self, card):
        """Plays the given action card"""
        if self.available_actions <= 0:
            raise ZeroActionsError(card)
        self.hand.pop(self.hand.index(card))
        self.played.append(card)
        self.draw(card.plus_cards)
        self.available_actions += card.plus_actions - 1
        self.buying_power += card.plus_money
        self.num_buys += card.plus_buys
        card.effect(self)
        
    def play_treasure(self, card):
        """Plays the given treasure card"""
        self.hand.pop(self.hand.index(card))
        self.played.append(card)
        self.buying_power += card.plus_money
        card.effect(self)
        
    def duration_effects(self):
        """Enact effects of duration cards left over from the previous turn"""
        for card in self.durations:
            self.draw(card.duration_cards)
            self.available_actions += card.duration_actions
            self.buying_power += card.duration_money
            self.num_buys += card.duration_buys
            card.effect(self)
        self.durations = []
            
    def buy(self, card):
        """Attempts to buy a card specified by
        given card string.  Returns False if unable to
        buy (not enough money or none remaining). Returns
        True if purchase is successful.
        """
        if self.buying_power < card.cost or self.num_buys < 1:
            raise InsufficientFundsError(card)
        # try:
        self.game.sell(card)
        # except Exception as e:
            # return False
        self.buying_power -= card.cost
        self.num_buys -= 1
        self.discard.append(card)
        return True
    # Need to deal with cards costing potions
        
    def end_turn(self):
        """Resets all turn variables and puts
        all used cards into discard and draws 
        a new hand, thus preparing for next turn.
        """
        self.buying_power = 0  # Available money
        self.num_buys = 1
        self.available_actions = 1
        self.available_potions = 0
        for card in self.durations:
            self.played.pop(self.played.index(card))
        self.discard = self.played + self.discard
        self.discard = self.hand + self.discard
        self.played = self.durations
        self.hand = []
        self.draw(5)
        
    @property
    def all_cards(self):
        """Returns a list of all cards the player owns"""
        return self.deck + self.hand + self.cards_in_play + self.discard
        
    @property
    def victory_points(self):
        """Returns the player's current victory point total"""
        score = 0
        for card in self.all_cards:
            if isinstance(card, Victory):
                score += card.victory_points
        return score
        
    @property
    def cards_in_play(self):
        return self.played
        
    def voluntary_trash(self, num):
        """Trashes up to num cards from the hand,
        the player chooses which ones and how many
        """
        pass
    
        
class HumanPlayer(Player):
    def __init__(self, game_space, name):
        super().__init__(game_space)
        self.name = name

    def take_turn(self):
        print("\n{}'s turn".format(self.name))
        self.duration_effects()
        played_cards = input("Cards you play affecting other players:\n").split()
        for card in played_cards:
            card = eval(card)
            try:
                self.play_card(card)
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
        self.end_turn()
        
    def voluntary_trash(self, num):
        """Allows the player to trash up to num cards from their hand"""
        while num > 0:
            card_str = input("Choose a card to trash (leave blank if you do not wish to trash)\n")
            if not card_str:
                break
            try:
                card = eval(card_str)
            except Exception as e:
                print("No such card {}.".format(card))
                continue
            self.game.trash.append(card)
            print("Trashed {}.".format(card))
            num -= 1
                
    def __repr__(self):
        return self.name
        
    def __str__(self):
        return self.name

        
class HumanNoCards(HumanPlayer):
    def take_turn(self):
        print("\n{}'s turn".format(self.name))
        self.duration_effects()
        while True:
            print("\nHand:  {},  In Play:  {},  Actions:  {}".format(self.hand, self.played, self.available_actions))
            card = input("What card do you wish to play? (leave blank if ready to buy) ")
            if card == "done" or card == "":
                break
            try:
                self.play_card(eval(card))
            except Exception as e:
                print(e)
        # Play all remaining treasure
        treasures_in_hand = []
        for card in self.hand:
            if isinstance(card, Treasure):
                treasures_in_hand.append(card)
        for card in treasures_in_hand:
            self.play_card(card)
        while True:
            if self.num_buys == 0:
                break
            print("\nMoney:  {},  Buys:  {}".format(self.buying_power, self.num_buys))
            card = input("What card do you wish to buy? (type 'done' if finished) ")
            if card == "done" or card == "":
                break
            try:
                self.buy(eval(card))
                print("{} purchased".format(card))
            except Exception as e:
                print(e)            
        self.end_turn()
        
    def voluntary_trash(self, num):
        """Allows the player to trash up to num cards from their hand"""
        while num > 0 and len(self.hand) > 0:
            print("\nCurrent hand:  {}".format(self.hand))
            card_str = input("Choose a card to trash (leave blank if you do not wish to trash)\n")
            if not card_str:
                break
            try:
                card = eval(card_str)
            except Exception as e:
                print("No such card {}.".format(card))
                continue
            try:
                self.trash_from_hand(card)
            except HandError as e:
                print(e)
                continue
            print("Trashed {}.".format(card))
            num -= 1
            
    
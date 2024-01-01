import random
from cards import *
from errors import *
from players import Player


class AiPlayer(Player):
    def __init__(self, game_space, custom_deck=None, evaluator=None, suppress_logging=False):
        super().__init__(game_space, custom_deck, suppress_logging)
        self.evaluator = evaluator
        self.suppress_logging = suppress_logging

    def play_card(self, card):
        if not self.suppress_logging:
            print(f"{self} plays a {card}")
        super().play_card(card)

    def buy(self, card):
        if super().buy(card) and not self.suppress_logging:
            print(f"{self} buys a {card}")

    def end_turn(self):
        if self.evaluator:
            self.evaluator.evaluate_turn(self)
        super().end_turn()


class RandomAgent(AiPlayer):
    next_id = 0

    def __init__(self, game_space, **kwargs):
        super().__init__(game_space, **kwargs)
        self.id = RandomAgent.next_id
        RandomAgent.next_id += 1

    def __repr__(self):
        return f"RandomAgent {self.id}"

    def __str__(self):
        return f"RandomAgent {self.id}"

    def currently_held_action_cards(self):
        """Returns a list of all action cards currently in hand."""
        # TODO(optimization): Can be cached as long as hand is not changed.
        return list(filter(lambda card: isinstance(card, Action), self.hand))

    def take_turn_impl(self):
        # Action phase
        # Play all actions in random order
        while self.available_actions > 0:
            action_cards = self.currently_held_action_cards()
            if not action_cards:
                break
            random.shuffle(action_cards)
            self.play_card(action_cards[0])

        # Buy phase
        # Play all treasures
        treasures_in_hand = list(filter(lambda card: isinstance(card, Treasure), self.hand))
        random.shuffle(treasures_in_hand)
        for treasure_card in treasures_in_hand:
            self.play_card(treasure_card)
        # Don't buy anything
        return

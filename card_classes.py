class Card(object):
    def __init__(self, name, cost):
        self.cost = cost
        self.name = name

    def __repr__(self):
        return self.name
        
    def __str__(self):
        return self.name
        

class Treasure(Card):
    def __init__(self, name, cost, value, effect=lambda player: None):
        super().__init__(name,cost)
        self.plus_money = value
        self.effect = effect

class VictoryValued(Card):
    def __init__(self, name, cost, value):
        super().__init__(name, cost)
        self.victory_points = value

class Victory(VictoryValued):
    pass

class Action(Card):
    def __init__(self, name, cost, plus_money=0, plus_cards=0, plus_actions=0, plus_buys=0, effect=lambda player: None):
        super().__init__(name,cost)
        self.plus_money = plus_money
        self.plus_cards = plus_cards
        self.plus_actions = plus_actions
        self.plus_buys = plus_buys
        self.effect = effect
        
class ActionDuration(Action):
    def __init__(self, name, cost, plus_money=0, plus_cards=0, plus_actions=0, plus_buys=0, effect=lambda player: None, 
                duration_money=0, duration_cards=0, duration_actions=0, duration_buys=0, duration_effect=lambda player: None):
        super().__init__(name, cost, plus_money, plus_cards, plus_actions, plus_buys, effect)
        self.duration_money = plus_money
        self.duration_cards = plus_cards
        self.duration_actions = plus_actions
        self.duration_buys = plus_buys
        self.duration_effect = duration_effect
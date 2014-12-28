# This file will contain all the non-kingdom cards

def copper(player):
    player.buying_power += 1

def silver(player):
    player.buying_power += 2
    
def gold(player):
    player.buying_power += 3
    
def platinum(player):
    player.buying_power += 5
    
def potion(player):
    player.available_potions += 1
    
# basic_victory_cards = {"estate": 1, "duchy": 3, "province": 6, "colony": 10}
nonkingdom_victory_point_cards = {"curse": lambda x: -1}
nonkingdom_victory_point_cards["estate"] = lambda x: 1
nonkingdom_victory_point_cards["duchy"] = lambda x: 3
nonkingdom_victory_point_cards["province"] = lambda x: 6
nonkingdom_victory_point_cards["colony"] = lambda x: 10
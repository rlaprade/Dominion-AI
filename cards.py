# This file will contain all the non-kingdom cards and import all kingdom cards
from card_classes import *
from dominion_base_set import *
from seaside import *

### Treasure Cards ###
copper = Treasure('copper', 0, 1)        
silver = Treasure('silver', 3, 2)
gold = Treasure('gold', 6, 3)
platinum = Treasure('platinum', 9, 5)
# def platinum(player):
    # player.buying_power += 5
    
# def potion(player):
    # player.available_potions += 1
    
    
### Victory(ish) Cards ###
curse = VictoryValued('curse', 0, -1)
estate = Victory('estate', 2, 1)
duchy = Victory('duchy', 5, 3)
province = Victory('province', 8, 6)
colony = Victory('colony', 11, 10)

# basic_victory_cards = {"estate": 1, "duchy": 3, "province": 6, "colony": 10}
# nonkingdom_victory_point_cards = {"curse": lambda x: -1}
# nonkingdom_victory_point_cards["estate"] = lambda x: 1
# nonkingdom_victory_point_cards["duchy"] = lambda x: 3
# nonkingdom_victory_point_cards["province"] = lambda x: 6
# nonkingdom_victory_point_cards["colony"] = lambda x: 10

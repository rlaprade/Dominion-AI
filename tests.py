import game
import players
from cards import *
from tools import *
from errors import *

blank_space = game.GameSpace(1, [])
a = players.Player(blank_space)
a.hand = [copper, copper, copper, copper, estate]
a.play_card(copper)
assert(a.buying_power == 1)
assert(len(a.hand) == 4)
a.trash_from_hand(estate)
assert(estate not in a.hand)
assert(estate in blank_space.trash)
try:
    a.play_card(silver)
except HandError as e:
    assert(str(e) == "No silver in hand.")
try:
    a.trash_from_hand(silver)
except HandError as e:
    assert(str(e) == "No silver in hand.")

#test buying, test supply error

p1 = players.Player(None)
p1.hand = [wharf, copper, copper, copper, copper]
p1.play_card(wharf)
assert(len(p1.hand) == 6)
assert(wharf in p1.played)
p1.end_turn()
p1.duration_effects()
assert(len(p1.hand) == 7)
assert(wharf in p1.played)
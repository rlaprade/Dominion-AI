import game
import players
from cards import *

p1 = players.Player(None)
p1.hand = [wharf, copper, copper, copper, copper]
p1.play_card(wharf)
assert(len(p1.hand) == 6)
assert(wharf in p1.played)
p1.end_turn()
p1.duration_effects()
assert(len(p1.hand) == 7)
assert(wharf in p1.played)
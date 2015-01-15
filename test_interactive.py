import game
import players
from cards import *

kingdom_cards = [chapel, smithy, wharf]

game_space = game.GameSpace(1, kingdom_cards)
p1 = players.HumanNoCards(game_space, "p1")
game_space.players.append(p1)
game_space.play()
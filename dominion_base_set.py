from card_classes import *

chapel = Action("chapel", 2, effect = lambda player: player.voluntary_trash(4))
smithy = Action("smithy", 4, plus_cards=3)

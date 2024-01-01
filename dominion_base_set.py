from card_classes import *

chapel = Action("chapel", 2, effect = lambda player: player.voluntary_trash(4))
festival = Action("festival", 5, plus_money=2, plus_actions=2, plus_buys=1)
smithy = Action("smithy", 4, plus_cards=3)
woodcutter = Action("woodcutter", 3, plus_money=2, plus_buys=1)
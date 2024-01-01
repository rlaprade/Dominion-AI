import unittest
import game
from ai_agents import RandomAgent
from dominion_base_set import festival, woodcutter


class MyTestCase(unittest.TestCase):
    def test_play_all_festivals(self):
        blank_space = game.GameSpace(1, [])
        agent = RandomAgent(blank_space, custom_deck=[festival, festival, festival, festival, festival])
        agent.take_turn()  # add assertion here


if __name__ == '__main__':
    unittest.main()

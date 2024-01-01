import unittest
import game
from ai_agents import RandomAgent
from dominion_base_set import festival, woodcutter
from evaluator import BuyingPowerEvaluator


class MyTestCase(unittest.TestCase):
    def test_play_all_festivals(self):
        blank_space = game.GameSpace(1, [])
        agent = RandomAgent(blank_space, custom_deck=[festival, festival, festival, festival, festival])
        agent.take_turn()

    def test_sim_1000(self):
        evaluator = BuyingPowerEvaluator()

        for i in range(1000):
            blank_space = game.GameSpace(1, [])
            agent = RandomAgent(blank_space, custom_deck=[festival, festival, woodcutter, woodcutter, woodcutter],
                                evaluator=evaluator, suppress_logging=True)
            agent.take_turn()

        evaluator.print_stats()


if __name__ == '__main__':
    unittest.main()

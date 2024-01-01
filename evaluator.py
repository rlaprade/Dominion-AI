from players import Player


class Evaluator(object):
    def evaluate_turn(self, player: Player) -> None:
        return

    def print_stats(self):
        print("Base evaluator class tracks no stats")


class BuyingPowerEvaluator(Evaluator):
    def __init__(self):
        self.turn_count = 0
        self.total_buying_power = 0
        self.buying_power_per_turn = []

    def evaluate_turn(self, player: Player) -> None:
        self.turn_count += 1
        self.total_buying_power += player.buying_power
        self.buying_power_per_turn.append(player.buying_power)

    def average_buying_power(self):
        return self.total_buying_power / float(self.turn_count)

    def max_buying_power(self):
        return max(self.buying_power_per_turn)

    def min_buying_power(self):
        return min(self.buying_power_per_turn)

    def print_stats(self):
        print(f"num_turns: {self.turn_count}\n"
              f"average_buying_power: {self.average_buying_power()}\n" +
              f"max_buying_power: {self.max_buying_power()}\n"
              f"min_buying_power: {self.min_buying_power()}\n")

import players

class GameSpace(object):
    def __init__(self, num_players, kingdom_cards):
        self.supply = Counter()
        self.num_players = num_players
        self.players = []
        
        for card in kingdom_cards:
            self.supply[card] = 10
        
        self.supply["copper"] = 60 - 7*self.num_players
        self.supply["silver"] = 40
        self.supply["gold"] = 30
        self.supply["estate"] = 24 - 3*self.num_players
        self.supply["duchy"] = 8 if self.num_players<=2 else 12
        self.supply["province"] = 8 if self.num_players<=2 else 12
        self.supply["curse"] = 10*(self.num_players - 1)
        
    def sell(self, card):
        """Method for when a player attempts
        to buy the given card.  Raises an 
        exception if none available.
        """
        if self.supply[card] <= 0:
            raise Exception("No {} cards remaining in supply".format(card))
        self.supply[card] -= 1
        
    def play(self):
        """Call this method to begin the game!"""
        current_player = 0
        while not self.game_is_over():
            self.players[current_player].take_turn()
            current_player = (current_player + 1) % self.num_players
            
        scores = [(i+1, self.players[i].victory_points) for i in range(self.num_players)]
        scores.sort(key=lambda x: -x[1])
        print("The final scores are: \n")
        for score in scores:
            player = self.players[score[0]-1]
            if isinstance(player, players.HumanPlayer):
                tag = player.name
            else:
                tag = "AI player"
            print("Player {}: {}  ({})".format(score[0], score[1], tag))
            
    def game_is_over(self):
        """Return True if the game ends
        i.e. No provinces left or 3 piles empty
        """
        if self.supply["province"] == 0:
            return True
        empty_piles = 0
        for card in self.supply:
            if self.supply[card] == 0:
                empty_piles += 1
        if empty_piles >= 3:
            return True
        return False
        
        
class Counter(dict):
    """The Counter class is a dictionary that will
    give zero for keys that are not in the dictionary,
    rather than raising an error.
    """
    
    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        return 0
    
    
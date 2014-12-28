import game
import players

while True:
    human_players = input("How many human players? ")
    ai_players = input("How many computer players? ")
    try:
        human_players = int(human_players)
        ai_players = int(ai_players)
        break
    except ValueError:
        print("Please give integer numbers\n")
    
num_players = human_players + ai_players
    
if ai_players > 0:
    while True:
        valid = True
        ai_seats = input("Please give the turn orders of the computer players, separated by spaces (i.e. 1 2 if you wish for the computer players to go first and second)").split()
        if len(ai_seats) != ai_players:
            print("Seat ordering does not match number of computer players")
            continue
        for i in range(len(ai_seats)):
            try:
                ai_seats[i] = int(ai_seats[i])
            except ValueError:
                print("Invalid input\n")
                valid = False
                break
        if valid:
            break
else:
    ai_seats = []
            
names = {}
for i in range(1, num_players+1):
    if i in ai_seats:
        names[i] = input("Which AI agent should be used for Player {}?\n".format(i))
    else:
        names[i] = input("Player {}, what is your name?\n".format(i))
            
kingdom_cards = []
while True:
    for _ in range(10):
        kingdom_cards.append(input("Give the name of a kingdom card to play with:  "))
    print("\nKingdom cards are: {}".format(kingdom_cards))
    while True:
        correct = input("Is this correct? (yes or no)")
        if correct not in ["yes", "no"]:
            continue
        break
    if correct == "yes":
        break
        
game_space = game.GameSpace(num_players, kingdom_cards)
for i in range(1, num_players+1):
    if i in ai_seats:
        game_space.players.append(eval("players.{}".format(names[i]))(game_space))
    else:
        game_space.players.append(players.HumanPlayer(game_space,names[i]))
game_space.play()
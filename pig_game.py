#PIG game -> roll until you get '1' otherthan '1' you add to points
# Modified version 
    # If player pick 'No' score saved for the player's next round 
    # players only loose points if they rolled '1' ONLY
    # Max score is hard coded to 50
import random

# Dice function roll to 1-6
def roll():
    min_val = 1
    max_val = 6

    roll_value = random.randint(min_val,max_val)
    return roll_value

#Get no of players as a input
while True:
    player = input("Enter No. of players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2<= player <= 4:
            break
        else:
            print("Players must be between 2 -4 ")
    else:
        print("Invalid, Try again")


max_score =50
player_score = [0 for _ in range(player)]
current_score = [0 for _ in range(player)]

#Game Logics
while max(player_score) < max_score:
    
    for player_index in range(player):
        print(f"\n Player {player_index+1}'s turn \n")
        print("Your current score is - ",player_score[player_index])

        while True:

            get_roll = input("Would you like to roll (y/n or 'e' to exit)? ")
            if get_roll.lower() == "e":
                exit(f"Player {player_index+1} exit the game")

            if get_roll.lower() != "y":
                player_score[player_index] = current_score[player_index] #if player pick no it stores players score
                break
            
            value = roll()
            if value == 1:
                print("You Roll 1, turn over")
                current_score[player_index] = 0
                break
            else:
                current_score[player_index] += value
                print(f"You rolled - {value}") 
            
            print("Your score is - ", current_score[player_index])
        
        player_score[player_index] = current_score[player_index]
        print("Your total score is - ", player_score[player_index])

max_score = max(player_score)
winner_index = player_score.index(max_score)

print(f"Player {winner_index+1} is the winner")

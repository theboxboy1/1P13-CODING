
import random


def look_away(first_move, second_move, third_move):
    points = 0

    for round_num in range(3): # Loops over three times for three rounds
        # Assigns the correct player move based on the round
        if round_num == 0:
            player_move = first_move
        elif round_num == 1:
            player_move = second_move
        else: 
            player_move = third_move

        print(f"///////ROUND {round_num+1}/3 ///////\n")
        print(f"YOUR MOVE: {player_move}")

        cpu1 = random.randint(1, 4)
        cpu2 = random.randint(1, 4)
        print(f"CPU1 Move: {cpu1}")
        print(f"CPU2 Move: {cpu2}")

        if player_move != cpu1 and player_move != cpu2:
            print("***HUMAN WINS***\n")
            points += 10
        else:
            print("***CPU WINS***\n")

    return points

    

import random

def slot_machine(bet):
    emoji_1 = "\U0001F40D"
    emoji_2 = "\U0001F98D"
    emoji_3 = "\U0001F352"
    emoji_4 = "\U0001F697"

    # Build emoji string and print symbols
    emoji_string = ""
    for _ in range(3):
        n = random.randint(1, 4)
        if n == 1:
            emoji_string += "1"
            print(emoji_1, end="")
        elif n == 2:
            emoji_string += "2"
            print(emoji_2, end="")
        elif n == 3:
            emoji_string += "3"
            print(emoji_3, end="")
        else:
            emoji_string += "4"
            print(emoji_4, end="")
    print()

    # Counts duplicate emojis
    num_copies = 0
    counted = ""  # Concatenates already counted numbers to an empty string
    for i in emoji_string:
        count_for_i = 0
        for j in counted:
            if i == j:
                count_for_i += 1  # Add 1 for each duplicate emoji number
        num_copies += count_for_i
        counted += i  # remember this number

    # Determine winnings
    if num_copies == 3:       # Three duplicate emojis returns 5x bet
        return 5*bet
    elif num_copies == 2:     # Two duplicate emojis returns 2x bet
        return 2*bet
    else:
        return 0

    
#print(slot_machine(1))
        
        


def pig_dice(threshold):

    total = 0
    
    while total < threshold:
    
        roll_1 = random.randint(1,6)
        roll_2 = random.randint(1,6)
        total += roll_1+roll_2
        print(f"({roll_1}, {roll_2})", sep =" ", end= "")
        
    if roll_1 == 1 or roll_2 == 1:
        return "Loss"
    elif roll_1 ==1 and roll_2 == 1:
        return "Castastrophic loss"
    return f".Win ({total})"


def games_room(name):
    print("XXXX MAIN MENU XXXXX")
    print(f"What game would you like to play {name}?")
    game = int(input("1- Look Away\n2- Slot Machine\n3- Pig Dice\n"))
    while type(game) == int and 1<=game<=3:
        if game == 1: #Look Away Game
            first_move = 0
            second_move = 0
            third_move = 0 # Placeholders for each move
            
            for i in range(3):
                move = int(input("Input move: "))
                if i == 0:
                    first_move = move
                elif i == 1:
                    second_move = move
                else:
                    third_move = move   # For each round, the move is saved because i in range(3) goes through 0,1,2

                    return look_away(first_move,second_move,third_move)
        if game == 2: # Slot Machine
            bet = int(input("Enter your bet: "))
            return print(slot_machine(bet))
        
        else: # Pig Dice
            threshold = int(input("Enter threshold: "))
            return print(pig_dice(threshold))
    print("Enter A Valid Number! (1-3)") # If not a valid input as per the while loop above, it will ask user for a valid number
        

games_room("zak")

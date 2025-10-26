
import random

#### GAMES
def look_away(first_move, second_move, third_move):
    points = 0

    for round_num in range(3):
        
        if round_num == 0: # round_num starts at 0 due to range(3) indexing starting at 0
            player_move = first_move
        elif round_num == 1:
            player_move = second_move
        else:
            player_move = third_move

        cpu1 = random.randint(1, 4)
        cpu2 = random.randint(1, 4)

        # Determine winner
        if player_move != cpu1 and player_move != cpu2:
            winner = "HUMAN"
            points += 10
        else:
            winner = "CPU"

        print(f"Round {round_num+1}: CPU1 = {cpu1}, CPU2 = {cpu2}, Player = {player_move}, Winner: {winner}")

    return points




def slot_machine(bet):
    """
    Simulates a slot machine spin and returns the amount won.
    Parameters: bet (int) - the amount wagered for the spin.
    Return: int - payout based on matching symbols (0, 2*bet, or 5*bet).
    Output: Prints three randomly selected emoji symbols to the console.
    
    """
    
    emoji_1 = "\U0001F40D"  # Unicode for emoji
    emoji_2 = "\U0001F98D"
    emoji_3 = "\U0001F352"
    emoji_4 = "\U0001F697"

    # Build emoji string and print symbols
    emoji_string = "" # Stores the number values of the rolled emojis
    for _ in range(3):
        n = random.randint(1, 4)
        if n == 1: # Stores the associated emoji number in "emoji_string"
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
    
    
    first = ""   
    second = "" # This initializes the second and first number of the emoji string respectively
    first_count = 0
    second_count = 0
    
    # This first part is checking if the first digit of "emoji_string" matches with any digits
    for digit in emoji_string: # Parsing through each digit in the emoji string of rolled emojis (ex. "112" parses through "1","1","2")
        if first == "" or digit == first:
            first = digit # Sets "first" to the string, "digit". ("digit" is actually a string number... ex. "3") 
            first_count += 1  # Adds 1 to the count if the digit is found again, will always start at 1 as the digit will always inherently occur at least once
        
        elif second == "" or digit == second: # If the first digit does not match with any other digit, it will move on to checking the second digit
            second = digit # Sets "second" string to the digit 
            second_count += 1 
    
    num_copies = 0
    if first_count > 1: # If the first digit of "emoji_string" occurs more than once, then the total number of times that digit occurs is how many duplicate symbols there are
        num_copies += first_count # Therefore, add "first_count" to the number of copies
    if second_count > 1: # The same logic applies to the second digit (i.e if it occurs only once, then there are NO duplicates)
        num_copies += second_count
    
    # Determine winnings
    if num_copies == 3:       # Three duplicate emojis returns 5x bet
        print(f" ({5*bet} points)")
        return 5*bet
    elif num_copies == 2:     # Two duplicate emojis returns 2x bet
        print(f" ({2*bet} points)")
        return 2*bet
    else:
        print(" (0 points)")
        return 0



def pig_dice(threshold):
    """
    Rolls two dice repeatedly until the total sum of the dice rolls reaches the threshold set by the user.
    Parameters: threshold (int) - the minimum score needed to stop rolling.
    Return: str - the outcome of the game: "Loss", "Catastrophic loss", or f"Win ({total})".
    Output: Prints each dice roll as it occurs.
    """

    total = 0
    print("Rolls: ", end = "") 
    while total < threshold: # Total being greater than threshold means the game is won
    
        roll_1 = random.randint(1,6)
        roll_2 = random.randint(1,6)
        total += roll_1+roll_2
       
        print(f"({roll_1}, {roll_2})", end= "")
        
    if roll_1 == 1 and roll_2 == 1:  # Two "1" rolls is a "catastrophic loss"
        print("Catastrophic Loss", end = "")
        return -1
    elif roll_1 ==1 or roll_2 == 1: # A singular "1" roll is a "loss"
        print("Loss", end = "")
        return 0
    print(f" WIN({total} points)", end = "")
    return total
    

#### GAMES ROOM 
def games_room(name):
    """
    Displays a menu of games and runs the selected game repeatedly until the user quits.
    Parameters: name (str) - the player's name displayed in prompts.
    Return: total_points (int) - total score after quitting.
    Output: Prints menus, results, and score updates throughout gameplay.
    """
    total_points = 0
    print(f"Welcome to the Games Room, {name}!")

    game_number = 0
    while game_number != 4: # 4 is the "Quit" option
        print(f"\nCURRENT SCORE: {total_points}")
        print("XXXX MAIN MENU XXXXX")
        print("1- Look Away\n2- Slot Machine\n3- Pig Dice\n4- Quit")

        game = int(input("Select a game: "))

        if game == 1:  # LOOK AWAY
            print("\n--- LOOK AWAY GAME ---")
            first = int(input("Input move #1: "))
            second = int(input("Input move #2: "))
            third = int(input("Input move #3: "))
            points = look_away(first, second, third)
            total_points += points

        elif game == 2:  # SLOT MACHINE
            print("\n--- SLOT MACHINE ---")
            print(f"You currently have {total_points} points.")
            bet = int(input("Enter your bet: "))

            if bet > total_points or bet < 1: # Check to see if user has enough points to make the requested bet, or if they bet an invalid number 
                print("Invalid bet! No game played.")
            else:
                total_points += -bet  # Bet amount is subtracted from the user's total points
                winnings = slot_machine(bet)
                total_points += winnings
                print(f"You won {winnings} points!")

        elif game == 3:  # PIG DICE
            print("\n--- PIG DICE ---")
            threshold = int(input("Enter threshold: "))
            result = pig_dice(threshold)

            if result == -1:
                print("Catastrophic loss! Score reset to 0.")
                total_points = 0
            else:
                total_points += result

        elif game == 4:  # QUIT
            print(f"\nThank you for playing!")
            return total_points

        else:  # INVALID MENU OPTION
            penalty = random.randint(1, 20)
            total_points += -penalty
            if total_points < 0: # If deducting the points will make the total score go to negative, it will instead just be set to zero
                total_points = 0
                penalty = 0 # Penalty will also be set to zero because it does not make sense to say you lost x amount of points and then still remain at 0 (this is moreso semantics than it is logic)
            print(f"Invalid choice! You lose {penalty} points.")

        
#### OUTPUT
def print_signature():
    return print(
        "------------------------------\n"
        "Name: Zakariya Yahmad\n"
        "Student Number: 400625734\n"
        "Program: Engineering 1\n"
        "ENG 1P13: Integrated Cornerstone Design Projects in Engineering\n"
        "Professor: Sam Scott\n"
        "Current Term: Fall 2025\n"
        "------------------------------"
    )


def main():
    print_signature()
    name = input("Enter your name: ")
    final_score = games_room(name)
    print(f"FINAL SCORE: {final_score}")

main()

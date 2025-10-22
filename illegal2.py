import random

def look_away(first_move, second_move, third_move):
    
    player_moves = [first_move, second_move, third_move]
    points = 0 # to count score

    for game in range(3):
        print(f"///////ROUND {game+1}/3 ///////\n")
        print(f"YOUR MOVE: {player_moves[game]}")

        cpu_moves = []  # reset each round
        for i in range(2):
            move = random.randint(1,4)
            cpu_moves.append(move)
            print(f"CPU{i+1} Move: {move}")

        # use the current player's move for this round
        player_move = player_moves[game]
        if player_move != cpu_moves[0] and player_move != cpu_moves[1]:
            print("***HUMAN WINS***\n")
            points+=10 # 10 points for winning
        else:
            print("***CPU WINS***\n")
    return print(points)


look_away(1,1,1)




def slot_machine(bet):
    
    symbols = ["\U0001F40D", "\U0001F98D", "\U0001F352", "\U0001F697"] # Emojis to be used written as unicode
    symbols_after_spin = [] # Empty list to store the symbols after spinning
    
    for i in range(3): # Loops over symbols three times to output three randomized symbols
        symbol_number = random.randint(1,4) 
        symbols_after_spin.append(symbols[symbol_number-1]) # Appends "new symbols" to "symbols_after_spin" based on randomized index number of original "symbols" list (This is the mechanism for "spinning" the slot machine )
    
    for symbol in symbols_after_spin:
        print(symbol, sep = " ", end = "") # Outputs the new symbols in a singular line
    print() # Same effect as using "\n" (Makes it so the outputted points are on their own seperate line)
        
    if symbols_after_spin[0] == symbols_after_spin[1]  == symbols_after_spin[-1]: # Checks to see if all symbols are the same
        return bet*5
    elif symbols_after_spin[0] == symbols_after_spin[1] or symbols_after_spin[0] ==symbols_after_spin[-1]: # Checks to see if two symbols are the same
        return bet*2
    return 0
        
    
#print(slot_machine(1))


def pig_dice(threshold):
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    total = roll_1+roll_2
    
    if total > threshold:
        print("WIN")
    elif roll_1 == 1 or roll_2 ==1:
        print("Loss")
    else:
        print("Castastrophic loss")

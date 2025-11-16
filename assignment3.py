
""" Mastermind

Name: Zakariya Yahmad
Student Number: 400625734

Program Description:

    In Mastermind, the player's mission is to crack a secret code made up of four 
    coloured pegs. After each guess, the player receives vital intel: 
    
    1. a RED token for every peg that is the correct colour in the correct spot
    
    2. a WHITE token for every peg that is the correct colour but hiding in the wrong 
    location
    
    3. No token means no match.


"""


import random

def new_code(filename, duplicates, n):
    
    """
    Generates a Mastermind code of n colours using a list of colours from a file.
    
    Parameters: 
        filename (str) - the name of the file containing available colours.
        duplicates (bool) - whether repeated colours are allowed in the code.
        n (int) - desired length of the generated code.
        
    Return: list - a list of n colours, or False if duplicates are not allowed and
                   there are not enough unique colours.
    Output: None.
    
    """
    ## Processing
    
    new_colors = []
    
    # read file lines into list
    with open(filename) as f:
        file = [line.strip() for line in f]
        
        
    # stores all colors onto "new_colors" list for easy access
    for color in file:
        new_colors.append(color)

    # in the case that there are not enough colors AND duplicates are not allowed
    if not duplicates and n > len(file):
        return False
    
    ## Logic
    
    # randomly remove a color until list length == n
    while len(new_colors) > n:
        delete = random.randint(0, len(new_colors) - 1)
        new_colors.pop(delete)
    
    # handle duplicates if not allowed
    if not duplicates:
        unique_colors = []
        for color in new_colors:
            if color not in unique_colors:
                unique_colors.append(color)   # appends a color from our original color list ("new_colors") until a duplicate color is encountered
            else:
                # replace the duplicate color with a random unique color
                replacement = random.choice(file)
                
                # keeps finding new replacement on the off chance that the replacement is the same color
                while replacement in unique_colors:
                    replacement = random.choice(file)
                unique_colors.append(replacement)
        new_colors = unique_colors # set unique colors to the new_colors list... no duplicates

    ## Error-handling
    
    # if list shorter than n (can happen if too many duplicates removed)
    while len(new_colors) < n:
        choice = random.choice(file)
        if duplicates or choice not in new_colors:  # will keep appending colors until list == n and will append only non-duplicate colors by checking the colors it previously appended to "new_colors"
            new_colors.append(choice) 
            
    ## Output
    return new_colors


def score_red(code, guess):
    
    """
    Calculates red tokens (correct colour in the correct position).
    Parameters:
        code (list) - the secret Mastermind code.
        guess (list) - the player's guessed sequence of colours.
    Return: str - (correct_position, positions) where positions is a list of True/False 
                    marking which positions match, and correct_position is the number of times a color is on a matching position. 
                    Returns "-1,[]" if list sizes are not the same.
    Output: None.
    """
    
    ## Processing and Error-checking
    
    correct_position = 0
    positions = []
    
    if len(code) != len(guess):  
        return f"-1,{positions}"   # will return -1, []  if code and guess are different sizes
    
    ## Logic 
    
    for i in range(len(code)):  # if the index of a guess corresponds to the same index on the "code" list, the "positions" list will be updated to show that (i.e by appendng True)
        if code[i] == guess[i]:
            positions.append(True)
            correct_position += 1
        else:
            positions.append(False)
            
    ## Output
    return f"{correct_position},{positions}"



def score_white(code, guess, redlist):
    
    """
    Calculates white tokens (correct colour, wrong position) excluding red matches.
    
    Parameters:
        code (list) - the secret code, modified to remove red matches.
        guess (list) - the player's guess, also modified to remove red matches.
        redlist (list) - boolean list marking positions already matched as red.
        
    Return: int - number of white tokens awarded, or -1 if input lengths differ.
    
    Output: None.
    
    """
    ## Processing and Error-checking
    
    if not (len(code) == len(guess) == len(redlist)):  # checks to make sure all lists are of same length
        return -1

    # replaces all colors that are on correct positions with "", basically deleting them while keeping each list size the same
    for i in range(len(guess)):
        if redlist[i] == True:
            code[i] = ""
            guess[i] = ""  

    ## Logic
    
    sum_white = 0
    
    for color in guess:
        if color != "" and color in code:  # checks to see if color exists in the code, that way we know it is a correct color
            sum_white += 1 
            code.remove(color) #the color we found is removed to prevent duplicates
            
    ## Output
    return sum_white

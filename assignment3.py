import random

def new_code(filename, duplicates, n):
    new_colors = []
    
    # Read file lines into list
    with open(filename) as f:
        file = [line.strip() for line in f]
    
    for color in file:
        new_colors.append(color)

    # not enough colors and duplicates not allowed
    if not duplicates and n > len(file):
        return False

    # randomly remove until list length == n
    while len(new_colors) > n:
        delete = random.randint(0, len(new_colors) - 1)
        new_colors.pop(delete)
    
    # Handle duplicates if not allowed
    if not duplicates:
        unique_colors = []
        for color in new_colors:
            if color not in unique_colors:
                unique_colors.append(color)
            else:
                # replace with a random unique color
                replacement = random.choice(file)
                # keeps finding new replacement on the off chance that the replacement is the same color
                while replacement in unique_colors:
                    replacement = random.choice(file)
                unique_colors.append(replacement)
        new_colors = unique_colors # set unique colors to the new_colors list... no duplicates    

    # if list shorter than n (can happen if too many duplicates removed)
    while len(new_colors) < n:
        choice = random.choice(file)
        if duplicates or choice not in new_colors:
            new_colors.append(choice)

    return new_colors


def score_red(code, guess):
    ...
    


def score_white(code, guess, redlist):
    ...





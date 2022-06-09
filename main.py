# Rock, Paper and Scissors Game

# *** Rules ***
# Tie = Computer and Player 1 pick same option
# Win = Rock beats Scissors
# Win = Paper beats Rock
# Win = Paper beats Rock

import random

options = ["R","P","S"]

def playgame():
    print("R")
    print("P")
    print("S")
    playeroption = str(input("Pick a game character\n"))

    computeroption = random.choice(options)

# Player picks Rock and computer picks Rock
    if(playeroption == options[0] and computeroption == options[0]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("It is a tie, please start again")
        playgame()

# Player picks Paper and computer picks Paper
    elif(playeroption == options[1] and computeroption == options[1]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("It is a tie, please start again")
        playgame()

# Player picks Scissors and computer picks Scissors
    elif(playeroption == options[2] and computeroption == options[2]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("It is a tie, please start again")
        playgame()

# Player picks Rock and computer picks Scissors
    elif(playeroption == options[0] and computeroption == options[2]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("Player Wins")
        exit()

# Player picks Paper and computer picks Rock
    elif(playeroption == options[1] and computeroption == options[0]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("Player Wins")
        exit()

# Player picks Scissors and computer picks Paper
    elif(playeroption == options[2] and computeroption == options[1]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("Player Wins")
        exit()

# Computer picks Rock and Player picks Scissors
    elif(playeroption == options[2] and computeroption == options[0]):
        print("Player picks (%s)" % playeroption)
        print("CPU  picks (%s)" % computeroption)
        print("CPU Wins")
        exit()

# Computer picks Paper and Player picks Rock
    elif(playeroption == options[0] and computeroption == options[1]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("CPU Wins")
        exit()

# Player picks Scissors and computer picks Paper
    elif(playeroption == options[1] and computeroption == options[2]):
        print("Player picks (%s)" % playeroption)
        print("CPU picks (%s)" % computeroption)
        print("CPU Wins")
        exit()

    else:
        print("Your option should not be a Small Letter or Number, please try again")
        playgame()


# Initialize and run the function
playgame()
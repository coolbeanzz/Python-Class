#Author: Robert Murphy
#Date: 9/26
#Mod3 2nd assignment
#Purpose: plays coin flip

import random
import time

print("Welcome to coin flip!")
print("If you and the computer match numbers you win, if you and the computer guess different, you lose!")

ready = input("Are you ready to play? Enter Y or N: ")
if ready.upper() == "N":
    print("See you next time!")
elif ready.upper() != "N" and ready.upper() != "Y":
    print("Please enter Y or N next time!")

win_count = 0
com_wins = 0
total_games = 0

while ready.upper() == "Y":
    print("The computer has chose its number!")
    user = input("Please enter a 0 or 1 to see if you win!: ")

    try:
        num = int(user)
    except ValueError:
        print("Please put in either 0 or 1!")

    if num != 0 and num != 1:
        print("Please put in a 0 or 1!")
    else:
        x = int(random.randint(0, 1))
        print("The computer selected: ", x)
        if num == 1 and x == 1:
            print("You Win!!!")
            win_count += 1
        elif num == 0 and x == 0:
            print("You Win!!!")
            win_count += 1
        else:
            print("You Lose!")
            com_wins += 1

    time.sleep(2)
    print()
    print("You have won", win_count, "times!")
    print("Computer has won", win_count, "times!")

    total_games += 1
    print("You have played", total_games, "times!")
    print()
    time.sleep(2)
    ready = input("Do you want to play again? Y or N: ")
    if ready.upper() != "N" and ready.upper() != "Y":
        print("Please enter Y or N next time!")

#authors: Robbie Murphy, Avery Corcoran
#Date: 3/2/22
#Purpose: Teach Avery how to code inputs and print statements

import pyfiglet
import datetime as datetime #Avery will code this section
import time #Avery will code this

#Avery and I will code a function that plays rock paper scissor shoot
#Avery will code a function that prints out the date but is delayed by a specific time

def input_banner(word):
    ascii_banner = pyfiglet.figlet_format(word)
    print(ascii_banner)

def RPSS():
    player1 = "Bert"
    player2 = "Avery"
    play = 'Y'
    a_win = 0
    r_win = 0
    while play == 'Y':
        move1 = input("Bert enter your play!: ")
        print()
        move2 = input("Avery enter your move!: ")
        print()
        if move1 == "rock" and move2 == "rock":
            print("Tie")
        elif move2 == "paper" and move1 == "paper":
            print("Tie")
        elif move1 == "scissor" and move2 == "scissor":
            print("Tie")
        elif move1 == "rock" and move2 == "scissor":
            print(player1, "Wins!")
            r_win += 1
        elif move2 == "rock" and move1 == "scissor":
            print(player2, "Wins!")
            a_win += 1
        elif move1 == "rock" and move2 == "paper":
            print(player2, "Wins!")
            a_win += 1
        elif move2 == "rock" and move1 == "paper":
            print(player1, "Wins!")
            r_win += 1
        elif move1 == "scissor" and move2 == "paper":
            print(player1, "Wins!")
            r_win += 1
        elif move1 == "scissor" and move2 == "paper":
            print(player1, "Wins!")
            r_win += 1
        elif move1 == "scissor" and move2 == "rocks":
            print(player2, "Wins!")
            a_win += 1
        elif move1 == "rock" and move2 == "paper":
            print(player2, "Wins!")
            a_win += 1
        elif move1 == "paper" and move2 == "rock":
            print(player1, "Wins!")
            r_win += 1
        elif move1 == "paper" and move2 == "scissor":
            print(player2, "Wins!")
            a_win += 1
        elif move1 == "scissor" and move2 == "paper":
            print(player1, "Wins!")
            r_win += 1

        print("Avery has ", a_win, "wins!")
        print("Bert has ", r_win, "wins!")
        if (r_win > a_win):
            print("bert has more wins")
        else:
            print("Avery has more wins")

        play = input("Do you want to play again? Y or N: ")

def print_date():
    #ask user for num of seconds, do sleep, print out datetime.datetime.now()
    time_delay = int(input("How many sec should I enter?"))
    time.sleep(time_delay)
    print(datetime.datetime.now())



print("\n\nHello! Here's the Menu:\n")

menu = int(input("Please choose what you would like to do (1, 2, or 3): \n1:    Make an Ascii Art Banner\n" 
                 "2:    Rock, Papers, Scissor, Shoot!\n3:    Print the date\n"))

if menu == 1:
    word = input("Please enter a word you want to use: ")
    input_banner(word)
elif menu == 2:
    RPSS()
elif menu == 3:
    print_date()




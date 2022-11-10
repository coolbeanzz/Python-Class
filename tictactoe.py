#Author: RObert Murphy
#Date: 10/2/21
#Assignment 4
#purpose: play tic tac toe
import time
import random

def display_board(num_list):
        board = [["+-------+-------+-------+"],
                ["|", "     ", "|", "     ", "|", "     ", "|"],
                ["|", " ", num_list[0], " ", "|", " ", num_list[1], " ", "|", " ", num_list[2], "  |"],
                ["|", "     ", "|", "     ", "|", "     ", "|"],
                ["+-------+-------+-------+"],
                ["|", "     ", "|", "     ", "|", "     ", "|"],
                ["|", " ", num_list[3], " ", "|", " ", num_list[4], " ", "|", " ", num_list[5], "  |"],
                ["|", "     ", "|", "     ", "|", "     ", "|"],
                ["+-------+-------+-------+"],
                ["|", "     ", "|", "     ", "|", "     ", "|"],
                ["|", " ", num_list[6], " ", "|", " ", num_list[7], " ", "|", " ", num_list[8], "  |"],
                ["|", "     ", "|", "     ", "|", "     ", "|"],
                ["+-------+-------+-------+"]]

        for row in board:
                for col in row:
                        print(col, end=" ")
                print()

def enter_move(nums):
        user_num = int(input("Please input the square's number you would like to mark (1-9): "))

        if user_num in used:
                print("Sorry that spot has been marked already.")
                y = False
                while y != True:
                        user_num = int(input("Input the new square's number you would like to mark: "))
                        if user_num in used:
                                user_num = int(input("Already taken. Input the new square's number you would like to mark: "))
                                if user_num not in used:
                                        y = True
                        else:
                                y = True

        nums[user_num - 1] = "O"
        display_board(nums)
        used.append(user_num)


def victory_for(win, nums):
        if nums[0] == "O" and nums[1] == "O" and nums[2] == "O":
                print()
                print("You won!!!!!!")
                print()
                display_board(nums)
                win = 1
        if nums[6] == "O" and nums[7] == "O" and nums[8] == "O":
                print()
                print("You won!!!!!!")
                print()
                display_board(nums)
                win = 1
        if nums[0] == "O" and nums[3] == "O" and nums[6] == "O":
                print()
                print("You won!!!!!!")
                print()
                display_board(nums)
                win = 1
        if nums[2] == "O" and nums[5] == "O" and nums[8] == "O":
                print()
                print("You won!!!!!!")
                print()
                display_board(nums)
                win = 1
        # if comp wins
        if nums[0] == "X" and nums[3] == "X" and nums[6] == "X":
                print()
                print("Computer won")
                print()
                display_board(nums)
                win = 1
        if nums[3] == "X" and nums[4] == "X" and nums[5] == "X":
                print()
                print("Computer won")
                print()
                display_board(nums)
                win = 1
        if nums[0] == "X" and nums[4] == "X" and nums[8] == "X":
                print()
                print("Computer won")
                print()
                display_board(nums)
                win = 1
        if nums[2] == "X" and nums[4] == "X" and nums[6] == "X":
                print()
                print("Computer won")
                print()
                display_board(nums)
                win = 1
        if ((nums[0] == "X" or nums[0] == "O") and (nums[1] == "X" or nums[1] == "O") and \
                (nums[2] == "X" or nums[2] == "O") and (nums[3] == "X" or nums[3] == "O") and \
                (nums[4] == "X" or nums[4] == "O") and (nums[5] == "X" or nums[5] == "O") and \
                (nums[6] == "X" or nums[6] == "O") and (nums[7] == "X" or nums[7] == "O") and \
                (nums[8] == "X" or nums[8] == "O")):
                win = 2
                print()
                print("TIE!!!")
                print()

        return win

def draw_move(nums):
        x = False
        time.sleep(1)
        while x == False:
                comp_num = random.randint(1, 9)
                if comp_num in used:
                        comp_num = random.randint(1, 9)
                        if comp_num not in used:
                                x = True
                else:
                        x = True

        nums[comp_num - 1] = "X"
        used.append(comp_num)
        display_board(nums)


nums = ["1","2", "3", "4", "X", "6", "7", "8", "9"]
print("Welcome to Tic Tac Toe!")
print("You are O's the computer is X's. Computer goes first.")
display_board(nums)
time.sleep(1)
used = [5]
global win
win = 0
stop = 0
while win != 1 and win != 2:
        if stop != 1 and stop != 2:
                stop = victory_for(win, nums)
                if stop == 1 or stop == 2:
                        break
                if win != 2 and win != 1:
                        enter_move(nums)
        if stop != 1 and stop != 2:
                stop = victory_for(win, nums)
                if stop == 1 or stop == 2:
                        break
                if stop != 1 and stop != 2:
                        draw_move(nums)





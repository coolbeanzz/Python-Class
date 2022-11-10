#Author: Robert Murphy
#Date: 9/26
#Mod3 1st assignment
#Purpose: makes superS of different styles

print("Welcome to the Super S design center!")
user_char = input("Please enter the character you want for the design: ")

super = [[" "," ", user_char, " ", " "],
         [" ", user_char, " ", user_char, " "],
         [user_char, " "," "," ", user_char],
         [user_char, " ", user_char, " ", user_char],
         [user_char, " ", user_char, " ", user_char],
         [user_char, " ", user_char, " ", " "],
         [" ", user_char, " ", user_char, " "],
         [" ", " ", user_char, " ", user_char],
         [user_char, " ", user_char, " ", user_char],
         [user_char, " ", user_char, " ", user_char],
         [user_char, " ", " ", " ", user_char],
         [" ", user_char, " ", user_char, " "],
         [" ", " ", user_char, " ", " "]]

for row in super:
    for col in row:
        print(col, end=" ")
    print()



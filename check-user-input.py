# Author: Robert Murphy
# Date: 9/17/21
# Purpose: check user input

def check_input_int(input):
    try:
        #try converting to int
        num = int(input)
        return 0
    except ValueError:
        try:
            # see if its a float
            num = float(input)
            print("You put in a float, not a integer.")
            return 1
        except ValueError:
            print("You put in a string. Put in an Integer please.")
            return 1

#checks to see if the input has all letters or - in it
def check_string_input(input):
    word2 = input
    hyphen = "-"
    TorF = word2.isalpha()
    if TorF == True:
        return 0
    if TorF == False and hyphen in word2:
        return 0
    if TorF == False:
        print("The string must have all letters. No numbers, symbols, or spaces.")
        return 1



# will take in a name as a string and then print that name back on console
user_name = input("Please enter your name: ")
print("You have a cool name " + user_name + ".")
# In my opinion names can have numbers ( elon musk's kid)
print("------------------")

# will ask the user for an int and them * it by itself and then print to console
mult_num = input("Please enter a integer number: ")
if check_input_int(mult_num) == 0:
    print(mult_num, " * ", mult_num)
    print("Result:", int(mult_num) * int(mult_num))
    print("------------------")


#asks user for a word, counts num of letters, and then prints
user_word = input("Please enter a word: ")
if check_string_input(user_word) == 0:
    length_of_word = len(user_word)
    print("Your word is " + str(length_of_word) + " letters long.")
    print("------------------")

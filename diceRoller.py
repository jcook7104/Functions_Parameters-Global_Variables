#Dice roll program
#The code is designed to roll a dice and display it as a face of a dice

#### Importing random and time into my code ####
import time
import random

#### Dice Face ####
s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"


#### Defines the function roll() ####
def roll():
    print("rolling.....")
    roll = random.randint(1,6)
    return roll

#### This tells the code to show the number on the dice face #####
def show_dice(roll):
    print(roll)
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)

#print(roll)# This is here for debugging purposes

#### This keeps the code in an infinite loop until it rolls a 6 ####
while True:
    MyRoll = roll()
    time.sleep(1)
    show_dice(MyRoll)
    if MyRoll == 6:
        break


#### ERRORS I HAVE FOUND ####
# I had to get rid of syntax errors such as missing colons and a capitial p instead of a lower case p
# There where unexpected indent blocks where i had to tab code in
# The else statment had to be changed into elif
# On the elif statements there was only 1 equals sign on each of them but there had to be 2 equals to make sure it is equal to that number

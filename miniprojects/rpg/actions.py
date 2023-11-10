#!/usr/bin/env python3
# import necessary modules
from random import randint
import os

# function to roll dice based off the type and number passed
# if no arguments passed defaults to roll a single twenty sided die
def roll_dice(roll: str = "1d20"):
    roll: list[str, str] = roll.split('d')
    dice: list[int] = []
    for i in range(int(roll[0])):
         dice.append(randint(1,int(roll[1])))
    return sum(dice)

def showInstructions():
    """Show the game instructions when called"""
    #print a simple main menu and the commands for now. Needs expanded
    os.system("clear")
    print('''
    Jail Break
    ==========
    You awake in a prison cell and are unsure how you got there.
    Try to gain your freedom.
    Commands:
      move [direction]
      get [item]
      search
          *this examines your current location in more detail
    ''')
    input("Press Enter to continue")
    os.system("clear")

# main method to test functions
def main():
    print(roll_dice("3d6"))
    print(roll_dice())

if __name__ == "__main__":
	main()
#!/usr/bin/env python3
# import necessary modules
from random import randint
import entity
import os
from pprint import pprint

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
    The Escape
    ==========
    You awake in a prison cell and are unsure how you got there.
    Try to gain your freedom.
    Commands:
      move [direction]
      search
          *this examines your current location in more detail

    Players Stats
    =============
    Strength makes you do more damage (extra damage)
    Dexterity makes you harder to hit (extra armor class)
          * The bonus is equal to (stat - 10) / 2
            For example, a strenth of 14 will give +2 damage - (14 - 10) / 2
    ''')
    input("Press Enter to continue")
    os.system("clear")

# main method to test functions
def main():
    print(roll_dice("3d6"))
    print(roll_dice())

if __name__ == "__main__":
	main()
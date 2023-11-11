#!/usr/bin/env python3

from random import randint
import entity
import os
from pprint import pprint

def roll_dice(roll: str = "1d20"):
    """
    Simulates rolling a dice based on the input string.

    Parameters:
    - roll (str): A string in the format "NdM", where N is the number of dice and M is the number of sides.

    Returns:
    - int: The sum of the dice rolls.

    Example:
    >>> roll_dice("3d6")
    10
    """
    # Split the input string into number of dice and number of sides
    roll: list[str, str] = roll.split('d')
    dice: list[int] = []

    # Roll the dice and store the results in a list
    for i in range(int(roll[0])):
         dice.append(randint(1,int(roll[1])))
    return sum(dice)

def showInstructions():
    """
    Displays game instructions and player stats.
    """
    os.system("clear")
    # Display game instructions and information concerning player stats
    print('''
    The Escape
    ==========
    You awake in a prison cell and are unsure how you got there.
    Try to gain your freedom by reaching the exit
    
    Commands:
      move [direction]
          example: move north
      get [item]
          example: get broom
      use [item]
          example: use broom
      search
          this examines your current location in more detail

    Players Stats
    =============
    Strength makes you do more damage (extra damage)
    Dexterity makes you harder to hit (extra armor class) and
      easier for you to hit others
          * The bonus is equal to (stat - 10) / 2
            For example, a strenth of 14 will give +2 damage - (14 - 10) / 2
          
    Notes
    =====
    Beware of the monsters that will attempt to end your life
    ''')
    input("Press Enter to continue")
    os.system("clear")

def main():
    print(roll_dice("3d6"))
    print(roll_dice())

if __name__ == "__main__":
	main()
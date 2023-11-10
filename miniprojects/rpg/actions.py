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
    roll: list[str, str] = roll.split('d')
    dice: list[int] = []
    for i in range(int(roll[0])):
         dice.append(randint(1,int(roll[1])))
    return sum(dice)

def showInstructions():
    """
    Displays game instructions and player stats.

    Commands:
    - move [direction]
    - search (examines current location in more detail)

    Player Stats:
    - Strength: Makes you do more damage (extra damage)
    - Dexterity: Makes you harder to hit (extra armor class)
      - The bonus is equal to (stat - 10) / 2
        For example, a strength of 14 will give +2 damage - (14 - 10) / 2
    """
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
    Dexterity makes you harder to hit (extra armor class) and
      easier for you to hit others
          * The bonus is equal to (stat - 10) / 2
            For example, a strenth of 14 will give +2 damage - (14 - 10) / 2
    ''')
    input("Press Enter to continue")
    os.system("clear")

def main():
    print(roll_dice("3d6"))
    print(roll_dice())

if __name__ == "__main__":
	main()
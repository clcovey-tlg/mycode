#!/usr/bin/env python3
# import necessary modules
from random import randint

# function to roll dice based off the type and number passed
# if no arguments passed defaults to roll a single twenty sided die
def roll_dice(number: int = 1, type: int = 20):
    dice: list[int] = []
    for i in range(number):
         dice.append(randint(1,type))
    return dice

# main method to test functions
def main():
    print(roll_dice(3 , 6))
    print(roll_dice())

if __name__ == "__main__":
	main()
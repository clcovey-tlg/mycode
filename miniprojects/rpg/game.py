#!/usr/bin/env python3

# define necessary imports
from pprint import pprint #loaded during testing
import load_game_data
from location import location_status

# initialize global variables
locations = {}
player_dead = False
escaped = False


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    Jail Break
    ==========
    You awake in a prison cell and are unsure how you got there.
    Try to gain your freedom.
    Commands:
      go [direction]
      get [item]
      look [item]
    ''')

def main():
    showInstructions()
    locations = load_game_data.load_locations()
    load_game_data.load_entities(locations)
    location_status(locations, 'cell')
    locations

if __name__ == "__main__":
	main()
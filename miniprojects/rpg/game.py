#!/usr/bin/env python3

# define necessary imports
from pprint import pprint #loaded during testing
import load_game_data

# initialize global variables
locations = {}
player_dead = False
escaped = False


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')




def main():
    locations = load_game_data.load_locations()
    load_game_data.load_entities(locations)
    print(locations["guard room"]["entities"]["guard"].__str__())

if __name__ == "__main__":
	main()
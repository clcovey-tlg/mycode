#!/usr/bin/env python3

# define necessary imports
from pprint import pprint #loaded during testing
from location import load_locations, location_status, location_search
from generate_entity import generate_player, load_npcs
from actions import showInstructions
import os

# initialize global variables
locations = {}
npcs = {}
# two conditions checked for ending game
player_dead = False
escaped = False

def play_game(locations, npcs, player):
    # breaking this while loop means the game is over
    while not player_dead or not escaped:
        location_status(locations, player.location)

        # the player MUST type something in
        # otherwise input will keep asking
        user_input = ''
        while user_input == '':  
            user_input = input('>')

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]          
        user_input_list = user_input.lower().split(" ", 1)
        action = user_input_list[0]
        if len(user_input_list) > 1:
            article = user_input_list[1]

        #if they type 'move' first
        if action == 'move':
            connections = locations[player.location]["connections"]
            #check that they are allowed wherever they want to go
            if article in list(connections):
                #set the current room to the new room
                player.move(locations, connections[article])
            # if they aren't allowed to go that way:
            else:
                print("You can't go that way!")

        #if they type 'search' first
        if action == 'search':
            location_search(locations, player.location)
            # check that they are allowed wherever they want to go
            if player.location in ["empty cell"]:
                # if player location is empty cell it reveals the loose stone
                locations[player.location]["connections"]["south"] = "escape tunnel"
            # waits for enter to continue to allow user to read room details
            input("Press enter to continue")

        # #if they type 'get' first
        # if move[0] == 'get' :
        #     # make two checks:
        #     # 1. if the current room contains an item
        #     # 2. if the item in the room matches the item the player wishes to get
        #     if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #         #add the item to their inventory
        #         inventory.append(move[1])
        #         #display a helpful message
        #         print(move[1] + ' got!')
        #         #delete the item key:value pair from the room's dictionary
        #         del rooms[currentRoom]['item']
        #     # if there's no item in the room or the item doesn't match
        #     else:
        #         #tell them they can't get it
        #         print('Can\'t get ' + move[1] + '!')
        
        # ## If a player enters a room with a monster
        # if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        #     print('A monster has got you... GAME OVER!')
        #     break
        
        ## Define how a player can win
        if player.location == 'exit':
            print('You escaped the dungeon... YOU WIN!')
            escaped = True

        # clears screen between moves
        os.system("clear")

def main():
    # shows instructions. function from actions.py
    showInstructions()

    # loads game data from json and generates player from input
    locations = load_locations()
    #npcs = load_npcs(locations)
    player = generate_player()
    
    play_game(locations, npcs, player)
    
if __name__ == "__main__":
	main()
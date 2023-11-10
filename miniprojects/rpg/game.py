#!/usr/bin/env python3

# define necessary imports
from location import load_locations, location_status, location_search
from generate_entity import generate_player, load_npcs
from actions import showInstructions
from battle import battle
from format_txt import underline, make_blue

# initialize global variables
locations = {}
npcs = {}



def play_game(locations, npcs, player):
    # two conditions checked for ending game
    player_dead = False
    escaped = False
    # breaking this while loop means the game is over
    while not (player_dead or escaped):
        location_status(locations, player.location)

        # the player MUST type something in
        # otherwise input will keep asking
        user_input = ''
        while user_input == '':
            print(f"Actions: {make_blue('Move <direction>')}, {make_blue('Search')}")
            user_input = input('>')

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]          
        user_input_list = user_input.lower().split(" ", 1)
        action = user_input_list[0]
        if len(user_input_list) > 1:
            article = user_input_list[1]

        if action in list(locations[player.location]["connections"]):
            article = action
            action = "move"

        # displays a message if the 
        if action not in ["move", "search"]:
            print(f"{action} is not a valid option")
            input("Press enter to continue")

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
                input("Press enter to continue")

        #if they type 'search' first
        if action == 'search':
            location_search(locations, player.location)
            # if player location is empty cell it reveals the loose stone and escape tunnel
            if player.location in ["empty cell"]:
                locations[player.location]["connections"]["south"] = "escape tunnel"
            # waits for enter to continue to allow user to read room details
            input("Press enter to continue")

        # starts a battle if the player movies into a room with a monster
        if len(locations[player.location]["entities"]) > 0:
            location_status(locations, player.location)
            monster_name = list(locations[player.location]["entities"].keys())[0]
            monster = npcs[monster_name]
            player_dead = battle(player, monster, locations)

        ## Define how a player can win
        if player.location == 'exit':
            print('You escaped the dungeon... YOU WIN!')
            escaped = True

def main():
    # shows instructions. function from actions.py
    showInstructions()

    # loads game data from json and generates player from input
    locations = load_locations()
    npcs = load_npcs(locations)
    player = generate_player()
    
    play_game(locations, npcs, player)
    
if __name__ == "__main__":
	main()
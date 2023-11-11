#!/usr/bin/env python3

from location import load_locations, location_status, location_search
from generate_data import generate_player, load_npcs, load_items
from actions import showInstructions
from battle import battle
from format_txt import underline, make_blue
import os
from textwrap import fill

# initialize global variables
locations = {}
npcs = {}
items = {}

def play_game(locations, npcs, player, items):
    """
    Main function to play the game, handling user input and game progression.

    Parameters:
    - locations (dict): Dictionary containing information about game locations.
    - npcs (dict): Dictionary containing information about Non-Player Characters (NPCs).
    - player (Player): The player entity.

    Returns:
    - None
    """
    # two conditions checked for ending game
    player_dead = False
    escaped = False
    # breaking this while loop means the game is over
    while not (player_dead or escaped):
        location_status(locations, player.location)

        print()
        player.display()

        user_input = ''
        while user_input == '':
            print(f"\nActions: {make_blue('Move <direction>')}, {make_blue('Search')}, {make_blue('Get <item>')}, {make_blue('Use <item>')}")
            user_input = input('>')

        user_input_list = user_input.lower().split(" ", 1)
        action = user_input_list[0]
        article = ""
        if len(user_input_list) > 1:
            article = user_input_list[1]

        if action in list(locations[player.location]["connections"]):
            article = action
            action = "move"

        if action not in ["move", "search", "get", "use"]:
            print(f"{action} is not a valid option")
            input("Press enter to continue")

        if action == 'move':
            connections = locations[player.location]["connections"]
            if article in list(connections):
                player.move(locations, connections[article])
            else:
                print("You can't go that way!")
                input("Press enter to continue")

        if action == 'get':
            room_items = locations[player.location]["inventory"]
            if article in room_items:
                player.get_item(locations, items, article)
            else:
                print("I don't see that item!")
                input("Press enter to continue")

        if action == 'use':
            player_items = player.inventory
            if article in player_items and article == "thieves tools" and player.location == "hall":
                locations[player.location]["connections"]["north"] = "storeroom"
                os.system("clear")
                text = "With a practiced touch, the lockpicks from the thieves tools are inserted into the keyhole, their tips grazing the inner mechanisms with a delicate finesse. "
                text += "The faint sound of metal on metal reverberates through the stillness as the adventurer manipulates the tumblers, seeking that elusive alignment that will grant passage beyond the locked door. "
                text += "\n\nIn a moment of triumph, a satisfying click breaks the silence. The lock surrenders, its resistance overcome by your skillful hands."
                print(fill(text, width=50))
                input("Press enter to continue")
            else:
                print("I am not sure how to use that at this time!")
                input("Press enter to continue")

        if action == 'search':
            location_search(locations, player.location)
            searched = locations[player.location]["searched"]
            # if player location is empty cell it reveals the loose stone and escape tunnel
            if player.location in ["empty cell"] and searched == False:
                locations[player.location]["connections"]["south"] = "escape tunnel"
            if player.location in ["cell"] and searched == False:
                locations[player.location]["inventory"].append("thieves tools")
            if player.location in ["storeroom"] and searched == False:
                locations[player.location]["inventory"].append("longsword")
            locations[player.location]["searched"] = True
            # waits for enter to continue to allow user to read room details
            input("Press enter to continue")

            if action == 'get':
                items = locations[player.location]["inventory"]
                if article in list(connections):
                    player.move(locations, connections[article])
                else:
                    print("You can't go that way!")
                    input("Press enter to continue")

        # starts a battle if the player movies into a room with a monster
        if len(locations[player.location]["entities"]) > 0:
            location_status(locations, player.location)
            monster_name = list(locations[player.location]["entities"].keys())[0]
            monster = npcs[monster_name]
            player_dead = battle(player, monster, locations)

        ## Define how a player can win
        if player.location == 'exit':
            os.system("clear")
            location_search(locations, "exit")
            print('\nYou escaped the dungeon... YOU WIN!')
            input("Press enter to leave the game")
            escaped = True

def main():
    """
    Main function to initialize and play the game.
    """
    showInstructions()

    locations = load_locations()
    items = load_items(locations)
    npcs = load_npcs(locations)
    player = generate_player()
    
    play_game(locations, npcs, player, items)
    
if __name__ == "__main__":
	main()
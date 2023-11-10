#!/usr/bin/env python3

# needed imports
from requests import get
import time
import json
from actions import roll_dice
from entity import NPC
from entity import Player

# function to retrieve npc data from api
def get_npc_data(npc, location, damage):
    # build api url
    api_url = "https://www.dnd5eapi.co/api/monsters/" + npc

    # retrieve and parse npc data
    response = get(api_url)
    parsed_data = response.json()
    
    # instanciate npc and set attributes from parsed api data
    npc = NPC(location, damage)
    setattr(npc, "index", parsed_data["index"])
    setattr(npc, "name", parsed_data["name"])
    setattr(npc, "group", parsed_data["type"])
    setattr(npc, "max_hp", parsed_data["hit_points"])
    setattr(npc, "hp", parsed_data["hit_points"])
    setattr(npc, "strength", parsed_data["strength"])
    setattr(npc, "dexterity", parsed_data["dexterity"])
    setattr(npc, "ac", parsed_data["armor_class"][0]["value"])
    setattr(npc, "attack", parsed_data["actions"][0]["name"])

    return npc

def generate_npc(locations, npc, location, damage):
    npc = get_npc_data(npc, location, damage)
    locations[location]["entities"][npc.index] = npc.index

    return npc

def load_npcs(locations):
    with open("game_data.txt", "r") as data:
        #reads data file object as json
        game_data = json.load(data)
            
        # reads locations from game_data.txt and saves in a npcs dict
        npcs = {}
        for entry in game_data["npcs"]:
            index = entry["index"]
            location = entry["location"]
            damage = entry["damage"]
            npc = generate_npc(locations, index, location, damage)
            npcs[index] = npc
    return npcs

# generate Player name with input from user
def generate_player_name():
    # prompt for name
    name: str = ""
    acceptable: bool = False
    while not acceptable:
        name = input("Please enter your characters name: \n> ")
        print(f"You entered: {name}")
        accept = input("Press enter to change or enter 'yes' to keep this name\n> ").lower()
        if accept in ["yes", "ye", "y"]:
             acceptable = True
    return name

# generate player stats
def generate_player_stats(player):
    # rolls dice for stat values
    stats: list[int, int] = []
    acceptable: bool = False
    while not acceptable:
        stats = []
        print("Rolling dice. Please wait...")
        stats.append(roll_dice("3d6") + 3)
        stats.append(roll_dice("3d6") + 3)
        time.sleep(1)
        print(f"You rolled a {stats[0]} and a {stats[1]}")
        accept = input("Press enter to keep reroll or enter 'yes' to keep these rolls\n> ").lower()
        if accept in ["yes", "ye", "y"]:
             acceptable = True
    
    # allows player to assign stats to strength or dexterity
    choice: str = ""
    while choice not in ["1", "2"]:
        choice = input(f"Should roll 1 - {stats[0]} or  2 - {stats[1]} be strength?\n> ")
    if choice == "1":
        setattr(player, "strength", stats[0])
        setattr(player, "dexterity", stats[1])
    else:
        setattr(player, "strength", stats[1])
        setattr(player, "dexterity", stats[0])

# generate the Player object
def generate_player():
    name = generate_player_name()
    player = Player(name, "cell")
    generate_player_stats(player)

    return player

# main method for testing of function during testing
def main():
    # guard = get_npc_data("guard", "guard room", "1d6")
    # rat = get_npc_data("rat", "escape tunnel", "1d1")
    # skeleton = get_npc_data("skeleton", "escape tunnel", "1d6")
    # print(guard.__str__())

    player = generate_player()
    print(player)

    

if __name__ == "__main__":
	main()
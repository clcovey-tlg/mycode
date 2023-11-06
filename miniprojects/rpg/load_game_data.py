#!/usr/bin/env python3

# defines necessary imports
import json
from entity import NPC
from entity import Player
from pprint import pprint

def load_locations():
    with open("game_data.txt", "r") as data:
        #reads data file object as json
        game_data = json.load(data)
            
        # reads locations from game_data.txt and saves in a locations dict
        locations = {}
        for location in game_data["locations"]:
            loc_name = location["index"]
            locations[loc_name] = location
    
    return locations   

def load_entities(locations):
     player = Player("Hero", "your cell")
     locations["cell"]["entities"][player.name] = player
     rat = NPC("rat","rodent", 1, 3, 1, 1, 1, 6, 1, 1, "escape tunnel")
     locations["escape tunnel"]["entities"][rat.group] = rat
     guard = NPC("guard","human", 3, 6, 3, 6, 3, 6, 3, 6, "guard room")
     locations["guard room"]["entities"][guard.group] = guard

def main():
     locations = load_locations()
     load_entities(locations)
     pprint(locations)

if __name__ == "__main__":
	main()
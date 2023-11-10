#!/usr/bin/env python3

# import needed classes and function
from entity import Entity
import json
from pprint import pprint
from textwrap import fill
import os

# define location class
class Location():
    def __init__(self, index: str, name: str, description: str, details: str, connections: dict[str, str], inventory: list[str]):
        self.index = index
        self.name = name
        self.description: str = description
        self.details: str = details
        self.connections: dict[str, str] = connections
        self.inventory: list[str] = inventory
        self.entities: list[str] = []

def location_status(locations, current_loc):
    os.system("clear")
    '''function to display location'''
    # sets the current location object
    current_loc_entry = locations[current_loc]
 
    # displayed when player enters a location or looks
    print(f"You are in {current_loc_entry['name']}")
    print("---------------------------")
    print(fill(current_loc_entry['description'], width=50))
    print("---------------------------")
    print("Looking around you see:")
    for key, value in current_loc_entry['connections'].items():
        print(f"\tYou see {locations[value]['name']} to the {key}")
    print("---------------------------")
    # prints out the rooms inventory or nothing is inventory is empty
    if current_loc_entry["inventory"] != []:
        print("You see the following items:")
        for item in current_loc_entry["inventory"]:
            print(item)
        print("---------------------------")
    if current_loc_entry["entities"] != {}:
        print("You see the following creatures/people:")
        for item in current_loc_entry["entities"]:
            print(item)
        print("---------------------------")

def location_search(locations, current_loc):
    current_loc_entry = locations[current_loc]
    os.system("clear")
    print("Your take a closer look at your surrondings...")
    print(fill(current_loc_entry['details'], width=50))
    print("\n")

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


# define main class for testing
def main():
    locations = load_locations()
    location_status(locations, "cell")
    print(locations['cell']['details'])

if __name__ == "__main__":
    main()
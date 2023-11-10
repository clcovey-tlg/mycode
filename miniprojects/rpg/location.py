#!/usr/bin/env python3

# import needed classes and function
from entity import Entity
import json
from pprint import pprint
from textwrap import fill
import os

# define location class
class Location():
    """
    A class used to represent a game location.

    ...

    Attributes
    ----------
    index : str
        an index to be used as a reference for the location
    name : str
        a formatted string for displaying the location name
    description : str
        a brief description of the location
    details : str
        additional details about the location
    connections : dict
        a dictionary representing connections to other locations
    inventory : list
        a list of items present in the location
    entities : list
        a list of entities (creatures/people) present in the location

    Methods
    -------
    None
    """
    def __init__(self, index: str, name: str, description: str, details: str, connections: dict[str, str], inventory: list[str]):
        self.index = index
        self.name = name
        self.description: str = description
        self.details: str = details
        self.connections: dict[str, str] = connections
        self.inventory: list[str] = inventory
        self.entities: list[str] = []

def location_status(locations, current_loc):
    """
    Display the status of the current location, including its description, connections, inventory, and entities.

    Parameters:
    - locations (dict): Dictionary containing information about game locations.
    - current_loc (str): The current location.

    Returns:
    - None
    """
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
    """
    Display additional details about the current location.

    Parameters:
    - locations (dict): Dictionary containing information about game locations.
    - current_loc (str): The current location.

    Returns:
    - None
    """
    current_loc_entry = locations[current_loc]
    os.system("clear")
    print("Your take a closer look at your surrondings...")
    print(fill(current_loc_entry['details'], width=50))
    print("\n")

def load_locations():
    """
    Load location data from the game_data.txt file and create Location objects.

    Returns:
    - dict: Dictionary containing generated Location objects.
    """
    with open("game_data.txt", "r") as data:
        #reads data file object as json
        game_data = json.load(data)
            
        # reads locations from game_data.txt and saves in a locations dict
        locations = {}
        for location in game_data["locations"]:
            loc_name = location["index"]
            locations[loc_name] = location
    
    return locations

def main():
    """
    Main function for testing purposes.
    """
    locations = load_locations()
    location_status(locations, "cell")
    print(locations['cell']['details'])

if __name__ == "__main__":
    main()
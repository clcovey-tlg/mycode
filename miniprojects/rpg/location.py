#!/usr/bin/env python3

# import needed classes and function
from entity import Entity
import json

# define location class
class Location():
    def __init__(self, index: str, name: str, description: str, connections: dict[str, str], inventory: list[str], entities: Entity):
        self.index = index
        self.name = name
        self.description: str = description
        self.connections: dict[str, str] = connections
        self.inventory: list[str] = inventory
        self.entities: Entity = entities

def location_status(locations, current_loc):
    # function to display location
    # displayed when player enters a location or looks
        print(f"You are in {locations[current_loc]['name']}")
        print("---------------------------")
        print(locations[current_loc]['description'])
        print("---------------------------")
        print("Looking around you see:")
        for key, value in locations[current_loc]['connections'].items():
             print(f"Direction: {key} - {value}")
        print("---------------------------")

# define main class for testing
def main():
    locations = {}
    with open("game_data.txt", "r") as data:
        #reads data file object as json
        game_data = json.load(data)
        
        # reads locations and saves in a locations dict
        for location in game_data["locations"]:
            loc_name = location["index"]
            locations[loc_name] = location
        #print(locations)
    current_location = "hall"
    location_status(locations, current_location)

if __name__ == "__main__":
    main()
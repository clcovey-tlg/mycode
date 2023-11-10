#!/usr/bin/env python3

import requests
from pprint import pprint

def display_json_monsters():
    """
    Display JSON representation of all monsters.

    Returns:
    None
    """
    monsters_url = "http://127.0.0.1:2224/monsters/json"
    monsters = requests.get(monsters_url).json()
    
    pprint(monsters)

def display_json_monster_detail(name):
    """
    Display JSON representation of details for a specific monster.

    Args:
    name (str): The name of the monster.

    Returns:
    None
    """
    detail_url = f"http://127.0.0.1:2224/monster/{name}/json"
    monster = requests.get(detail_url).json()
    
    # extracts keys from monster to move NAME so that it will be printed first
    keys = list(monster.keys())
    keys.insert(0, keys.pop(keys.index("NAME")))
    for key in keys:
        print(f"{key.capitalize()}: {monster[key]}")

def main():
    #display_json_monsters()
    display_json_monster_detail("Rat")

if __name__ == "__main__":
	main()
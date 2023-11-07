#!/usr/bin/env python3

# needed imports
from requests import get
import json
from entity import NPC
from pprint import pprint

# function to retrieve npc data from api
def get_npc_data(npc, location):
    # build api url
    api_url = "https://www.dnd5eapi.co/api/monsters/" + npc

    # retrieve and parse npc data
    response = get(api_url)
    data = response.text
    parsed_data = json.loads(data)
    
    # instanciate npc and set attributes from parsed api data
    npc = NPC(location)
    setattr(npc, "index", parsed_data["index"])
    setattr(npc, "name", parsed_data["name"])
    setattr(npc, "group", parsed_data["type"])
    setattr(npc, "max_hp", parsed_data["hit_points"])
    setattr(npc, "hp", parsed_data["hit_points"])
    setattr(npc, "strength", parsed_data["strength"])
    setattr(npc, "dexerity", parsed_data["dexterity"])
    setattr(npc, "ac", parsed_data["armor_class"][0]["value"])
    setattr(npc, "attack", parsed_data["actions"][0]["name"])

    return npc

# main method for testing of function during testing
def main():
    guard = get_npc_data("guard", "guard room")
    print(guard.__dict__)
    rat = get_npc_data("rat", "escape tunnel")
    print(rat.__dict__)

if __name__ == "__main__":
	main()
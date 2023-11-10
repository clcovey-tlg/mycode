#!/usr/bin/env python3
# import necessary modules
import os
from actions import roll_dice
from pprint import pprint
from format_txt import make_red, make_green, make_blue, underline

# method for an entity to attack
def attack(attacker, target):
    roll = roll_dice()
    dam_mod = int((attacker.strength - 10) / 2)
    if dam_mod < 0:
        dam_mod = 0
    atk_mod = int((attacker.dexterity - 10) / 2)
    atk = roll + atk_mod
    print(f"{attacker.name} rolled a {atk}. {target.name} has an armor class of {target.ac}")
    if atk > target.ac:
        damage = roll_dice(attacker.damage) + dam_mod
        target.hp -= damage
        if target.__class__.__name__ == "Player":
            print(f"{make_green(attacker.name)} has hit you for {make_red(damage)} damage")
        else:    
            print(f"{make_green(attacker.name)} hit the {make_blue(target.name)} for {make_red(damage)} damage")
    else:
        print(f"{make_green(attacker.name)} has {make_red('missed')}")

def battle(player, monster, locations):
    player_dam_mod = int((player.strength - 10) / 2)
    if player_dam_mod < 0:
        player_dam_mod = 0
    monster_dam_mod = int((monster.strength - 10) / 2)
    if monster_dam_mod < 0:
        monster_dam_mod = 0
    input(f"\nThe battle with the {monster.name} begins! Press enter")
    while True:
        os.system("clear")
        print(f"{player.name} - Health: {player.hp}, Damage: {player.damage} + {player_dam_mod}, Armor Class: {player.ac}")
        print(f"{monster.name} - Health: {monster.hp}, Damage: {monster.damage} + {monster_dam_mod}, Armor Class: {monster.ac}\n")
        attack(player, monster)
        print()
        if monster.hp < 1:
            print(f"You killed the {monster.name}!")
            input("Press enter to continue")
            del locations[monster.location]["entities"][monster.index]
            monster.location = ""
            return False
        attack(monster, player)
        if player.hp < 1:
            print(f"You were killed by a {monster.name}")
            print(f"{underline(make_red('You were killed!! Better luck next time!'))}")
            return True
        input(f"\nPress enter to continue your battle with the {monster.name}")
        
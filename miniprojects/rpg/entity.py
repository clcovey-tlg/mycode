#!/usr/bin/env python3

# import necessary modules
from actions import roll_dice

# define parent class for an entity
class Entity():
    """
    A class used to represent an Entity

    ...

    Attributes
    ----------
    index : str
        an index to be used as a reference for the entity
    name : str
        a formatted string for displaying the entity name
    group : str
        the group to which the entity belongs (i.e. beast, humanoid)
    max_health : int
        the maximum health of the entity
    health : int
        the current health of the entity
    strength : int
        a representation of the physical strength of the entity
    dexterity : int
        a representation of agility, reflexes, and balance of the entity
    ac : int
        a representation of how easy/difficult an entity is to hit

    Methods
    -------
    __str__()
        Prints a custom to string for entity
    move(new_location)
        Moves entity to a new location
    """
    def __init__(self):
        self.index: str
        self.name: str
        self.group: str
        self.max_hp: int
        self.hp: int
        self.strength: int
        self.damage: str
        self.dexterity: int
        self.ac: int
        self.inventory: list[str] = []
        self.location: str

    # method to define __str__ for entities
    def __str__(self):
        if self.__class__.__name__ == "Player":
            print(f"Name: {self.name}, Type: {self.__class__.__name__}, Race: {self.race}")
        else:
            print(f"NPC: {self.name}, Type: {self.group}")
        print("\x1B[4mStats\x1B[0m")
        print(f"Max Health: {self.max_hp}, Current Health: {self.hp}")
        print(f"Strength: {self.strength}, Damage: {self.damage}")
        print(f"Dexterity: {self.dexterity}, Armor Class: {self.ac}")
        if self.inventory == []:
            print(f"Inventory: Empty")
        else:
            print(f"Inventory: ")
            for item in self.inventory:
                print(item)
        print(f"Current Location: {self.location}")

    # method for an entity to move
    def move(self, locations, new_location):
        if self.__class__.__name__ == "Player":
            self.location = new_location
        else:
            locations[self.location]["entities"] #remove from current location
            self.location = new_location
            

    # method for an entity to attack
    def attack(self, target):
        roll = roll_dice()
        mod = int((self.dexterity - 10) / 2)
        atk = roll + mod
        if atk > target.ac:
            damage = roll_dice(self.damage)
            target.hp -= damage
            print(f"You hit the {target.name} for {damage} damage")
            if target.hp <= 0:
                print(f"You have killed the {target.name}")
        else:
            print("You miss")

# define child class for a monster from entity
class NPC(Entity):
    def __init__(self, location: str, damage: str):
        # keep the attributes from Entity
        super().__init__()
        self.index: str
        self.name: str
        self.group: str
        self.max_hp: int
        self.hp: int
        self.strength: int
        self.damage: str = damage
        self.dexterity: int
        self.ac: int
        self.inventory: list[str] = []
        self.location: str = location

# define child class of player from entity
class Player(Entity):
    def __init__(self, name: str, location: str):
        # keep the attributes from Entity
        super().__init__()
        self.race: str = "Human"
        self.name: str = name
        self.max_hp = 20
        self.hp = self.max_hp
        self.strength = 14
        self.damage: str = "1d6"
        self.dexterity = 14
        self.ac: int = 10
        self.inventory: list[str] = []
        self.location: str = location
        

def main():
    player = Player("Ezok", "cell")
    print(getattr(player, "name"))
    rat = NPC("none", "1d1")
    setattr(rat, "hp", 1)
    setattr(rat, "ac", 11)
    setattr(rat, "name", "Rat")
    player.attack(rat)

if __name__ == "__main__":
	main()
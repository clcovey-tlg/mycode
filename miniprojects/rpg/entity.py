#!/usr/bin/env python3

# import necessary modules
import json


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
    says(sound=None)
        Prints the animals name and what sound it makes
    """
    def __init__(self):
        self.index: str
        self.name: str
        self.group: str
        self.max_health: int
        self.health: int
        self.strength: int
        self.dexerity: int
        self.ac: int
        self.inventory: list[str] = []
        self.location: str

    # method to define __str__ for entities
    def __str__(self):
        if self.__class__.__name__ == "Player":
            line1 = (f"Name: {self.name}, Type: {self.__class__.__name__}, Race: {self.race}\n")
        else:
            line1 = (f"Group: {self.group}, Race: {self.race}\n")
        line2 = ("\x1B[4mStats\x1B[0m\n")
        line3 = (f"Max Health: {self.max_health}, Current Health: {self.health}\n")
        line4 = (f"Strength: {self.strength}, Dexterity: {self.dexerity}, Intelligence: {self.intelligence}\n")
        if self.inventory == []:
            line5 = (f"Inventory: Empty\n")
        else:
            line5 = (f"Inventory: ")
            for item in self.inventory:
                line5 += (f"{item} ")
            line5 += "\n"
        line6 = (f"Current Location: {self.location}\n")

        return line1 + line2 + line3 + line4 + line5 + line6

    # method for an entity to move
    def move(self, new_location):
        self.location = new_location

    # method for an entity to attack
    def attack(self, damage, target):
        target.health -= damage - (target.dexerity / 3)

# define child class for a monster from entity
class NPC(Entity):
    def __init__(self, location):
        # keep the attributes from Entity
        super().__init__()
        self.index: str
        self.name: str
        self.group: str
        self.max_health: int
        self.health: int
        self.strength: int
        self.dexerity: int
        self.inventory: list[str] = []
        self.location: str

# define child class of player from entity
class Player(Entity):
    def __init__(self, name: str, location: str):
        # keep the attributes from Entity
        super().__init__()
        self.race: str = "Human"
        self.name: str = name
        self.max_health = 20
        self.strength = 10
        self.dexerity = 10
        self.health = self.max_health
        self.location: str = location

def main():
    player = Player("Ezok", "cell")
    player.inventory.append("sword")
    print(player.__str__())

if __name__ == "__main__":
	main()
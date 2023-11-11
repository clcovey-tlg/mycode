#!/usr/bin/env python3

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
    display()
        Prints a custom to string for entity
    move(new_location)
        Moves entity to a new location
    get_item(locations, items, item_name)
        Adds an item to the entity's inventory if it exists in the current location,
        and updates entity attributes based on the item's category.
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

    def display(self):
        """
        Prints the attributes and stats of an entity in a formatted manner.
        """
        if self.__class__.__name__ == "Player":
            print(f"Name: {self.name}, Type: {self.__class__.__name__}, Race: {self.race}")
        else:
            print(f"NPC: {self.name}, Type: {self.group}")
        print("\x1B[4mStats\x1B[0m")
        print(f"Max Health: {self.max_hp}, Current Health: {self.hp}")
        print(f"Strength: {self.strength}, Damage: {self.damage} + {max(0, (self.strength - 10) // 2)}")
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
        """
        Moves the entity to a new location.

        Parameters:
        - locations: The dictionary containing information about locations in the game.
        - new_location: The name of the new location to move the entity to.

        If the entity is a player, the location is updated directly.
        If the entity is an NPC, it is removed from the current location's entities list and added to the new location.
        """
        if self.__class__.__name__ == "Player":
            self.location = new_location
        else:
            locations[self.location]["entities"] #remove from current location
            self.location = new_location

    def get_item(self, locations, items, item_name):
        """
        Adds an item to the entity's inventory if it exists in the current location,
        and updates entity attributes based on the item's category.

        Parameters:
        - locations: The dictionary containing information about locations in the game.
        - items: The dictionary containing information about available items in the game.
        - item_name: The name of the item to be added to the entity's inventory.
        """
        item_list = locations[self.location]["inventory"]
        if item_name in item_list:
            self.inventory.append(item_name)
            locations[self.location]["inventory"].remove(item_name)
            item = items[item_name]
            if item["category"] == "weapon":
                self.damage = item["damage"]
            if item["category"] == "armor":
                self.ac += int(item["ac"])


# define child class for a monster from entity
class NPC(Entity):
    """
    A class used to represent a Non-Player Character (NPC) entity, inheriting from Entity.

    ...

    Attributes
    ----------
    Inherits attributes from the parent class Entity and adds:
    damage : str
        the damage capability of the NPC

    Methods
    -------
    None
    """
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
    """
    A class used to represent a Player entity, inheriting from Entity.

    ...

    Attributes
    ----------
    Inherits attributes from the parent class Entity and adds:
    race : str
        the race of the player

    Methods
    -------
    None
    """
    def __init__(self, name: str, location: str):
        # keep the attributes from Entity
        super().__init__()
        self.race: str = "Human"
        self.name: str = name
        self.max_hp: int = 20
        self.hp: int = self.max_hp
        self.strength: int = 0
        self.damage: str = "1d4"
        self.dexterity: int = 0
        self.ac: int
        self.inventory: list[str] = []
        self.location: str = location
        

def main():
    player = Player("Ezok", "cell")
    print(getattr(player, "name"))
    rat = NPC("none", "1d1")
    setattr(rat, "hp", 1)
    setattr(rat, "ac", 11)
    setattr(rat, "name", "Rat")

if __name__ == "__main__":
	main()
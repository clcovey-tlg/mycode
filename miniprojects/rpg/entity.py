#!/usr/bin/env python3

# import necessary modules
from actions import roll_dice


# define parent class for an entity
class Entity():
    def __init__(self):
        self.race: str
        self.max_health: int
        self.health: int
        self.strength: int
        self.dexerity: int
        self.intelligence: int
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
    def __init__(self, group: str, race: str, hp_die_number: int, hp_die_type: int, str_die_number: int, str_die_type: int, dex_die_number: int, dex_die_type: int, int_die_number: int, int_die_type: int, location: str):
        # keep the attributes from Entity
        super().__init__()
        self.group: str = group
        self.race: str = race
        self.max_health = sum(roll_dice(hp_die_number, hp_die_type))
        self.health = self.max_health
        self.strength: int = sum(roll_dice(str_die_number, str_die_type))
        self.dexerity: int = sum(roll_dice(dex_die_number, dex_die_type))
        self.intelligence: int = sum(roll_dice(int_die_number, int_die_type))
        self.location: str = location

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
        self.intelligence = 10
        self.health = self.max_health
        self.location: str = location

def main():
     player = Player("Ezok", "default")
     player.inventory.append("sword")
     print(player.__str__())
     rat = NPC("monster","rodent", 3, 1, 1, 1, 6, 1, 1, 1, "default")
     print(rat.__str__())
     guard = NPC("guard","human", 3, 1, 1, 1, 6, 1, 1, 1, "default")
     print(guard.__str__())

if __name__ == "__main__":
	main()
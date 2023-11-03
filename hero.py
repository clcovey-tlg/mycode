#!/usr/bin/env python3

# design a Player class
class Player():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.max_health = 10
        self.stamina = 10
        self.max_stamina = 10
        self.strength = self.stamina / 2
        self.inventory = []
        self.location = "Hall"

    # method to move
    def move(self, new_location):
        self.location = new_location
        print("You move to", new_location)

    # method to attack
    def attack(self, target):
        self.health
        target.health -= self.strength
        print(f"{target.name} now has {target.health} health")

# create a Player objects
zack = Player("Zack")
gen = Player("Gen")

# print out a attribute of a class object
print(zack.health)
print(gen.location)

# call a method
gen.move("Living Room")
print(gen.location)

gen.attack(zack)

# inheritance
class Wizard(Player):
    def __init__(self, name):
        # keep the attributes from Player
        super().__init__(name)
        self.magic = 10

    def fireball(self, target):
        target.health -= self.magic * 2
        print(f"{target.name} now has {target.health} health")

bert = Wizard("Alberto")
chad = Player("Chad")

bert.fireball(chad)
bert.attack(chad)

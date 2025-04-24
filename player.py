from combat import player_attack
import time
from world import print_world, print_room_description
from utils import move_player


class Player:
    health, speed, attack, inventory = 0, 0, 0, []

    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type

        if class_type == "Warrior":
            self.health = 150
            self.speed = 70
            self.attack = 105
            self.inventory = {
                "Health Potion": "Heals damage taken in battle.",
                "Berserker Charm": "Boosts attack power."}
        elif class_type == "Mage":
            self.health = 125
            self.speed = 100
            self.attack = 80
            self.inventory = {
                "Mana Potion": "Increases magic attack power.",
                "Fire Scroll": "Casts a powerful fire spell."}
        else:
            self.health = 100
            self.speed = 150
            self.attack = 100
            self.inventory = {
                "Smoke Bomb": "Escape from battle or avoid an ambush.",
                "Throwing Knives": "Quick ranged damage"}

    def is_alive(self):
        return self.health > 0

    def print_stats(self):
        print(f"Your stats are: \n"
              f"Health: {self.health}\n"
              f"Speed: {self.speed}\n"
              f"Attack: {self.attack}\n")

    def print_inventory(self):
        print("Your inventory consists of:")
        for key, value in self.inventory.items():
            print(f"- {key}: {value}")

    def use_item(self, item, player_x = None, player_y = None, enemy = None):
        match item:
            case "Health Potion":
                if self.health < 130:
                    self.health += 20
                    print("You have gained 20hp!")
                    del self.inventory[item]
                else:
                    print("Your hp is already full!")
            case "Berserker Charm":
                self.attack += 20
                print("Your attack power has increased by 20!")
                del self.inventory[item]
            case "Mana Potion":
                self.attack += 30
                print("Your attack power has increased by 30!")
                del self.inventory[item]
            case "Fire Scroll":
                self.attack = 110
                print("You have used the Fire Scroll!")
                if enemy:
                    player_attack(self, enemy)
                self.attack = 80
                del self.inventory[item]
            case "Smoke Bomb":
                print("The smoke bomb has been used! You can flee from battle!")
                print("Choose where you wish to run: ")
                print_world(player_x, player_y)
                time.sleep(3)
                player_x, player_y = move_player(player_x, player_y)
                print_room_description(player_x, player_y)
                time.sleep(3)
                del self.inventory[item]
            case "Throwing Knives":
                self.attack = 130
                print("You have used Throwing Knives!")
                if enemy:
                    player_attack(self, enemy)
                self.attack = 100
                del self.inventory[item]

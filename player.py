from combat import player_attack


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

    def use_item(self, item, enemy = None):
        match item:
            case "Health Potion":
                self.health += 20
                print("You have gained 20hp!")
            case "Berserker Charm":
                self.attack += 20
                print("Your attack power has increased by 20!")
            case "Mana Potion":
                self.attack += 30
                print("Your attack power has increased by 30!")
            case "Fire Scroll":
                self.attack = 110
                print("You have used the Fire Scroll!")
                if enemy:
                    player_attack(self, enemy)
                self.attack = 80
            case "Smoke Bomb":
                pass
            case "Throwing Knives":
                self.attack = 130
                print("You have used Throwing Knives!")
                if enemy:
                    player_attack(self, enemy)
                self.attack = 100
        del self.inventory[item]

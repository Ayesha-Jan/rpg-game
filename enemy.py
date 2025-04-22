class Enemy():
    health, speed, attack = 0, 0, 0

    def __init__(self, name):
        self.name = name
        if self.name == "Goblin":
            self.health = 50
            self.speed = 100
            self. attack = 40
        elif self.name == "Orc":
            self.health = 80
            self.speed = 60
            self.attack = 60
        elif self.name == "Zombie":
            self.health = 70
            self.speed = 60
            self.attack = 35
        else:
            self.health = 120
            self.speed = 100
            self.attack = 100

    def is_alive(self):
        return self.health > 0

    def appears(self):
        print(f"{self.name} has appeared!\n")

    def print_stats(self):
        print(f"The {self.name}'s stats are: \n"
              f"Health: {self.health}\n"
              f"Speed: {self.speed}\n"
              f"Attack: {self.attack}\n")

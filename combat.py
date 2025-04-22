import random


def player_attack(player, enemy):
    damage = random.randint(player.attack - 20, player.attack)
    print(f"You have damaged the {enemy.name} by {damage}!")
    enemy.health -= damage
    enemy.health = max(0, enemy.health)
    print(f"{enemy.name} has {enemy.health}hp remaining!")


def enemy_attack(player, enemy):
    damage = random.randint(enemy.attack - 20, enemy.attack)
    print(f"You have been damaged by {damage}!")
    player.health -= damage
    player.health = max(0, player.health)
    print(f"You have {player.health}hp remaining!")
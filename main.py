import time
from player import Player
from enemy import Enemy
import random
from utils import choose_class_type, menu, choose_move, move_player
from world import print_world, print_room_description
from combat import player_attack, enemy_attack


def main():

    #PLAYER INFO
    print("🗡️ Welcome to *Realm of Shadows*! ")
    time.sleep(1)
    name = input("\nEnter your player name: ").capitalize()
    print(f"\nWelcome, {name} the Brave!")
    time.sleep(1)

    print("\nBefore you begin your quest, choose your path wisely...\n")
    time.sleep(1)
    class_type = choose_class_type()

    player = Player(name, class_type)
    print(f"\n{name} the {player.class_type}, your journey begins now!\n")
    time.sleep(2)

    player.print_stats()
    time.sleep(3)
    player.print_inventory()
    time.sleep(3)

    #SHOWCASING MAP
    player_x = 0
    player_y = 0
    print_world(player_x, player_y)
    time.sleep(3)
    print_room_description(player_x, player_y)
    time.sleep(3)

    while player.is_alive():

        if player_x == 2 and player_y == 2:
            enemy = Enemy("Boss")
        else:
            enemies = ("Goblin", "Orc", "Zombie")
            enemy = Enemy(random.choice(enemies))

        enemy.appears()
        time.sleep(2)
        enemy.print_stats()
        time.sleep(3)

        battle_over = False

        while player.is_alive() and enemy.is_alive():
            if enemy.is_alive():
                choice = menu()
                time.sleep(1)

            if choice == "1":
                if player.speed > enemy.speed:
                    player_attack(player, enemy)
                    time.sleep(2)
                    if enemy.is_alive():
                        enemy_attack(player, enemy)
                        time.sleep(2)
                        if not player.is_alive():
                            break
                else:
                    enemy_attack(player, enemy)
                    time.sleep(2)
                    if not player.is_alive():
                        break
                    player_attack(player, enemy)
                    time.sleep(2)

            elif choice == "2":
                player.print_inventory()
                item = input("Select an item: ").title()
                while item not in player.inventory:
                    print("Item not available.")
                    item = input("Select an item: ").title()
                player.use_item(item, enemy)

            else:
                if player.speed > enemy.speed:
                    print(f"{name} has decided to run!")
                    print("Choose where you wish to run: ")
                    print_world(player_x, player_y)
                    time.sleep(3)
                    player_x, player_y = move_player(player_x, player_y)
                    print_room_description(player_x, player_y)
                    time.sleep(3)
                    battle_over = True
                else:
                    print("You are slower than the enemy and cannot run!")
                    choice = menu()
                    battle_over = True

        if not player.is_alive():
            break

        if enemy.name == "Boss" and not enemy.is_alive():
            print("\n Congratulations! You have defeated the final boss and saved the realm!")
            print("The land is peaceful once again. You are a true hero.")
            print("Thank you for playing!\n")
            return

        if not battle_over:
            print_world(player_x, player_y)
            time.sleep(3)
            player_x, player_y = move_player(player_x, player_y)
            print_room_description(player_x, player_y)
            time.sleep(3)

    if not player.is_alive():
        print(f"\n{name}, you have fallen in battle!")
        choice = input("Would you like to start over? (Yes/No): ").capitalize()
        if choice == "Yes":
            print("\nRestarting rpg_game...\n")
            time.sleep(1)
            main()
        else:
            print("Thanks for playing! Farewell, brave warrior.")
            exit()


if __name__ == '__main__':
    main()


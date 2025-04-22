def choose_class_type():
    print("The following class types are available:\n"
          "1. Warrior\n"
          "2. Mage\n"
          "3. Rogue\n")

    class_type = input("Choose a class type: ").capitalize()
    while class_type not in ["Warrior", "Mage", "Rogue"]:
        print("Choose a correct class type!")
        class_type = input("Choose a class type: ").capitalize()
    print(f"You have chosen {class_type}!")
    return class_type


def choose_move():
    print("Select a direction:")
    direction = input("W (North)\n"
                      "A (West)\n"
                      "S (South)\n"
                      "D (East)\n").upper()
    while direction not in ["W", "A", "S", "D"]:
        print("Invalid direction!")
        direction = input("W (North)\n"
                          "A (West)\n"
                          "S (South)\n"
                          "D (East)\n").upper()
    return direction


def move_player(player_x, player_y):
    while True:
        direction = choose_move()
        match direction:
            case "W":
                if player_y > 0:
                    player_y -= 1
                    break
                else:
                    print("You can't go further north!")
            case "A":
                if player_x > 0:
                    player_x -= 1
                    break
                else:
                    print("You can't go further west!")
            case "S":
                if player_y < 2:
                    player_y += 1
                    break
                else:
                    print("You can't go further south!")
            case "D":
                if player_x < 2:
                    player_x += 1
                    break
                else:
                    print("You can't go further east!")

    return player_x, player_y


def menu():
    print(
        "What will you do?\n"
        "1. Attack\n"
        "2. Use Item\n"
        "3. Run")

    choice = input("Choose an option(1/2/3): ")
    while choice not in ["1", "2", "3"]:
        print("Choose a correct option!")
        choice = input("Choose an option(1/2/3): ")
    return choice


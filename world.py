def print_world(player_x, player_y):
    worlds = [["Forgotten Forest", "Crystal Cavern", "Tower Ruins"],
              ["River Crossing", "Sacred Grove", "Lost Library"],
              ["Murky Swamp", "Dragon's Hollow", "Boss Fight"]]

    emojis = [["🌲", "💎", "🏰"],
              ["🌊", "🌿", "📚"],
              ["🐸", "🐉", "👑"]]

    cell_width = 20
    border = "+" + ("-" * cell_width + "+") * 3

    for y, (world_row, emoji_row) in enumerate(zip(worlds, emojis)):
        print(border)

        # Emoji line with player marker
        emoji_line = ""
        for x, emoji in enumerate(emoji_row):
            if x == player_x and y == player_y:
                emoji = "👤"  # Player is here
            emoji_line += f"| {emoji.center(cell_width - 2)} "
        print(emoji_line + "|")

        # Room name line
        name_line = ""
        for name in world_row:
            name_line += f"| {name.center(cell_width - 2)} "
        print(name_line + "|")

    print(border)


# Example usage:

descriptions = {
    (0, 0): "You stand beneath the ancient trees of the Forgotten Forest. The air is thick with mystery.",
    (1, 0): "Crystals shimmer on the cavern walls. It's eerily quiet in the Crystal Cavern.",
    (2, 0): "The Tower Ruins loom above you, worn down by centuries of wind and rain.",
    (0, 1): "The River Crossing is slick with moss. You hear the rush of water all around.",
    (1, 1): "You enter the Sacred Grove. The trees whisper in a language long forgotten.",
    (2, 1): "Books float and shift on their own in the Lost Library. The past is alive here.",
    (0, 2): "The swamp bubbles ominously. Creatures slither in the murky waters.",
    (1, 2): "Dragon's Hollow is vast and echoing. You feel heat pulsing through the stone.",
    (2, 2): "You face the Boss. The final battle begins here!"
}


def print_room_description(player_x, player_y):
    room_description = descriptions[(player_x, player_y)]
    print("\n" + room_description + "\n")

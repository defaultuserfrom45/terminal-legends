import json
from terminal_legends.character import Character


SAVE_FILE = "savegame.json"


def save_game(player):
    data = {
        "name": player.name,
        "char_class": player.char_class,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "attack": player.attack,
        "level": player.level,
        "xp": player.xp,
        "xp_to_next_level": player.xp_to_next_level,
        "potions": player.potions,
        "gold": player.gold,
    }

    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("\nGame saved successfully!")


def load_game():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        player = Character(data["name"], data["char_class"])
        player.hp = data["hp"]
        player.max_hp = data["max_hp"]
        player.attack = data["attack"]
        player.level = data["level"]
        player.xp = data["xp"]
        player.xp_to_next_level = data["xp_to_next_level"]
        player.potions = data["potions"]
        player.gold = data["gold"]

        print("\nGame loaded successfully!")
        return player

    except FileNotFoundError:
        print("\nNo save file found.")
        return None

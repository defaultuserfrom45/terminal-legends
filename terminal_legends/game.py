from terminal_legends.character import Character
from terminal_legends.battle import start_battle

def start_game():
    print("⚔️ Welcome to Terminal Legends!")
    print("----------------------------")

    name = input("Enter your character name: ")

    print("\nChoose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")

    choice = input("> ")

    if choice == "1":
        char_class = "Warrior"
    elif choice == "2":
        char_class = "Mage"
    elif choice == "3":
        char_class = "Rogue"
    else:
        char_class = "Adventurer"

    player = Character(name, char_class)

    print(f"\nWelcome, {player.name} the {player.char_class}!")

    # Start first battle
    start_battle(player)

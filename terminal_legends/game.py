from terminal_legends.character import Character
from terminal_legends.battle import start_battle, start_boss_battle
from terminal_legends.shop import open_shop


def show_player_status(player):
    print("\n====================")
    print(f"Name: {player.name}")
    print(f"Class: {player.char_class}")
    print(f"Level: {player.level}")
    print(f"HP: {player.hp}/{player.max_hp}")
    print(f"Attack: {player.attack}")
    print(f"XP: {player.xp}/{player.xp_to_next_level}")
    print(f"Potions: {player.potions}")
    print(f"Gold: {player.gold}")
    print("====================")


def create_character():
    print("Welcome to Terminal Legends!")
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
    return player


def game_loop(player):
    while player.is_alive():
        print("\nMain Menu")
        print("1. Fight a monster")
        print("2. Show character status")
        print("3. Visit shop")

        if player.level >= 3:
            print("4. Fight the Boss")
            print("5. Quit game")
        else:
            print("4. Quit game")

        choice = input("> ")

        if choice == "1":
            survived = start_battle(player)
            if not survived:
                print("\nGame Over!")
                break

        elif choice == "2":
            show_player_status(player)

        elif choice == "3":
            open_shop(player)

        elif choice == "4" and player.level >= 3:
            boss_result = start_boss_battle(player)

            if boss_result == "boss_won":
                print("\nCongratulations! You completed the game!")
                break
            elif boss_result == "boss_lost":
                print("\nGame Over!")
                break

        elif (choice == "4" and player.level < 3) or (choice == "5" and player.level >= 3):
            print("\nThanks for playing Terminal Legends!")
            break

        else:
            print("\nInvalid choice. Please try again.")


def start_game():
    player = create_character()
    game_loop(player)

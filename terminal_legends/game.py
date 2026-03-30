from terminal_legends.character import Character
from terminal_legends.battle import start_battle, start_boss_battle
from terminal_legends.shop import open_shop
from terminal_legends.save_system import save_game, load_game
from terminal_legends.events import trigger_random_event


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


def show_intro():
    print("\n====================================")
    print("         TERMINAL LEGENDS")
    print("====================================")
    print("The ancient land of Eldoria is in danger.")
    print("For years, monsters have roamed the roads,")
    print("villages have fallen silent, and fear has")
    print("spread across the kingdom.")
    print("\nOnly one hero can rise against the darkness.")
    print("Train, survive, grow stronger, and prepare")
    print("for the final battle against the Dragon.")
    print("Your legend begins now.")
    print("====================================")


def create_character():
    print("\nCreate Your Character")
    print("---------------------")

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
    print("Your journey into Eldoria begins...")
    return player


def main_menu():
    while True:
        print("\n====================================")
        print("         TERMINAL LEGENDS")
        print("====================================")
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")

        choice = input("> ")

        if choice == "1":
            show_intro()
            return create_character()
        elif choice == "2":
            player = load_game()
            if player is not None:
                print(f"\nWelcome back, {player.name}.")
                return player
        elif choice == "3":
            print("\nGoodbye!")
            return None
        else:
            print("\nInvalid choice. Please try again.")


def game_loop(player):
    while player.is_alive():
        print("\nMain Menu")
        print("1. Fight a monster")
        print("2. Show character status")
        print("3. Visit shop")
        print("4. Save game")

        if player.level >= 3:
            print("5. Fight the Boss")
            print("6. Quit game")
        else:
            print("5. Quit game")

        choice = input("> ")

        if choice == "1":
            trigger_random_event(player)

            if not player.is_alive():
                print("\nYou did not survive the event...")
                print("Game Over!")
                break

            survived = start_battle(player)
            if not survived:
                print("\nGame Over!")
                break

        elif choice == "2":
            show_player_status(player)

        elif choice == "3":
            open_shop(player)

        elif choice == "4":
            save_game(player)

        elif choice == "5" and player.level >= 3:
            boss_result = start_boss_battle(player)

            if boss_result == "boss_won":
                print("\nCongratulations! You completed the game!")
                break
            elif boss_result == "boss_lost":
                print("\nGame Over!")
                break

        elif (choice == "5" and player.level < 3) or (choice == "6" and player.level >= 3):
            print("\nThanks for playing Terminal Legends!")
            break

        else:
            print("\nInvalid choice. Please try again.")


def start_game():
    player = main_menu()
    if player is not None:
        game_loop(player)

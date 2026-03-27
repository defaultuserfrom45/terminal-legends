def start_game():
    print("Welcome to Terminal Legends!")
    print("----------------------------")

    name = input("Enter your character name: ")

    print("\nChoose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")

    choice = input("> ")

    if choice == "1":
        player_class = "Warrior"
    elif choice == "2":
        player_class = "Mage"
    elif choice == "3":
        player_class = "Rogue"
    else:
        player_class = "Adventurer"

    print(f"\nWelcome, {name} the {player_class}!")
    print("Your journey begins now...\n")

    print("You walk into a dark forest...")
    print("A wild Goblin appears!")

    print("\n(To be continued...)")

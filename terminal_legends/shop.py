def open_shop(player):
    while True:
        print("\n=== Shop ===")
        print(f"Your gold: {player.gold}")
        print("1. Buy potion (10 gold)")
        print("2. Upgrade attack (+1) (20 gold)")
        print("3. Upgrade max HP (+5) (20 gold)")
        print("4. Leave shop")

        choice = input("> ")

        if choice == "1":
            if player.gold >= 10:
                player.gold -= 10
                player.potions += 1
                print("\nYou bought 1 potion.")
            else:
                print("\nNot enough gold.")

        elif choice == "2":
            if player.gold >= 20:
                player.gold -= 20
                player.attack += 1
                print("\nYour attack increased by 1.")
            else:
                print("\nNot enough gold.")

        elif choice == "3":
            if player.gold >= 20:
                player.gold -= 20
                player.max_hp += 5
                player.hp += 5
                if player.hp > player.max_hp:
                    player.hp = player.max_hp
                print("\nYour max HP increased by 5.")
            else:
                print("\nNot enough gold.")

        elif choice == "4":
            print("\nYou leave the shop.")
            break

        else:
            print("\nInvalid choice. Try again.")

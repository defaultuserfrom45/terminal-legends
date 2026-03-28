import random
from terminal_legends.monster import Monster


def create_random_monster(player_level):
    monsters = [
        Monster("Goblin", 15 + player_level * 2, 4 + player_level, 10),
        Monster("Wolf", 12 + player_level * 2, 5 + player_level, 12),
        Monster("Skeleton", 18 + player_level * 2, 3 + player_level, 14),
        Monster("Orc", 22 + player_level * 3, 6 + player_level, 18),
    ]
    return random.choice(monsters)


def start_battle(player):
    monster = create_random_monster(player.level)

    print(f"\nA wild {monster.name} appears!")

    while player.is_alive() and monster.is_alive():
        print("\n--------------------")
        print(f"{player.name} - Level {player.level}")
        print(f"HP: {player.hp}/{player.max_hp}")
        print(f"Attack: {player.attack}")
        print(f"XP: {player.xp}/{player.xp_to_next_level}")
        print(f"Potions: {player.potions}")
        print(f"\n{monster.name} HP: {monster.hp}")
        print("--------------------")

        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Use potion")
        print("3. Run away")

        choice = input("> ")

        if choice == "1":
            damage = player.deal_damage()
            monster.take_damage(damage)
            print(f"\nYou attack the {monster.name} and deal {damage} damage!")

        elif choice == "2":
            used_potion = player.heal()
            if not used_potion:
                continue

        elif choice == "3":
            print("\nYou ran away from the battle!")
            return True

        else:
            print("\nInvalid choice. Try again.")
            continue

        if monster.is_alive():
            damage = monster.deal_damage()
            player.take_damage(damage)
            print(f"The {monster.name} hits you for {damage} damage!")

    if player.is_alive():
        print(f"\nYou defeated the {monster.name}!")
        player.gain_xp(monster.xp_reward)
        return True
    else:
        print(f"\nYou were defeated by the {monster.name}...")
        return False

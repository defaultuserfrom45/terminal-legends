import random
import time
from terminal_legends.monster import Monster
from terminal_legends.boss import create_boss


def create_random_monster(player_level):
    monsters = [
        Monster("Goblin", 15 + player_level * 2, 4 + player_level, 10, 8),
        Monster("Wolf", 12 + player_level * 2, 5 + player_level, 12, 10),
        Monster("Skeleton", 18 + player_level * 2, 3 + player_level, 14, 12),
        Monster("Orc", 22 + player_level * 3, 6 + player_level, 18, 15),
    ]
    return random.choice(monsters)


def battle_loop(player, monster, allow_run=True):
    print(f"\nA wild {monster.name} appears!")
    time.sleep(1)

    while player.is_alive() and monster.is_alive():
        print("\n==============================")
        print(f"{player.name} (Level {player.level})")
        print(f"HP: {player.hp}/{player.max_hp}")
        print(f"Attack: {player.attack}")
        print(f"XP: {player.xp}/{player.xp_to_next_level}")
        print(f"Potions: {player.potions}")
        print(f"Gold: {player.gold}")
        print("------------------------------")
        print(f"{monster.name} HP: {monster.hp}")
        print("==============================")

        print("\nWhat do you want to do?")
        print("1. Attack")
        print("2. Use potion")
        if allow_run:
            print("3. Run away")

        choice = input("> ")

        if choice == "1":
            damage = player.deal_damage()
            monster.take_damage(damage)
            print(f"\nYou strike the {monster.name} for {damage} damage.")
            time.sleep(1)

        elif choice == "2":
            used_potion = player.heal()
            if not used_potion:
                continue
            time.sleep(1)

        elif choice == "3" and allow_run:
            print("\nYou ran away from the battle!")
            return "ran"

        else:
            print("\nInvalid choice. Try again.")
            continue

        if monster.is_alive():
            damage = monster.deal_damage()
            player.take_damage(damage)
            print(f"The {monster.name} attacks you for {damage} damage.")
            time.sleep(1)

    if player.is_alive():
        print(f"\nYou defeated the {monster.name}!")
        player.gain_xp(monster.xp_reward)
        player.gain_gold(monster.gold_reward)
        return "won"
    else:
        print(f"\nYou were defeated by the {monster.name}...")
        return "lost"


def start_battle(player):
    monster = create_random_monster(player.level)
    result = battle_loop(player, monster, allow_run=True)
    return result != "lost"


def start_boss_battle(player):
    boss = create_boss(player.level)
    print("\n=== BOSS BATTLE ===")
    print("A terrifying Dragon stands before you!")
    print("There is no escape from this fight.")

    result = battle_loop(player, boss, allow_run=False)

    if result == "won":
        print("\nYOU DEFEATED THE DRAGON!")
        print("================================")
        print(f"Champion: {player.name}")
        print(f"Final Level: {player.level}")
        print(f"Final Gold: {player.gold}")
        print("================================")
        print("You are the true hero of Terminal Legends!")
        return "boss_won"

    if result == "lost":
        print("\nThe Dragon has defeated you...")
        return "boss_lost"

    return result

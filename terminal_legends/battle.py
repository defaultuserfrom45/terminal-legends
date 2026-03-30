import random
import time
from terminal_legends.monster import Monster
from terminal_legends.boss import create_boss, Boss


def create_random_monster(player_level):
    monsters = [
        Monster("Goblin", 14 + player_level * 2, 3 + player_level, 10, 8),
        Monster("Wolf", 13 + player_level * 2, 4 + player_level, 12, 10),
        Monster("Skeleton", 17 + player_level * 2, 3 + player_level, 14, 12),
        Monster("Orc", 20 + player_level * 3, 5 + player_level, 18, 15),
    ]
    return random.choice(monsters)


def get_special_name(player):
    if player.char_class == "Warrior":
        return "Heavy Strike"
    elif player.char_class == "Mage":
        return "Fireball"
    elif player.char_class == "Rogue":
        return "Double Attack"
    return "Special Ability"


def monster_attack(player, monster):
    if isinstance(monster, Boss) and random.random() < 0.25:
        damage = monster.use_special_attack()
        player.take_damage(damage)
        print(f"\nThe {monster.name} uses Fire Breath and deals {damage} damage!")
        time.sleep(1)
    else:
        damage = monster.deal_damage()
        player.take_damage(damage)
        print(f"The {monster.name} attacks you for {damage} damage.")
        time.sleep(1)


def battle_loop(player, monster, allow_run=True):
    print(f"\nA wild {monster.name} appears!")
    time.sleep(1)

    while player.is_alive() and monster.is_alive():
        print("\n==============================")
        print(f"{player.name} (Level {player.level})")
        print(f"Class: {player.char_class}")
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
        print(f"2. Use {get_special_name(player)}")
        print("3. Use potion")
        if allow_run:
            print("4. Run away")

        choice = input("> ")

        if choice == "1":
            damage = player.deal_damage()
            monster.take_damage(damage)
            print(f"\nYou strike the {monster.name} for {damage} damage.")
            time.sleep(1)

        elif choice == "2":
            damage = player.use_special_ability()
            monster.take_damage(damage)
            print(f"You use {get_special_name(player)} against the {monster.name}.")
            time.sleep(1)

        elif choice == "3":
            used_potion = player.heal()
            if not used_potion:
                continue
            time.sleep(1)

        elif choice == "4" and allow_run:
            print("\nYou ran away from the battle!")
            return "ran"

        else:
            print("\nInvalid choice. Try again.")
            continue

        if monster.is_alive():
            monster_attack(player, monster)

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

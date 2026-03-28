from terminal_legends.monster import Monster

def start_battle(player):
    monster = Monster("Goblin", 15, 4, 10)

    print(f"\n⚔️ A wild {monster.name} appears!")

    while player.is_alive() and monster.is_alive():
        print(f"\n{player.name}: {player.hp}/{player.max_hp} HP")
        print(f"{monster.name}: {monster.hp} HP")

        print("\n1. Attack")
        print("2. Do nothing")

        choice = input("> ")

        if choice == "1":
            damage = player.deal_damage()
            monster.take_damage(damage)
            print(f"You deal {damage} damage!")

        if monster.is_alive():
            damage = monster.deal_damage()
            player.take_damage(damage)
            print(f"The {monster.name} hits you for {damage} damage!")

    if player.is_alive():
        print(f"\nYou defeated the {monster.name}!")
        player.gain_xp(monster.xp_reward)
    else:
        print("\n💀 You died...")

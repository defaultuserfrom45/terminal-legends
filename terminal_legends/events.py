import random


def trigger_random_event(player):
    event_type = random.choice(["gold", "trap", "healer", "potion", "nothing"])

    print("\n=== Random Event ===")

    if event_type == "gold":
        gold_found = random.randint(8, 20)
        player.gold += gold_found
        print(f"You found a treasure chest with {gold_found} gold!")

    elif event_type == "trap":
        damage = random.randint(5, 12)
        player.take_damage(damage)
        print(f"You stepped into a trap and lost {damage} HP!")

    elif event_type == "healer":
        heal_amount = random.randint(8, 15)
        player.hp += heal_amount
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        print(f"A traveling healer restores {heal_amount} HP!")

    elif event_type == "potion":
        player.potions += 1
        print("You found a healing potion!")

    else:
        print("Nothing happened. The road remains quiet...")

    print("====================")

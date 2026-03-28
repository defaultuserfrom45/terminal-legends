from terminal_legends.monster import Monster


def create_boss(player_level):
    boss_hp = 35 + player_level * 5
    boss_attack = 8 + player_level
    boss_xp = 30
    boss_gold = 25

    return Monster("Dragon", boss_hp, boss_attack, boss_xp, boss_gold)

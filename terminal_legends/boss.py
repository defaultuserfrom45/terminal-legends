from terminal_legends.monster import Monster


class Boss(Monster):
    def __init__(self, name, hp, attack, xp_reward, gold_reward):
        super().__init__(name, hp, attack, xp_reward, gold_reward)

    def use_special_attack(self):
        return self.attack + 4


def create_boss(player_level):
    boss_hp = 32 + player_level * 5
    boss_attack = 7 + player_level
    boss_xp = 35
    boss_gold = 30

    return Boss("Dragon", boss_hp, boss_attack, boss_xp, boss_gold)

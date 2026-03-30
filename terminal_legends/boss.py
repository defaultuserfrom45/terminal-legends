from terminal_legends.monster import Monster


class Boss(Monster):
    def __init__(self, name, hp, attack, xp_reward, gold_reward):
        super().__init__(name, hp, attack, xp_reward, gold_reward)

    def use_special_attack(self):
        return self.attack + 5


def create_boss(player_level):
    boss_hp = 35 + player_level * 5
    boss_attack = 8 + player_level
    boss_xp = 30
    boss_gold = 25

    return Boss("Dragon", boss_hp, boss_attack, boss_xp, boss_gold)

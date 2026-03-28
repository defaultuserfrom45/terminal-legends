class Monster:
    def __init__(self, name, hp, attack, xp_reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.xp_reward = xp_reward

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def deal_damage(self):
        return self.attack
        

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class

        if char_class == "Warrior":
            self.max_hp = 30
            self.attack = 6
        elif char_class == "Mage":
            self.max_hp = 20
            self.attack = 8
        elif char_class == "Rogue":
            self.max_hp = 25
            self.attack = 7
        else:
            self.max_hp = 25
            self.attack = 5

        self.hp = self.max_hp
        self.level = 1
        self.xp = 0

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def deal_damage(self):
        return self.attack

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gained {amount} XP!")

        if self.xp >= 20:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.max_hp += 5
        self.attack += 1
        self.hp = self.max_hp

        print(f"\n🔥 LEVEL UP! {self.name} is now level {self.level}!")

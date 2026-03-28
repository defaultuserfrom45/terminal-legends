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
        self.xp_to_next_level = 20
        self.potions = 2
        self.gold = 0

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def deal_damage(self):
        return self.attack

    def heal(self):
        if self.potions <= 0:
            print("\nYou have no potions left!")
            return False

        if self.hp == self.max_hp:
            print("\nYour health is already full!")
            return False

        heal_amount = 10
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        self.potions -= 1
        print(f"\nYou used a potion and restored {heal_amount} HP!")
        print(f"Potions left: {self.potions}")
        return True

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gained {amount} XP!")

        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level_up()

    def gain_gold(self, amount):
        self.gold += amount
        print(f"{self.name} received {amount} gold!")

    def level_up(self):
        self.level += 1
        self.max_hp += 5
        self.attack += 1
        self.hp = self.max_hp
        self.xp_to_next_level += 10

        print(f"\nLEVEL UP! {self.name} is now level {self.level}!")
        print(f"Max HP increased to {self.max_hp}.")
        print(f"Attack increased to {self.attack}.")

class Hero:
    def __init__(self, name, health, attack, armor, mana=50):
        self.name = name
        self._health = health
        self.attack = attack
        self.mana = mana
        self.armor = armor

    def __str__(self):
        return f"Nama Hero {self.name}"

    def diserang(self, jumlah):
        self._health = max(self._health - jumlah, 0) # 0 agar saat diserang tidak mines atau malah healing

    def serang(self, target):
        damage = max(self.attack - target.armor, 0)
        target.diserang(damage)
        print(f"{self.name} menyerang {target.name}, damage {damage}")

    @property
    def health(self):
        return self.health

class Archer(Hero):
    def __init__(self, name, health, attack, armor, mana = 50, missChance = 50):
        super().__init__(name, health, attack, armor, mana=50)
        self.missChance = missChance

    def serang(self, target): # overriding nimpa
        super().serang(target)  # kalau mau makai tempelate yang sebelumnya
        print(f"Menyerang menggunakan panah")
        # print(f"Menyerang menggunakan panah ke {target.name}")


class Mage(Hero): 
    pass

class EnergyArcher(Archer):
    def __init__(self, name, health, attack, armor, mana = 50, missChance = 50, energi = 100):
        super().__init__(name, health, attack, armor, mana = 50, missChance = 50)
        self.energi = energi

    def serang(self, target):

        if self.energi >= 20:
            self.energi -= 20
            damage = max(self.attack * 2 - target.armor, 0)
            target.diserang(damage)
            print(f"{self.name} menyerang {target.name}, damage {damage}, sisa energi {self.energi} ")
            

class Healing():
    def heal (self, jumlah):
        self._health += jumlah
        print(f"{self.name} melakukan healing sebesar {jumlah}")

class Support(Archer, Healing):
    pass

roger = Hero("roger", 100, 15, 100)
Windranger = Archer("Windranger", 80, 20, 50, 40)
kimmy = EnergyArcher("kimmy", 100, 20, 30, 40, 50, 30)
nana = Support("nana", 100, 15, 4)
# print(isinstance (axe, Warrior))
# print()

# print(roger.__dict__)

roger.serang(Windranger)

for _ in range(10):
    kimmy.serang(roger)

nana.serang(kimmy) # untuk melihat apakah nana dapt warisan dari hero
nana.heal(10) # untuk melihat apakah nana dapt healing dari hero



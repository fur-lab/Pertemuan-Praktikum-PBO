class Hero:

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attack_diterima = attack_lawan
        self.health -= attack_diterima
        print(f"Darah dari {self.name} tersisa {self.health}")

roger = Hero('roger', 100, 4, 5)
sniper = Hero('sniper', 50, 5, 3)

sniper.serang(roger)


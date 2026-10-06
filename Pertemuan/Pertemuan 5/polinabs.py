from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def __str__(self):
        return f"Nama Hero {self.name}"

    def hitung_damage(self, target):
        return max(self.attack - target.armor, 0)

    def serang(self, target):
        damage = self.hitung_damage(target)
        target.health -= damage
        print(f"{self.name} menyerang {target.name}, damage {damage}")

    @abstractmethod
    def ulti(self, target):
        pass

    def __add__(self, other):
        return self.health + other.attack
    def __sub__(self, burn):
        for i in range(10):
            darah = self.health - burn
            print("darah : ", darah)
        self.health = darah
        print(self.health)


class Mage(Hero):
    def hitung_damage(self, target):
        return self.attack 

    def ulti(self, target):
        return (self.attack * 88)

class Warrior(Hero):
    def hitung_damage(self, target):
        return super().hitung_damage(target) + 5 # bonus 5

class Minion():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

sora = Warrior("Sora", 60, 100, 50)
eudora = Mage("Eudora", 100, 60,5)
Minion = Minion("Minion", 10, 2)

# sora.serang(eudora)
# eudora.serang(sora)
# eudora.serang(Minion)

# print(sora.ulti(eudora))

# print(eudora + 100)
# print(eudora + sora)

print(isinstance(eudora, Mage)) # buat cek true false, kalau mage true begitu juga kalau parentnya Hero. kalau warrior false.
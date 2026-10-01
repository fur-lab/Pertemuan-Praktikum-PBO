import random


class Hero:
    # pass
    # hero1 = Hero() #m Membuat objek
    # hero1.name = 'sniper'

    # print(hero1)
    # print(hero1.name)
    jumlahHero = 0

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack
        print("nama saya rafli")

    def healthUp(self, up):
        self.health += up

    def levelUp(self): # Ini instance method karena menggunakan self sebagai parameter
            self.health += 5
            self.attack += 3
            self.armor += 2

    @classmethod
    def totalHero(cls):  # Ini class method karena menggunakan cls sebagai parameter
        print(f"total hero {cls.jumlahHero}")

    @staticmethod
    def 

roger = Hero('roger', 100, 4, 5)

print(roger.name)
print(roger.__dict__)

roger.healthUp(50)
print(roger.__dict__)

sniper = Hero('sniper', 50, 5, 3) # Setiap bikin nambahkan baru, class init bakal berjalan 

    


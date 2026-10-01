# class Hero:
#     jumlahHero = 0

#     def __init__(self, name, health, armor, attack):
#         self.name = name
#         self.health = health
#         self.armor = armor
#         self.attack = attack
# INI CARA BIASA

# from dataclasses import dataclass, field

# @dataclass
# class Hero:
#     name = str
#     health = int
#     armor = int
#     attack = int
# INI PAKAI LIBRARY, Biar kebih keliatan Javanya 
# Post init (???)

class Hero:
    jumlahHero = 0

    def __init__(self, name, health, armor, attack):
        self.__name = name
        self.__health = health
        self.armor = armor
        self.attack = attack

    @property
    def getName(self):
        return self.__name

    @property
    def getHealth(self):
        return self.__health

    @getHealth.setter
    def health(self, darahBaru) -> int  : #Biar lebih jago -> int
        if darahBaru <= 0:
            self.__health = 0
        else :
            self.__health = darahBaru

sniper = Hero("lele", 100, 10, 20)

# sniper.health = 150
# print(sniper.health)
# print(sniper.__name) # Gabisa karena private
# print(sniper.__dict__)

# print(sniper.getName) # Ini untuk mengakses name dengan cara getter

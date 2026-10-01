# ASOSIASI

class Shop:
    def __init__(self, nama):
        self.nama = nama


    def proses_pembelian(self, hero, item):
        if hero.gold >= item.harga:
            hero.gold -= item.harga
            print(f"{self.nama} beli {item.nama}"
                f"({item.harga} gold), sisa gold {hero.gold}")
            return True
        print(f"[{self.nama}] Gold {hero.nama} tidak cukup untuk {item.nama}")
        return False

class Hero:
    jumlahHero = 0 
    MAKS_SLOT = 4

    def __init__(self, nama, health, mana, armor, attack, gold, list_skill):
        self.nama = nama
        self.health = health
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.gold = gold
        self.list_skill = list_skill
        self._inventory =[] # Agregasi
        self._skill = [Skill(nama, dmg, mana) for name , dmg, mana in list_skill]
        Hero.jumlahHero += 1

# Penggunaan ASOSIASI
    def beli_item(self, shop, item):
        if len (self.inventory) >= Hero.MAKS_SLOT:
            print(f"Inventory {self.nama} dah penuh brok")
            return
        if shop.proses_pembelian(self, item):
            self.inventory.append(item)

    def ambil_item(self, item):
        if len(self.)

    def cast_skill(self, nomor_skill, lawan):
        skill = self._skills[nomor_skill - 1]
        if self.nama < skill.mana_cost:
            print(f"Mana {self.nama}tidak cukup untuk {skill.nama}")
            return
        self.mana -= skill.mana_cost
        lawan.health -= skill.damage
        print(f"{self.nama} memakai {skill.nama} ke {lawan.nama},"
                f"sisa health {lawan.nama} : {lawan.health}")

class Item:
    def __init__(self, nama, harga, bonus_attack=0, bonus_armor=0):
        self.nama = nama
        self.harga = harga
        self.bonus_attack = bonus_attack
        self.bonus_armor = bonus_armor

    def __str__(self):
        return(f"item : {self.nama} + {self.bonus_attack} attack | +{self.bonus_armor} armor")

class Skill:
    def __init__(self, nama, damage, mana_cost):
        self.nama = nama
        self.damage = damage
        self.mana_cost = mana_cost

    def __str__(self):
        return f"{self.nama} ({self.damage} damage, {self.mana_cost} mana)"
        

brodi = Hero("Brodi", health=3000, mana=1000, armor=10, attack=100, gold=400, list_skill=[("tembak", 100, 10), ("loncat", 10, 1)])
shop = Shop("Belanja Item")
bod = Item("BOD", 3100, bonus_attack=160)
winter = Item("Winter", 2140, bonus_attack=15, bonus_armor=45)

brodi.beli_item(shop, bod)

print()
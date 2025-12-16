import sys
from zlib import DEF_MEM_LEVEL

class Pokemon:
    def __init__(self,name, hp, dmg, element):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.dmg = dmg
        self.element = element.lower()
    def __str__(self):
        return (
            f"Ten pokemon {self.name}\n"
            f"Mau: {self.hp}\n"
            f"Sat thuong gay ra : {self.dmg}\n"
            f"He: {self.element}"
        )

    def get_multipler(self, other):
        m = 1.0
        t1 = self.element
        t2 = other.element
        if t1 == "nuoc" and t2 == "hoa":
            m = 1.20
        if t1 == "hoa" and t2 == "co":
            m = 1.25
        if t1 == "co" and t2 == "dat":
            m = 1.15
        if t1 == "dat" and t2 =="nuoc":
            m = 1.30
        if t1 == "co" and t2 == "nuoc":
            m = 1.10
        if t1 == "dat" and t2 =="lua":
            m = 1.35
        return m

    def __gt__(self, other):
        score = 0
        if self.hp > other.hp:
            score += 1
        if self.dmg > other.dmg:
            score += 1
        self_other = self.get_multipler(other)
        other_self = other.get_multipler(self)
        if self_other > other_self: # tuc la self khac he other hoac other khac he self
            score += 1
        return score >= 2
def get_winner(name):
    with open("WINNER.OUT", "w", encoding="utf-8") as f:
        f.write(name)
    sys.exit()
def fight(p1:Pokemon, p2:Pokemon):
    # xac dinh con pokemon nao danh luot dau tien truoc
    # # sau do cho vong lap cho toi khi 1 trong 2 con co hp <=0

    if p1 > p2:
        first = p2
        second = p1
        print(f"Pokemon {first.name} tan cong Pokemon {second.name}")
    else:
        first = p1
        second = p2
        print(f"Pokemon {first.name} tan cong Pokemon {second.name}")
    round = 1
    while True:
        print(f"--- Vong dau thu {round} ---")
        mult = first.get_multipler(second)
        dmg = first.dmg * mult
        second.hp -= dmg
        if second.hp <= 0 :
            second.hp = 0
        print(f"{first.name} gay ra {dmg} sat thuong, mau hien tai: {first.hp}")
        print(f"{second.name} con lai {second.hp}")
        if second.hp == 0:
            print(f"Ket thuc, {first.name} chien thang")
            get_winner(first.name)
        first, second = second, first
        round += 1

def nhap():
    print("Nhap thong tin: ")
    name = input("Ten: ")
    hp = float(input("Mau (HP): "))
    dmg = float(input("Sat thuong (Attack): "))
    ele = input("He (nuoc, hoa, co, dat): ")
    return name, hp, dmg, ele
def main():
    poke_list = []
    n = int (input("Nhap so luong pokemon: "))
    for _ in range(n):
        print(f"Pokemon thu {_+1}")
        name, hp, dmg, element = nhap()
        poke_list.append(Pokemon(name, hp, dmg, element))
    idx1 = int(input("Chon so thu tu pokemon 1: "))
    idx2 = int(input("Chon so thu tu pokemon 2: "))
    assert 0 <= idx1 < n and 0 <= idx2 < n and idx1 != idx2
    fight(poke_list[idx1], poke_list[idx2])

if __name__ == "__main__":
    main()

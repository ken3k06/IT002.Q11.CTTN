# Link de : https://www.hackerrank.com/contests/de-thi-thuc-hanh/challenges/freefire

import sys

class Gun:
    def __init__(self, name, bang_dan, sat_thuong, toc_do, so_bang_dan, hao_mon):
        self.name = name
        self.bang_dan = bang_dan
        self.sat_thuong = sat_thuong
        self.toc_do = toc_do
        self.so_bang_dan = so_bang_dan
        self.hao_mon = hao_mon
    def get_true_dmg(self):
        dmg = self.sat_thuong
        if self.hao_mon == 1:
            return dmg
        else:
            return dmg * self.hao_mon

    def get_delay(self):
        rate = self.toc_do
        if self.hao_mon < 1:
            rate /= 2.0
        return 1.0 / rate
    def calculate_dps(self, time_limit):
        dmg = self.get_true_dmg()
        delay = self.get_delay()

        total = int(self.so_bang_dan * self.bang_dan)
        current_time = 0.0
        total_dmg = 0
        current_size = self.bang_dan

        # Bắn xong -> Trừ đạn -> Cộng thời gian delay -> Kiểm tra nạp đạn
        while current_time <= time_limit and total > 0:
            total_dmg += dmg
            total -= 1
            current_size -= 1
            current_time += delay

            if current_size == 0 and total > 0:
                current_time += 2.0
                current_size = self.bang_dan

        return total_dmg

class SungNgan(Gun):
    def __init__(self, name, bang_dan, sat_thuong, toc_do, so_bang_dan, hao_mon):
        super().__init__(name, bang_dan, sat_thuong, toc_do, so_bang_dan, hao_mon)

class SungTruong(Gun):
    def __init__(self, name, bang_dan, sat_thuong, toc_do, so_bang_dan, hao_mon, skin_tang_dam):
        super().__init__(name, bang_dan, sat_thuong, toc_do, so_bang_dan, hao_mon)
        self.skin_tang_dam = skin_tang_dam

    def get_true_dmg(self):

        return super().get_true_dmg() + self.skin_tang_dam

class SungBanTia(Gun):
    def __init__(self, name, bang_dan, sat_thuong, toc_do, so_bang_dan, hao_mon):
        super().__init__(name, bang_dan, sat_thuong, toc_do, so_bang_dan, hao_mon)

    def get_delay(self):
        return super().get_delay() + 1.0

def create_gun(type_id, num_mags, wear, iterator):
    if type_id == 1:
        return SungNgan("G18", 12, 2, 1, num_mags, wear)
    elif type_id == 2:
        return SungNgan("M500", 5, 4, 0.5, num_mags, wear)
    elif type_id == 3:
        skin = float(next(iterator))
        return SungTruong("MP40", 20, 3, 5, num_mags, wear, skin)
    elif type_id == 4:
        skin = float(next(iterator))
        return SungTruong("AK", 30, 5, 1, num_mags, wear, skin)
    elif type_id == 5:
        return SungBanTia("SVD", 10, 5, 0.5, num_mags, wear)
    elif type_id == 6:
        return SungBanTia("AWM", 5, 10, 0.5, num_mags, wear)
    return None
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        guns = []
        for _ in range(n):
            type_id = int(next(iterator))
            num_mags = int(next(iterator))
            wear = float(next(iterator))
            guns.append(create_gun(type_id, num_mags, wear, iterator))
        time_limit = float(next(iterator))
        for gun in guns:
            dmg = float(gun.calculate_dps(time_limit))
            if dmg.is_integer():
                print(f"{gun.name}: {int(dmg)}")
            else:
                print(f"{gun.name}: {round(dmg, 2)}")

    except StopIteration:
        pass
if __name__ == "__main__":
    main()

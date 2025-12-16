from abc import ABC, abstractmethod
import random
class ChungCu(ABC):
    def __init__(self, ten, soTang, dienTich:float, tenQL, soHuu):
        self.ten = ten
        self.soTang = soTang
        self.dienTich = dienTich
        self.tenQL = tenQL
        self.soHuu = soHuu
    def thong_bao(self):
        return (
            f"{self.tenQL} ----- {self.ten} ---- {self.soHuu}"
        )
    @abstractmethod
    def tien_phong(self):
        pass


class CCVinHome(ChungCu):
    def __init__(self, ten, soTang, dienTich, tenQL):
        super().__init__(ten, soTang, dienTich, tenQL, soHuu = "Vinhomes")
    def tien_phong(self):
        if self.dienTich > 600:
            r = random.randint(10,15)
            return r*self.soTang * 6
        else:
            r = random.randint(6,10)
            return r*self.soTang * 6


class CCBcon(ChungCu):
    def __init__(self, ten, soTang, dienTich, tenQL):
        super().__init__(ten, soTang, dienTich, tenQL, soHuu = "Bcons")
    def tien_phong(self):
        if self.dienTich > 600:
            r = random.randint(8,12)
            return r*self.soTang * 6
        else:
            r = random.randint(5,8)
            return r*self.soTang * 6
def nhap_chung_cu(name):
    print(f"Nhập thông tin cho chung cư {name}")
    ten = input("Ten chung cu: ")
    so_tang = int(input("So tang: "))
    dien_tich = float(input("Dien tich (m2): "))
    ten_ql = input("Ten quan ly: ")
    return ten, so_tang, dien_tich, ten_ql

def main():
    danh_sach = []
    cc_vin = int(input("Nhap so luong chung cu VinHomes: "))
    for _ in range(cc_vin):
        ten, so_tang, dien_tich, ten_ql = nhap_chung_cu("Vinhomes")
        cc = CCVinHome(ten, so_tang, dien_tich, ten_ql)
        danh_sach.append(cc)
    cc_bcon = int(input("Nhap so luong chung cu Bcons: "))
    for _ in range(cc_bcon):
        ten, so_tang, dien_tich, ten_ql = nhap_chung_cu("Bcons")
        cc = CCBcon(ten, so_tang, dien_tich, ten_ql)
        danh_sach.append(cc)
    print("---Gui thong bao---")
    for cc in danh_sach:
        print(cc.thong_bao())
    tien = 0
    for cc in danh_sach:
        doanh_thu = cc.tien_phong()
        tien += doanh_thu
        print(f"Chung cu {cc.ten} ({cc.soHuu}) : {tien} trieu")
    print(f"Tong doanh thu: {tien} trieu")
if __name__ == "__main__":
    main()

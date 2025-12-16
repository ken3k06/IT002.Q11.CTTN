from abc import ABC, abstractmethod


class NhanVien(ABC):
    def __init__(self, nv_id, ho_ten, tuoi, sdt, email, luong_cb):
        self.nv_id = nv_id
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.sdt = sdt
        self.email = email
        self.luong_cb = luong_cb

    @abstractmethod
    def tinh_luong(self) -> float:
        pass


class LapTrinhVien(NhanVien):
    def __init__(self, nv_id, ho_ten, tuoi, sdt, email, luong_cb, overtime):
        super().__init__(nv_id, ho_ten, tuoi, sdt, email, luong_cb)
        self.overtime = overtime

    def tinh_luong(self) -> float:
        return self.luong_cb + self.overtime * 200000


class KiemChungVien(NhanVien):
    def __init__(self, nv_id, ho_ten, tuoi, sdt, email, luong_cb, so_bug):
        super().__init__(nv_id, ho_ten, tuoi, sdt, email, luong_cb)
        self.so_bug = so_bug

    def tinh_luong(self) -> float:
        return self.luong_cb + self.so_bug * 50000



def nhap_lap_trinh_vien():
    nv_id = input()
    ho_ten = input()
    tuoi = int(input())
    sdt = input()
    email = input()
    luong_cb = float(input())
    overtime = int(input())
    return LapTrinhVien(nv_id, ho_ten, tuoi, sdt, email, luong_cb, overtime)

if __name__ == "__main__":
    pass

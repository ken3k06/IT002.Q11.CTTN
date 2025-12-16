from abc import ABC, abstractmethod
from typing import List


class NhanVien(ABC):
    def __init__(self, ho_ten, ngay_sinh, luong_cb):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.luong_cb = luong_cb

    @abstractmethod
    def tinh_luong(self) -> float:
        pass

    def xuat_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngày sinh: {self.ngay_sinh}")
        print(f"Lương: {self.tinh_luong():,.0f} VND")


class VanPhong(NhanVien):
    def __init__(self, ho_ten, ngay_sinh, luong_cb, so_ngay_lam, tro_cap):
        super().__init__(ho_ten, ngay_sinh, luong_cb)
        self.so_ngay_lam = so_ngay_lam
        self.tro_cap = tro_cap

    def tinh_luong(self):
        return self.luong_cb + self.so_ngay_lam * 200000 + self.tro_cap


class SanXuat(NhanVien):
    def __init__(self, ho_ten, ngay_sinh, luong_cb, so_san_pham):
        super().__init__(ho_ten, ngay_sinh, luong_cb)
        self.so_san_pham = so_san_pham

    def tinh_luong(self):
        return self.luong_cb + self.so_san_pham * 2000


class Quanly(NhanVien):
    def __init__(self, ho_ten, ngay_sinh, luong_cb, he_so, thuong):
        super().__init__(ho_ten, ngay_sinh, luong_cb)
        self.he_so = he_so
        self.thuong = thuong

    def tinh_luong(self):
        return self.luong_cb * self.he_so + self.thuong


class CongTy:
    def __init__(self):
        self.ds_nv: List[NhanVien] = []

    def nhap_thong_tin(self, nv):
        self.ds_nv.append(nv)

    def tinh_luong_tung_nv(self):
        for nv in self.ds_nv:
            print(f"Lương của {nv.ho_ten}: {nv.tinh_luong()}")
            print("-" * 30)

    def xuat_thong_tin(self):
        for nv in self.ds_nv:
            nv.xuat_thong_tin()
            print("-" * 30)

    def tong_luong(self):
        tong = 0
        for nv in self.ds_nv:
            tong += nv.tinh_luong()
        return tong

    def find_nv(self, name):
        return [nv for nv in self.ds_nv if name.lower() in nv.ho_ten.lower()]


if __name__ == "__main__":
    cong_ty = CongTy()
    mau = [
        VanPhong(
            ho_ten="Nguyễn Văn An",
            ngay_sinh="12/03/1995",
            luong_cb=5_000_000,
            so_ngay_lam=22,
            tro_cap=1_000_000,
        ),
        VanPhong(
            ho_ten="Trần Thị Bình",
            ngay_sinh="08/07/1998",
            luong_cb=4_800_000,
            so_ngay_lam=20,
            tro_cap=800_000,
        ),
        SanXuat(
            ho_ten="Lê Văn Cường",
            ngay_sinh="01/01/1990",
            luong_cb=4_500_000,
            so_san_pham=350,
        ),
        SanXuat(
            ho_ten="Phạm Thị Dung",
            ngay_sinh="22/11/1996",
            luong_cb=4_200_000,
            so_san_pham=280,
        ),
        Quanly(
            ho_ten="Hoàng Minh Đức",
            ngay_sinh="15/05/1985",
            luong_cb=8_000_000,
            he_so=1.5,
            thuong=5_000_000,
        ),
    ]
    for nv in mau:
        cong_ty.nhap_thong_tin(nv)
    cong_ty.xuat_thong_tin()
    cong_ty.tinh_luong_tung_nv()

    print("=== TỔNG LƯƠNG CÔNG TY ===")
    print(f"{cong_ty.tong_luong():,.0f} VND")
    print("=== TÌM NHÂN VIÊN THEO TÊN ===")
    ket_qua = cong_ty.find_nv("Đức")
    for nv in ket_qua:
        nv.xuat_thong_tin()

from abc import ABC, abstractmethod


class SinhVien(ABC):
    def __init__(self, mssv, ho_va_ten, dia_chi, tong_tin_chi, diem_tb):
        self.mssv = mssv
        self.ho_va_ten = ho_va_ten
        self.dia_chi = dia_chi
        self.tong_tin_chi = tong_tin_chi
        self.diem_tb = diem_tb

    @abstractmethod
    def xet_tot_nghiep(self) -> bool:
        pass

    def __str__(self):
        return f"MSSV: {self.mssv}\nHo va ten: {self.ho_va_ten}\nDia chi: {self.dia_chi}\nTong tin chi: {self.tong_tin_chi}\nDiem trung binh: {self.diem_tb}"


class SinhVienDaiHoc(SinhVien):
    def __init__(
        self,
        mssv,
        ho_va_ten,
        dia_chi,
        tong_tin_chi,
        diem_tb,
        ten_luan_van,
        diem_luan_van,
    ):
        super().__init__(mssv, ho_va_ten, dia_chi, tong_tin_chi, diem_tb)
        self.ten_luan_van = ten_luan_van
        self.diem_luan_van = diem_luan_van

    def xet_tot_nghiep(self):
        if self.tong_tin_chi >= 170 and self.diem_tb >= 5 and self.diem_luan_van >= 5:
            return True
        else:
            return False

    def __str__(self):
        return (
            super().__str__()
            + f"\nTen luan van: {self.ten_luan_van}"
            + f"\nDiem luan van: {self.diem_luan_van}"
        )


class SinhVienCaoDang(SinhVien):
    def __init__(
        self, mssv, ho_va_ten, dia_chi, tong_tin_chi, diem_tb, diem_thi_tot_nghiep
    ):
        super().__init__(mssv, ho_va_ten, dia_chi, tong_tin_chi, diem_tb)
        self.diem_tot_nghiep = diem_thi_tot_nghiep

    def xet_tot_nghiep(self) -> bool:
        if self.tong_tin_chi >= 120 and self.diem_tb >= 5 and self.diem_tot_nghiep >= 5:
            return True
        else:
            return False

    def __str__(self):
        return super().__str__() + f"\nDiem tot nghiep: {self.diem_tot_nghiep}"


if __name__ == "__main__":
    print("Dien thong tin cao dang: ")
    mssv = input("MSSV: ")
    ho_va_ten = input("Ho va ten: ")
    dia_chi = input("Dia chi: ")
    tong_tin_chi = int(input("Tong tin chi: "))
    diem_tb = float(input("Diem trung binh: "))
    diem_thi_tot_nghiep = float(input("Diem tot nghiep: "))

    sv_cd = SinhVienCaoDang(
        mssv, ho_va_ten, dia_chi, tong_tin_chi, diem_tb, diem_thi_tot_nghiep
    )
    print("Dien thong tin sinh vien: ")
    mssv = input("MSSV: ")
    ho_va_ten = input("Ho va ten: ")
    dia_chi = input("Dia chi: ")
    tong_tin_chi = int(input("Tong tin chi: "))
    diem_tb = float(input("Diem trung binh: "))
    ten_luan_van = input("Ten luan van: ")
    diem_luan_van = float(input("Diem tot nghiep: "))

    sv_dh = SinhVienDaiHoc(
        mssv, ho_va_ten, dia_chi, tong_tin_chi, diem_tb, ten_luan_van, diem_luan_van
    )
    if sv_cd.xet_tot_nghiep():
        print("Sinh vien cao dang da tot nghiep")
    if sv_dh.xet_tot_nghiep():
        print("Sinh vien dai hoc da tot nghiep")

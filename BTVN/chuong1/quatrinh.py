import sys


    def __init__(self, ID, Name, diem_toan, diem_van, diem_ly, diem_hoa):
        self.ID = ID
        self.Name = Name
        self.diem_toan = float(diem_toan)
        self.diem_van = float(diem_van)
        self.diem_ly = float(diem_ly)
        self.diem_hoa = float(diem_hoa)

    @property
    def diem_trung_binh(self):
        sum = self.diem_toan + self.diem_hoa + self.diem_ly + self.diem_van
        return sum / 4

    # dung property cho diem trung binh vi: day la thuoc tinh khong can duoc luu
    # cung nhu khong cho phep chinh sua truc tiep
    def __str__(self):
        dtb = self.diem_trung_binh
        return (
            f"---Thông tin học sinh---\n"
            f"Mã HS: {self.ID}\n"
            f"Tên: {self.Name}\n"
            f"Điểm TB: {dtb:.2f}\n"
        )


if __name__ == "__main__":
    sid = input("Mã học sinh: ")
    name = input("Họ và tên: ")
    toan = float(input("Toán: "))
    van = float(input("Văn: "))
    ly = float(input("Vật lý: "))
    hoa = float(input("Hóa học: "))
    student = HocSinh(sid, name, toan, van, ly, hoa)
    print(student)

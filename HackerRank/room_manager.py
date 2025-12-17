# link đề: https://www.hackerrank.com/contests/de-thi-thuc-hanh/challenges/room-manager
from typing import List
class Room:
    def __init__(self, ten, floor, num_id, capacity):
        self.ten = ten
        self.floor = floor
        self.num_id = num_id
        self.capacity = capacity


def nhap_thong_tin():
    ten = input("Ten phong: ")
    floor = int(input("So tang: "))
    num_id = int(input("So phong: "))
    capacity = int(input("Suc chua: "))
    return ten, floor, num_id, capacity


class LyThuyet(Room):
    def __init__(self, ten, floor, num_id, capacity, may_lanh):
        super().__init__(ten, floor, num_id, capacity)
        self.may_lanh = may_lanh


class ThucHanh(Room):
    def __init__(self, ten, floor, num_id, capacity, so_may_tinh):
        super().__init__(ten, floor, num_id, capacity)
        self.so_may_tinh = so_may_tinh


class GiangDuong(Room):
    def __init__(self, ten, floor, num_id, capacity, so_may_chieu):
        super().__init__(ten, floor, num_id, capacity)
        self.so_may_chieu = so_may_chieu


def nhap():
    room_type = int(input("Nhap loai phong: "))
    ten, floor, num_id, capacity = nhap_thong_tin()

    if room_type == 1:
        print("-----Phong Ly thuyet-----")
        may_lanh = int(input("So may lanh: ")) == 1
        return LyThuyet(ten, floor, num_id, capacity, may_lanh)

    elif room_type == 2:
        print("-----Phong thuc hanh-----")
        so_may_tinh = int(input("So may tinh: "))
        return ThucHanh(ten, floor, num_id, capacity, so_may_tinh)

    elif room_type == 3:
        print("-----Giang duong-----")
        so_may_chieu = int(input("So may chieu: "))
        return GiangDuong(ten, floor, num_id, capacity, so_may_chieu)
def main():
    n = int(input("Nhap so luong phong: "))
    lst_room:List[Room] = []
    for _ in range(n):
        room = nhap()
        if room is not None:
            lst_room.append(room)
    total_capacity = 0
    k = int(input("Nhap suc chua cua phong can tim: "))
    for room in lst_room:
        total_capacity += room.capacity
    print(f"Tong suc chua: {total_capacity}")
    # tim phong phu hop: uu tien lau thap, so phong thap
    cand = [r for r in lst_room if r.capacity >= k]
    cand.sort(key = lambda r: (r.capacity, r.floor, r.num_id))
    print(f"Phong phu hop nhat: {cand[0].ten}")
    # sort theo capacity truoc, roi toi tang roi toi so phong
if __name__ == "__main__":
    main()

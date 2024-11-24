class Vehicule:
    # Biến class đếm số lượng xe
    count = 0

    def __init__(self, ten, dung_tich_dong_co, hang_sx):
        self.ten = ten
        self.dung_tich_dong_co = dung_tich_dong_co
        self.hang_sx = hang_sx
        Vehicule.count += 1

    # Phương thức class hiển thị số lượng xe
    @classmethod
    def hien_thi_so_luong_xe(cls):
        print(f"Tổng số lượng xe: {cls.count}")

    # Phương thức hiển thị thông tin xe
    def hienthi(self):
        return f"Tên: {self.ten}, Dung tích động cơ: {self.dung_tich_dong_co}cc, Hãng sản xuất: {self.hang_sx}"


class XeTai(Vehicule):
    countXeTai = 0
    def __init__(self, ten, dung_tich_dong_co, hang_sx, loai_xe, tai_trong):
        super().__init__(ten, dung_tich_dong_co, hang_sx)
        self.loai_xe = loai_xe
        self.tai_trong = tai_trong
        XeTai.countXeTai += 1

    @classmethod
    def hien_thi_so_luong_xe_tai(cls):
        print(f"Tổng số lượng xe tải: {cls.countXeTai}")
    
    def hienthi(self):
        base_info = super().hienthi()
        return f"{base_info}, Loại xe: {self.loai_xe}, Tải trọng: {self.tai_trong} tấn"


class XeKhach(Vehicule):
    countXeKhach = 0
    def __init__(self, ten, dung_tich_dong_co, hang_sx, so_nguoi):
        super().__init__(ten, dung_tich_dong_co, hang_sx)
        self.so_nguoi = so_nguoi
        XeKhach.countXeKhach += 1

    @classmethod
    def hien_thi_so_luong_xe_khach(cls):
        print(f"Tổng số lượng xe khách: {cls.countXeKhach}")

    def hienthi(self):
        base_info = super().hienthi()
        return f"{base_info}, Số người: {self.so_nguoi}"


# Tạo danh sách xe
danh_sach_xe = [
    XeTai("Xe tải Hino", 4000, "Hino", "Xe tải hạng nặng", 10),
    XeKhach("Xe khách 45 chỗ", 2500, "Thaco", 45),
    XeTai("Xe tải Isuzu", 3000, "Isuzu", "Xe tải nhẹ", 5),
    XeKhach("Xe khách 16 chỗ", 2200, "Ford", 16),
]

# Hiển thị thông tin tất cả các xe trong danh sách
for xe in danh_sach_xe:
    print(xe.hienthi())

# Hiển thị tổng số lượng xe
XeTai.hien_thi_so_luong_xe_tai()

XeKhach.hien_thi_so_luong_xe_khach()

Vehicule.hien_thi_so_luong_xe()
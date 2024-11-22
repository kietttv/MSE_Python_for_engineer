import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

# Hàm tự tạo cửa sổ thông báo
def custom_messagebox(title, message, box_type="info"):
    # Tạo một cửa sổ popup
    popup = ctk.CTkToplevel()
    popup.title(title)
    popup.geometry("300x150")
    popup.grab_set()  # Giữ cửa sổ chính không hoạt động khi popup mở

    # Tính toán vị trí để mở cửa sổ popup ở giữa màn hình
    window_width = 300
    window_height = 150

    # Lấy kích thước màn hình và cửa sổ chính
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    # Tính toán tọa độ x, y của cửa sổ sao cho cửa sổ mở ở giữa màn hình
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Đặt vị trí cho cửa sổ popup
    popup.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Nhãn hiển thị thông báo
    lbl_message = ctk.CTkLabel(popup, text=message, wraplength=250, justify="center")
    lbl_message.pack(pady=20)

    # Tạo nút OK đóng cửa sổ popup
    btn_ok = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    btn_ok.pack(pady=10)

# Hàm kiểm tra và xử lý lưu dữ liệu
def save_data():
    errors = []
    
    # Kiểm tra các trường nhập liệu
    if not entry_name.get():
        errors.append("Tên không được để trống.")
    if not combo_start.get() or combo_start.get() not in ["Hà Nội", "TP.HCM", "Đà Nẵng"]:
        errors.append("Vui lòng chọn điểm đi hợp lệ.")
    if not combo_end.get() or combo_end.get() not in ["Hà Nội", "TP.HCM", "Đà Nẵng"]:
        errors.append("Vui lòng chọn điểm đến hợp lệ.")
    if not date_entry.get():
        errors.append("Vui lòng chọn ngày.")
    else:
        # Lấy ngày nhập vào từ DateEntry
        entered_date = datetime.strptime(date_entry.get(), "%d/%m/%Y").date()

        # Lấy ngày hiện tại
        current_date = datetime.today().date()

        # So sánh ngày nhập vào với ngày hiện tại
        if entered_date < current_date:
            errors.append("Ngày không thể nhỏ hơn ngày hiện tại.")
    
    # Hiển thị thông báo lỗi nếu có
    if errors:
        custom_messagebox("Lỗi nhập liệu", "\n".join(errors))
    else:
        data = (
            f"Tên: {entry_name.get()}\n"
            f"Điểm đi: {combo_start.get()}\n"
            f"Điểm đến: {combo_end.get()}\n"
            f"Ngày: {date_entry.get()}"
        )
        custom_messagebox("Thông báo", f"Dữ liệu đã được lưu:\n\n{data}")

# Hàm đóng ứng dụng
def close_app():
    root.destroy()

# Cấu hình giao diện chính CustomTkinter
ctk.set_appearance_mode("Dark")  # Chế độ giao diện: Light, Dark, hoặc System
ctk.set_default_color_theme("blue")  # Chủ đề màu: blue, green, hoặc dark-blue

# Tạo cửa sổ chính
root = ctk.CTk()
root.title("Form Nhập Liệu")
root.geometry("400x350")

# Tính toán vị trí để mở cửa sổ ở giữa màn hình
window_width = 400
window_height = 350

# Lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Tính toán tọa độ x, y của cửa sổ sao cho cửa sổ mở ở giữa màn hình
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Đặt vị trí cho cửa sổ
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Hàm kiểm tra tên nhập vào (chỉ cho phép chữ cái và khoảng trắng)
def on_validate_name_input(P):
    if P == "" or P.isalpha() or P.isspace():  # Chỉ cho phép chữ cái và khoảng trắng
        return True
    return False

# Hàm kiểm tra chỉ cho phép nhập ngày đúng định dạng dd/mm/yyyy
def on_validate_date_input(P):
    if P == "" or P[-1] in "0123456789/":  # Chỉ cho phép nhập số và dấu "/"
        if len(P) <= 10:  # Đảm bảo không nhập quá dài
            return True
    return False

# Tạo validator cho tên và ngày
vcmd_name = root.register(on_validate_name_input)
vcmd_date = root.register(on_validate_date_input)

# Tạo các nhãn và ô nhập liệu
lbl_name = ctk.CTkLabel(root, text="Tên:")
lbl_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = ctk.CTkEntry(root, placeholder_text="Nhập tên của bạn", validate="key", validatecommand=(vcmd_name, "%P"))
entry_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

lbl_start = ctk.CTkLabel(root, text="Điểm đi:")
lbl_start.grid(row=1, column=0, padx=10, pady=10, sticky="w")
combo_start = ctk.CTkComboBox(root, values=["Hà Nội", "TP.HCM", "Đà Nẵng"], state="readonly")
combo_start.set("Chọn điểm đi")
combo_start.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

lbl_end = ctk.CTkLabel(root, text="Điểm đến:")
lbl_end.grid(row=2, column=0, padx=10, pady=10, sticky="w")
combo_end = ctk.CTkComboBox(root, values=["Hà Nội", "TP.HCM", "Đà Nẵng"], state="readonly")
combo_end.set("Chọn điểm đến")
combo_end.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

lbl_date = ctk.CTkLabel(root, text="Ngày:")
lbl_date.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Tạo DateEntry với định dạng ngày dd/mm/yyyy và chặn ký tự đặc biệt
date_entry = DateEntry(root, date_pattern='dd/mm/yyyy', state="readonly")
date_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

# Tạo nút Lưu và Đóng
btn_save = ctk.CTkButton(root, text="LƯU", command=save_data)
btn_save.grid(row=4, column=0, padx=10, pady=20, sticky="ew")

btn_close = ctk.CTkButton(root, text="ĐÓNG", command=close_app)
btn_close.grid(row=4, column=1, padx=10, pady=20, sticky="ew")

# Định nghĩa layout
root.grid_columnconfigure(1, weight=1)

# Chạy vòng lặp giao diện
root.mainloop()

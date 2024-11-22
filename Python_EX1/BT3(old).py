import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar  # Thư viện Calendar để chọn ngày

# Hàm xác thực và hiển thị thông tin vé máy bay
def validate_ticket_data(combo_departure, combo_destination, entry_date):
    departure_point = combo_departure.get()
    destination_point = combo_destination.get()
    departure_date = entry_date.get()

    if not departure_point or not destination_point:
        messagebox.showerror("Lỗi", "Điểm đi và điểm đến không được để trống!")
        return

    if not departure_date:
        messagebox.showerror("Lỗi", "Ngày đi không được để trống!")
        return

    try:
        # Kiểm tra định dạng ngày (mm/dd/yyyy)
        day, month, year = map(int, departure_date.split('/'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi", "Ngày đi không hợp lệ! Định dạng đúng là mm/dd/yyyy.")
        return

    messagebox.showinfo("Thông báo", f"Thông tin vé máy bay: \nĐiểm đi: {departure_point}\nĐiểm đến: {destination_point}\nNgày đi: {departure_date}")
    


# Hàm mở cửa sổ đặt vé máy bay
def open_ticket_form():
    ticket_window = tk.Toplevel(root)
    ticket_window.title("Đặt Vé Máy Bay")

    # Các label và widget nhập liệu
    label_departure = tk.Label(ticket_window, text="Điểm đi:")
    label_departure.grid(row=0, column=0, padx=10, pady=10)
    combo_departure = ttk.Combobox(ticket_window, values=["Hà Nội", "TP. Hồ Chí Minh", "Đà Nẵng", "Nha Trang", "Cần Thơ"])
    combo_departure.grid(row=0, column=1, padx=10, pady=10)

    label_destination = tk.Label(ticket_window, text="Điểm đến:")
    label_destination.grid(row=1, column=0, padx=10, pady=10)
    combo_destination = ttk.Combobox(ticket_window, values=["Hà Nội", "TP. Hồ Chí Minh", "Đà Nẵng", "Nha Trang", "Cần Thơ"])
    combo_destination.grid(row=1, column=1, padx=10, pady=10)

    label_date = tk.Label(ticket_window, text="Ngày đi (mm/dd/yyyy):")
    label_date.grid(row=2, column=0, padx=10, pady=10)
    entry_date = tk.Entry(ticket_window)
    entry_date.grid(row=2, column=1, padx=10, pady=10)
    
    def save_ticket():
        validate_ticket_data(combo_departure, combo_destination, entry_date)
    
    # Các nút Lưu và Đóng
    save_button = tk.Button(ticket_window, text="Lưu", command=save_ticket)
    save_button.grid(row=3, column=0, padx=10, pady=20)

    close_button = tk.Button(ticket_window, text="Đóng", command=ticket_window.destroy)
    close_button.grid(row=3, column=1, padx=10, pady=20)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giao Diện Đặt Vé Máy Bay")

# Nút mở cửa sổ đặt vé máy bay
ticket_button = tk.Button(root, text="Đặt Vé Máy Bay", command=open_ticket_form)
ticket_button.pack(padx=20, pady=20)

# Cửa sổ chính chạy
root.mainloop()

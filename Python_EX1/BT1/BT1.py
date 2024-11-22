import tkinter as tk
from PIL import Image, ImageTk  # Thêm thư viện PIL để xử lý hình ảnh

def reset_entry_color(entry):
    """Khôi phục màu nền mặc định cho một ô nhập liệu."""
    entry.config(bg="white", fg="black")

def show_error(entry, message):
    """Hiển thị thông báo lỗi và đổi màu nền ô nhập trong 1 giây."""
    error_label.config(text=message, fg="red")
    entry.config(bg="red")
    window.after(500, lambda: (reset_entry_color(entry), error_label.config(text="")))

def on_button_click(event=None):
    weight = entry_weight.get()  # Lấy giá trị từ ô nhập cân nặng
    height = entry_height.get()  # Lấy giá trị từ ô nhập chiều cao

    has_error = False

    try:
        weight = float(weight)
        if weight <= 0:
            raise ValueError
    except ValueError:
        show_error(entry_weight, "Cân nặng không hợp lệ!")
        has_error = True

    try:
        height = float(height)
        if height <= 0:
            raise ValueError
    except ValueError:
        show_error(entry_height, "Chiều cao không hợp lệ!")
        has_error = True

    if not has_error:
        bmi = weight / (height ** 2)  # Tính BMI

        # Hiển thị kết quả BMI trong Label thay vì Entry
        result_label.config(text=f"{bmi:.2f}")

        # Đưa ra kết luận về tình trạng BMI và thay đổi màu nền của result_label
        if bmi < 18:
            status = "Gầy"
            result_label.config(bg="light yellow", fg="black")
            status_label.config(bg="light coral", fg="black")
        elif 18 <= bmi <= 24:
            status = "Bình thường"
            result_label.config(bg="light green", fg="black")  
            status_label.config(bg="light green", fg="black")  
        else:
            status = "Bạn cần giảm cân"
            result_label.config(bg="light coral", fg="black")
            status_label.config(bg="light coral", fg="black")

        # Cập nhật tình trạng BMI vào Label
        status_label.config(text=status)

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tính chỉ số BMI")
window.geometry("600x250")  # Kích thước cửa sổ (rộng x cao)

# Tải và chuyển đổi hình ảnh
image_path = "doctor.png"  # Thay đường dẫn tới hình ảnh của bạn
image = Image.open(image_path)
image = image.resize((150, 150), Image.LANCZOS)  # Thay đổi kích thước hình ảnh nếu cần
photo = ImageTk.PhotoImage(image)

# Tạo Label và gán hình ảnh
label_image = tk.Label(window, width=150, height=150, image=photo)
label_image.image = photo  # Giữ tham chiếu đến đối tượng ảnh để tránh bị xóa
label_image.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky="e")  # Sử dụng rowspan để ảnh không ảnh hưởng đến các hàng khác

# Tạo nhãn và ô nhập liệu cho cân nặng
label_weight = tk.Label(window, text="Nhập cân nặng (kg):")
label_weight.grid(row=0, column=1, padx=10, pady=10, sticky="e")

entry_weight = tk.Entry(window, width=30)
entry_weight.grid(row=0, column=2, padx=10, pady=10)

# Tạo nhãn và ô nhập liệu cho chiều cao
label_height = tk.Label(window, text="Nhập chiều cao (m):")
label_height.grid(row=1, column=1, padx=10, pady=10, sticky="e")

entry_height = tk.Entry(window, width=30)
entry_height.grid(row=1, column=2, padx=10, pady=10)

# Tạo nút bấm để tính BMI
button = tk.Button(window, text="Tính BMI", command=on_button_click)
button.grid(row=2, column=2, columnspan=2, pady=10)

# Tạo nhãn và Label để hiển thị kết quả BMI với viền
label_result = tk.Label(window, text="Kết quả BMI:")
label_result.grid(row=4, column=1, padx=10, pady=10, sticky="e")

result_label = tk.Label(window, width=25, bg="white", fg="black", relief="solid", bd=1)
result_label.grid(row=4, column=2, padx=10, pady=10)

# Tạo nhãn và Label để hiển thị tình trạng BMI với viền
label_status = tk.Label(window, text="Tình trạng BMI:")
label_status.grid(row=5, column=1, padx=10, pady=10, sticky="e")

status_label = tk.Label(window, width=25, bg="white", fg="black", relief="solid", bd=1)
status_label.grid(row=5, column=2, padx=10, pady=10)

# Thêm nhãn hiển thị thông báo lỗi
error_label = tk.Label(window, text="", fg="red")
error_label.grid(row=6, column=2, columnspan=2, pady=10)

# Liên kết phím Enter với hàm `on_button_click`
entry_weight.bind("<Return>", on_button_click)
entry_height.bind("<Return>", on_button_click)

# Chạy vòng lặp chính
window.mainloop()

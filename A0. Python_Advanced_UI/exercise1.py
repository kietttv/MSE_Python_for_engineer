import tkinter as tk
import PIL, ImageTk

def reset_entry_color(entry):
    """Khôi phục màu nền mặc định cho một ô nhập liệu."""
    entry.config(bg="white")

def show_error(entry, message):
    """Hiển thị thông báo lỗi và đổi màu nền ô nhập trong 1 giây."""
    error_label.config(text=message, fg="red")
    entry.config(bg="red")
    window.after(1000, lambda: (reset_entry_color(entry), error_label.config(text="")))

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

        # Hiển thị kết quả BMI trong Entry readonly
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"{bmi:.2f}")
        result_entry.config(state="readonly")

        # Đưa ra kết luận về tình trạng BMI
        if bmi < 18:
            status = "Gầy"
        elif 18 <= bmi <= 24:
            status = "Bình thường"
        else:
            status = "Mập z ba"

        status_entry.config(state="normal")
        status_entry.delete(0, tk.END)
        status_entry.insert(0, status)
        status_entry.config(state="readonly")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tính chỉ số BMI")
window.geometry("500x350")  # Kích thước cửa sổ (rộng x cao)

# Thêm khung cho hình ảnh
image_label = tk.Label(window)
image_label.grid(row=0, column=0, rowspan=6, padx=10, pady=10, sticky="nw")  # Nằm ở góc trái màn hình

# Tải và hiển thị hình ảnh
try:
    image = ImageTk.open("example_image.png")  # Đường dẫn tới hình ảnh của bạn
    image = image.resize((100, 100), ImageTk.ANTIALIAS)  # Điều chỉnh kích thước hình ảnh
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo
except FileNotFoundError:
    image_label.config(text="Không tìm thấy ảnh")

# Tạo nhãn và ô nhập liệu cho cân nặng
label_weight = tk.Label(window, text="Nhập cân nặng (kg):")
label_weight.grid(row=0, column=1, padx=10, pady=10, sticky="w")

entry_weight = tk.Entry(window, width=30)
entry_weight.grid(row=0, column=2, padx=10, pady=10)

# Tạo nhãn và ô nhập liệu cho chiều cao
label_height = tk.Label(window, text="Nhập chiều cao (m):")
label_height.grid(row=1, column=1, padx=10, pady=10, sticky="w")
entry_height = tk.Entry(window, width=30)
entry_height.grid(row=1, column=2, padx=10, pady=10)

# Tạo nút bấm để tính BMI
button = tk.Button(window, text="Tính BMI", command=on_button_click)
button.grid(row=2, column=1, columnspan=2, pady=10)

# Tạo nhãn và Entry readonly để hiển thị kết quả BMI
label_result = tk.Label(window, text="Kết quả BMI:")
label_result.grid(row=3, column=1, padx=10, pady=10, sticky="w")

result_entry = tk.Entry(window, width=30, state="readonly")
result_entry.grid(row=3, column=2, padx=10, pady=10)

# Tạo nhãn và Entry readonly để hiển thị tình trạng BMI
label_status = tk.Label(window, text="Tình trạng BMI:")
label_status.grid(row=4, column=1, padx=10, pady=10, sticky="w")

status_entry = tk.Entry(window, width=30, state="readonly")
status_entry.grid(row=4, column=2, padx=10, pady=10)

# Thêm nhãn hiển thị thông báo lỗi
error_label = tk.Label(window, text="", fg="red")
error_label.grid(row=5, column=1, columnspan=2, pady=10)

# Liên kết phím Enter với hàm `on_button_click`
entry_weight.bind("<Return>", on_button_click)
entry_height.bind("<Return>", on_button_click)

# Chạy vòng lặp chính
window.mainloop()
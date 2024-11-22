import tkinter as tk
from tkinter import messagebox

# Hàm xác thực và hiển thị thông tin sinh viên
def validate_student_data(entry_name, entry_age, gender_var, active_var):
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    is_active = active_var.get()

    if not name or not age:
        messagebox.showerror("Lỗi", "Tên và tuổi không được để trống!")
        return

    if gender == "Chưa chọn":
        messagebox.showerror("Lỗi", "Bạn chưa chọn giới tính!")
        return

    if not is_active:
        messagebox.showerror("Lỗi", "Bạn phải chọn trạng thái hoạt động!")
        return

    messagebox.showinfo("Thông báo", f"Thông tin sinh viên: \nTên: {name}\nTuổi: {age}\nGiới tính: {gender}\nTrạng thái: {'Hoạt động' if is_active else 'Không hoạt động'}")


# Hàm xác thực và hiển thị thông tin ngành học
def validate_course_data(entry_course_name, entry_course_code):
    course_name = entry_course_name.get()
    course_code = entry_course_code.get()

    if not course_name or not course_code:
        messagebox.showerror("Lỗi", "Tên ngành học và mã ngành không được để trống!")
        return

    messagebox.showinfo("Thông báo", f"Thông tin ngành học: \nTên ngành học: {course_name}\nMã ngành học: {course_code}")


def open_student_form():
    student_window = tk.Toplevel(root)
    student_window.title("Nhập Thông Tin Sinh Viên")

    # Các label và widget nhập liệu
    label_name = tk.Label(student_window, text="Tên:")
    label_name.grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(student_window)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    label_age = tk.Label(student_window, text="Tuổi:")
    label_age.grid(row=1, column=0, padx=10, pady=10)
    entry_age = tk.Entry(student_window)
    entry_age.grid(row=1, column=1, padx=10, pady=10)

    label_gender = tk.Label(student_window, text="Giới tính:")
    label_gender.grid(row=2, column=0, padx=10, pady=10)
    gender_var = tk.StringVar(value="Chưa chọn")
    gender_male = tk.Radiobutton(student_window, text="Nam", variable=gender_var, value="Nam")
    gender_male.grid(row=2, column=1, padx=10, pady=5)
    gender_female = tk.Radiobutton(student_window, text="Nữ", variable=gender_var, value="Nữ")
    gender_female.grid(row=2, column=2, padx=10, pady=5)

    label_active = tk.Label(student_window, text="Trạng thái hoạt động:")
    label_active.grid(row=3, column=0, padx=10, pady=10)
    active_var = tk.BooleanVar()
    active_check = tk.Checkbutton(student_window, text="Đang hoạt động", variable=active_var)
    active_check.grid(row=3, column=1, padx=10, pady=10)

    # Các nút Lưu và Đóng
    save_button = tk.Button(
        student_window, 
        text="Lưu", 
        command=lambda: validate_student_data(entry_name, entry_age, gender_var, active_var)
    )
    save_button.grid(row=4, column=0, padx=10, pady=20)

    close_button = tk.Button(student_window, text="Đóng", command=student_window.destroy)
    close_button.grid(row=4, column=1, padx=10, pady=20)


# Hàm mở cửa sổ nhập thông tin ngành học
def open_course_form():
    course_window = tk.Toplevel(root)
    course_window.title("Nhập Thông Tin Ngành Học")

    # Các label và widget nhập liệu
    label_course_name = tk.Label(course_window, text="Tên ngành học:")
    label_course_name.grid(row=0, column=0, padx=10, pady=10)
    entry_course_name = tk.Entry(course_window)
    entry_course_name.grid(row=0, column=1, padx=10, pady=10)

    label_course_code = tk.Label(course_window, text="Mã ngành học:")
    label_course_code.grid(row=1, column=0, padx=10, pady=10)
    entry_course_code = tk.Entry(course_window)
    entry_course_code.grid(row=1, column=1, padx=10, pady=10)

    # Các nút Lưu và Đóng
    save_button_course = tk.Button(
        course_window, 
        text="Lưu", 
        command=lambda: validate_course_data(entry_course_name, entry_course_code)
    )
    save_button_course.grid(row=2, column=0, padx=10, pady=20)

    close_button_course = tk.Button(course_window, text="Đóng", command=course_window.destroy)
    close_button_course.grid(row=2, column=1, padx=10, pady=20)


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chọn Hình Thức Nhập Dữ Liệu")

# Nút mở cửa sổ nhập thông tin sinh viên
student_button = tk.Button(root, text="Nhập Thông Tin Sinh Viên", command=open_student_form)
student_button.grid(row=0, column=0, padx=10, pady=20)

# Nút mở cửa sổ nhập ngành học
course_button = tk.Button(root, text="Nhập Thông Tin Ngành Học", command=open_course_form)
course_button.grid(row=0, column=1, padx=10, pady=20)

# Căn giữa hai nút
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Chạy chương trình
root.mainloop()

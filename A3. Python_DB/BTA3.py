import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import re

# Tạo cơ sở dữ liệu và bảng
def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Nganh (
            ma_nganh TEXT PRIMARY KEY,
            ten_nganh TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SV (
            MSSV TEXT PRIMARY KEY,
            hoten TEXT NOT NULL,
            ma_nganh TEXT NOT NULL,
            sodt TEXT,
            email TEXT,
            FOREIGN KEY (ma_nganh) REFERENCES Nganh(ma_nganh)
        )
    ''')
    conn.commit()
    conn.close()

create_database()

# Hàm kiểm tra email hợp lệ
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Hàm kiểm tra số điện thoại hợp lệ
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10

# Hàm thêm sinh viên
def add_student():
    mssv = entry_mssv.get().strip()
    hoten = entry_hoten.get().strip()
    ma_nganh = combobox_nganh.get()
    sodt = entry_sdt.get().strip()
    email = entry_email.get().strip()

    if not mssv or not hoten or ma_nganh == "Chọn Ngành Học":
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    if not is_valid_phone(sodt):
        messagebox.showerror("Lỗi", "Số điện thoại không hợp lệ!")
        return

    if not is_valid_email(email):
        messagebox.showerror("Lỗi", "Email không hợp lệ!")
        return

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO SV (MSSV, hoten, ma_nganh, sodt, email) VALUES (?, ?, ?, ?, ?)',
                       (mssv, hoten, ma_nganh, sodt, email))
        conn.commit()
        messagebox.showinfo("Thông báo", "Thêm sinh viên thành công!")
        update_student_list()  # Refresh the student list
    except sqlite3.IntegrityError:
        messagebox.showerror("Lỗi", "MSSV đã tồn tại!")
    finally:
        conn.close()

# Hàm thêm ngành
def add_major():
    ma_nganh = entry_ma_nganh.get().strip()
    ten_nganh = entry_ten_nganh.get().strip()

    if not ma_nganh or not ten_nganh:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Nganh (ma_nganh, ten_nganh) VALUES (?, ?)', (ma_nganh, ten_nganh))
        conn.commit()
        messagebox.showinfo("Thông báo", "Thêm ngành học thành công!")
        update_course_list()  # Refresh the course list
    except sqlite3.IntegrityError:
        messagebox.showerror("Lỗi", "Mã ngành hoặc tên ngành đã tồn tại!")
    finally:
        conn.close()

# Hàm lấy danh sách sinh viên
def fetch_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM SV')
    students = cursor.fetchall()
    conn.close()
    return students

# Hàm lấy danh sách ngành
def fetch_courses():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Nganh')
    courses = cursor.fetchall()
    conn.close()
    return courses

# Cập nhật danh sách sinh viên
def update_student_list():
    for row in tree_students.get_children ():
        tree_students.delete(row)
    for student in fetch_students():
        tree_students.insert("", "end", values=student)

# Cập nhật danh sách ngành
def update_course_list():
    for row in tree_courses.get_children():
        tree_courses.delete(row)
    for course in fetch_courses():
        tree_courses.insert("", "end", values=course)

# Cập nhật danh sách ngành học
def update_major_list():
    return [course[0] for course in fetch_courses()]

# Giao diện chính
root = tk.Tk()
root.title("Quản Lý Sinh Viên và Ngành Học")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tab Sinh Viên
student_tab = ttk.Frame(notebook)
notebook.add(student_tab, text="Thông Tin Sinh Viên")

# Treeview cho Sinh Viên
tree_students = ttk.Treeview(student_tab, columns=("MSSV", "Họ và Tên", "Mã Ngành", "Số Điện Thoại", "Email"), show='headings')
tree_students.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
tree_students.heading("MSSV", text="MSSV")
tree_students.heading("Họ và Tên", text="Họ và Tên")
tree_students.heading("Mã Ngành", text="Mã Ngành")
tree_students.heading("Số Điện Thoại", text="Số Điện Thoại")
tree_students.heading("Email", text="Email")

# Định cấu hình lưới
student_tab.grid_rowconfigure(0, weight=1)
student_tab.grid_columnconfigure(1, weight=1)

# MSSV
label_mssv = tk.Label(student_tab, text="MSSV:* ")
label_mssv.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_mssv = tk.Entry(student_tab, width=33)
entry_mssv.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Họ tên
label_hoten = tk.Label(student_tab, text="Họ và Tên:* ")
label_hoten.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_hoten = tk.Entry(student_tab, width=33)
entry_hoten.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Ngành
label_nganh = tk.Label(student_tab, text="Mã ngành:* ")
label_nganh.grid(row=3, column=0, padx=10, pady=5, sticky="w")
combobox_nganh = ttk.Combobox(student_tab, values=update_major_list(), state="readonly", width=30)
combobox_nganh.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
combobox_nganh.set("Chọn Ngành Học")

# Số điện thoại
label_sdt = tk.Label(student_tab, text="Số điện thoại:* ")
label_sdt.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_sdt = tk.Entry(student_tab, width=33)
entry_sdt.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Email
label_email = tk.Label(student_tab, text="Email:* ")
label_email.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(student_tab, width=33)
entry_email.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

# Nút thêm sinh viên
add_student_button = tk.Button(student_tab, text="Thêm Sinh Viên", command=add_student, fg="white", bg="green")
add_student_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="e")

# Tab Ngành Học
major_tab = ttk.Frame(notebook)
notebook.add(major_tab, text="Thông Tin Ngành Học")

# Treeview cho Ngành Học
tree_courses = ttk.Treeview(major_tab, columns=("Mã Ngành", "Tên Ngành"), show='headings')
tree_courses.heading("Mã Ngành", text="Mã Ngành")
tree_courses.heading("Tên Ngành", text="Tên Ngành")
tree_courses.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Cấu hình lưới
major_tab.grid_rowconfigure(0, weight=1)  # Đảm bảo Treeview co giãn
major_tab.grid_columnconfigure(1, weight=1)

# Mã ngành học
label_ma_nganh = tk.Label(major_tab, text="Mã ngành học:* ")
label_ma_nganh.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_ma_nganh = tk.Entry(major_tab, width=30)
entry_ma_nganh.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Tên ngành học
label_ten_nganh = tk.Label(major_tab, text="Tên ngành học:* ")
label_ten_nganh.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_ten_nganh = tk.Entry(major_tab, width=30)
entry_ten_nganh.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Nút thêm ngành
add_major_button = tk.Button(major_tab, text="Thêm Ngành Học", command=add_major, fg="white", bg="green")
add_major_button.grid(row=3, column=1, padx=10, pady=20, sticky="e")

# Cập nhật danh sách khi khởi động
update_student_list()
update_course_list()

# Chạy ứng dụng
root.mainloop()
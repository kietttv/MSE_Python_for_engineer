import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def validate_on_focus_out(event):
    name = entry_name.get().strip()
    error_label_name.config(text="Họ và Tên không được để trống!" if not name else "")

    age = entry_age.get().strip()
    if not age:
        error_msg_age.config(text="Tuổi không được để trống")
    else:
        if age.isdigit() and int(age) > 0:
            error_msg_age.config(text="")
        elif not age.isdigit():
            error_msg_age.config(text="Tuổi không hợp lệ!")
        else:
            error_msg_age.config(text="Tuổi phải lớn hơn 0!")

    major = combobox_major.get()
    error_msg_major.config(text="Ngành học không được để trống!" if major == "Chọn Ngành Học" else "")

def validate_student_data():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    gender = gender_var.get()
    major = combobox_major.get()
    note = text_note.get("1.0", "50.0")

    errors = []

    if not name:
        errors.append("Tên không được để trống!")

    if not age:
        errors.append("Tuổi không được để trống!")
    else:
        try:
            age = int(age)
            if age <= 0:
                errors.append("Tuổi phải lớn hơn 0!")
        except ValueError:
            errors.append("Tuổi phải là số hợp lệ!")

    if major == "Chọn Ngành Học":
        errors.append("Ngành học không được để trống!")  

    if not gender:
        errors.append("Bạn chưa chọn giới tính!")   

    if errors:
        messagebox.showerror("Lỗi", "\n".join(errors))
        return

    messagebox.showinfo(
        "Thông báo",
        f"Thông tin sinh viên: \nTên: {name}\nTuổi: {age}\nNgành học: {major}\nGiới tính: {gender}\nGhi chú: {note}"
    )

def confirm_and_quit():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    major = combobox_major.get().strip()
    note = text_note.get("1.0", "50.0").strip()

    if name or age or major != major_default or note:
        response = messagebox.askokcancel(
            "Cảnh báo!!!",
            "Các thông tin bạn đã nhập sẽ không được lưu!\nBạn có chắc chắn muốn đóng?"
        )
        if response:
            root.quit()
    else:
        root.quit()

def get_level_data():
    level_data_arr = []

    add_to_level_data = lambda check_var, level_name: level_data_arr.append(level_name) if check_var.get() else None

    add_to_level_data(level_var_cd, "Cao Đẳng")
    add_to_level_data(level_var_dh, "Đại Học")
    add_to_level_data(level_var_ths, "Thạc Sĩ")
    add_to_level_data(level_var_ts, "Tiến Sĩ")

    return level_data_arr

def validate_course_on_focus_out(event):
    course_code = entry_course_code.get().strip()
    error_label_course_code.config(text="Mã ngành học không được để trống!" if not course_code else "")

    course_name = entry_course_name.get().strip()
    error_label_course_name.config(text="Tên ngành học không được để trống!" if not course_name else "")

    level_data = get_level_data()
    if not level_data:
        error_label_level.config(text="Bật đào tạo không được để trống!")
    else:
        error_label_level.config(text="")


def validate_course_data():
    course_name = entry_course_name.get()
    course_code = entry_course_code.get()
    level_data = get_level_data()

    if not course_code:
        messagebox.showerror("Lỗi", "Mã ngành không được để trống!")
        return
    
    if not course_name:
        messagebox.showerror("Lỗi", "Tên ngành học không được để trống!")
        return

    if len(level_data) == 0:
        messagebox.showerror("Lỗi", "Bật đào tạo không được để trống!")
        return

    arr_major.append(course_code + " - " + course_name)

    combobox_major['value'] = arr_major

    messagebox.showinfo("Thông báo", f"Thông tin ngành học: \nMã ngành học: {course_code}\nTên ngành học: {course_name}\nBật đào tạo: {', '.join(level_data)}")

# khởi tạo
root = tk.Tk()
root.title("Nhập Dữ Liệu Sinh Viên và Ngành Học")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# <----------- start tab sinh viên ----------->
student_tab = ttk.Frame(notebook)
notebook.add(student_tab, text="Thông Tin Sinh Viên")

# tên
label_name = tk.Label(student_tab, text="Họ và Tên:* ")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = tk.Entry(student_tab, width=33)
entry_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")
error_label_name = tk.Label(student_tab, text="", fg="red")
error_label_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_name.bind("<FocusOut>", validate_on_focus_out)

# tuổi
label_age = tk.Label(student_tab, text="Tuổi:* ")
label_age.grid(row=0, column=2, padx=10, pady=10, sticky="w")
entry_age = tk.Entry(student_tab, width=25)
entry_age.grid(row=0, column=3, padx=10, pady=10, sticky="w")
error_msg_age = tk.Label(student_tab, text="", fg="red")
error_msg_age.grid(row=1, column=3, padx=10, pady=5, sticky="w")
entry_age.bind("<FocusOut>", validate_on_focus_out)

# ngành
label_major = tk.Label(student_tab, text="Mã ngành:* ")
label_major.grid(row=2, column=0, padx=10, pady=10, sticky="w")
arr_major = ["CNTT - Công Nghệ Thông Tin", "QTKD - Quản Trị Kinh Doanh", "TKDH - Thiết Kế Đồ Họa"]
combobox_major = ttk.Combobox(student_tab, values=arr_major, state="readonly", width=30)
combobox_major.grid(row=2, column=1, padx=10, pady=10, sticky="w")
major_default = "Chọn Ngành Học"
combobox_major.set(major_default)
error_msg_major = tk.Label(student_tab, text="", fg="red")
error_msg_major.grid(row=3, column=1, padx=10, pady=5, sticky="w")
combobox_major.bind("<FocusOut>", validate_on_focus_out)

# giới tính
label_gender = tk.Label(student_tab, text="Giới tính:* ")
label_gender.grid(row=4, column=0, padx=10, pady=10, sticky="w")
gender_var = tk.StringVar(value="Nam")
gender_male = tk.Radiobutton(student_tab, text="Nam", variable=gender_var, value="Nam")
gender_male.grid(row=4, column=1, padx=10, pady=5, sticky="w")
gender_female = tk.Radiobutton(student_tab, text="Nữ", variable=gender_var, value="Nữ")
gender_female.grid(row=4, column=2, padx=10, pady=5, sticky="w")
gender_female.bind("<FocusOut>", validate_on_focus_out)
gender_male.bind("<FocusOut>", validate_on_focus_out)

# ghi chú
label_note = tk.Label(student_tab, text="Ghi chú:")
label_note.grid(row=5, column=0, padx=10, pady=10, sticky="nw")
text_note = tk.Text(student_tab, width=50, height=5, wrap="word")
text_note.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky="w")
text_note.bind("<FocusOut>", validate_on_focus_out)

# nút lưu
save_button = tk.Button(student_tab, text="Lưu", command=validate_student_data, fg="white", bg="green")
save_button.grid(row=6, column=2, padx=10, pady=20, sticky="e")

# nút đóng
close_button = tk.Button(student_tab, text="Đóng", command=confirm_and_quit, fg="white", bg="red")
close_button.grid(row=6, column=3, padx=10, pady=20, sticky="w")
# <----------- end tab sinh viên ----------->

# <----------- start tab ngành học -----------> 
course_tab = ttk.Frame(notebook) 
notebook.add(course_tab, text="Thông Tin Ngành Học")

# mã ngành học 
label_course_code = tk.Label(course_tab, text="Mã ngành học:*") 
label_course_code.grid(row=0, column=0, padx=10, pady=10) 
entry_course_code = tk.Entry(course_tab) 
entry_course_code.grid(row=0, column=1, padx=10, pady=10)
error_label_course_code = tk.Label(course_tab, text="", fg="red")
error_label_course_code.grid(row=0, column=2, padx=10, pady=10)
entry_course_code.bind("<FocusOut>", validate_course_on_focus_out)

# tên ngành học 
label_course_name = tk.Label(course_tab, text="Tên ngành học:*")  
label_course_name.grid(row=1, column=0, padx=10, pady=10) 
entry_course_name = tk.Entry(course_tab) 
entry_course_name.grid(row=1, column=1, padx=10, pady=10)
error_label_course_name = tk.Label(course_tab, text="", fg="red")
error_label_course_name.grid(row=1, column=2, padx=10, pady=10)
entry_course_name.bind("<FocusOut>", validate_course_on_focus_out)

# bật đào tạo 
label_level = tk.Label(course_tab, text="Bật đào tạo:*") 
label_level.grid(row=2, column=0, padx=10, pady=10)

#checkbox
level_var_cd = tk.BooleanVar()
level_var_cd.set(True)
level_check_cd = tk.Checkbutton(course_tab, text="Cao Đẳng", variable=level_var_cd)
level_check_cd.grid(row=2, column=1, padx=10, pady=10)
level_check_cd.bind("<FocusOut>", validate_course_on_focus_out)

# checkbox
level_var_dh = tk.BooleanVar()
level_check_dh = tk.Checkbutton(course_tab, text="Đại Học", variable=level_var_dh)
level_check_dh.grid(row=2, column=2, padx=10, pady=10)
level_check_dh.bind("<FocusOut>", validate_course_on_focus_out)

# checkbox
level_var_ths = tk.BooleanVar()
level_check_ths = tk.Checkbutton(course_tab, text="Thạc Sĩ", variable=level_var_ths)
level_check_ths.grid(row=2, column=3, padx=10, pady=10)
level_check_ths.bind("<FocusOut>", validate_course_on_focus_out)

# checkbox
level_var_ts = tk.BooleanVar()
level_check_ts = tk.Checkbutton(course_tab, text="Tiến Sĩ", variable=level_var_ts)
level_check_ts.grid(row=2, column=4, padx=10, pady=10)
level_check_ts.bind("<FocusOut>", validate_course_on_focus_out)

# error msg
error_label_level = tk.Label(course_tab, text="", fg="red")
error_label_level.grid(row=3, column=2, padx=10, pady=10)

# nut luu
save_button_course = tk.Button(course_tab, text="Lưu", command=validate_course_data, fg="white", bg="green")
save_button_course.grid(row=6, column=2, padx=10, pady=20, sticky="e")

# nut dong
close_button_course = tk.Button(course_tab, text="Đóng", command=root.quit, fg="white", bg="red")
close_button_course.grid(row=6, column=3, padx=10, pady=20, sticky="w")
# <----------- end tab ngành học -----------> 

# loop
root.mainloop()
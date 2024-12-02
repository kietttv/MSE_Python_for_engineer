import sqlite3
from sqlite3 import Error
from sqlite3 import Cursor

# Tạo hoặc kết nối đến cơ sở dữ liệu
con = sqlite3.connect('A3. Python_DB\\db\\test_crud.sqlite')
cur = con.cursor()

# Tạo bảng 'users'
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
con.commit()

print("Bảng 'users' đã được tạo!")

# Chức năng CRUD
def create_user(name, email, age):
    try:
        cur.execute('''
        INSERT INTO users (name, email, age)
        VALUES (?, ?, ?)
        ''', (name, email, age))
        con.commit()
        print(f"Đã thêm user: {name}")
    except sqlite3.IntegrityError:
        print("Email đã tồn tại!")

def read_users():
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    print("Danh sách người dùng:")
    for row in rows:
        print(row)

def update_user(user_id, name=None, email=None, age=None):
    fields = []
    params = []
    if name:
        fields.append("name = ?")
        params.append(name)
    if email:
        fields.append("email = ?")
        params.append(email)
    if age:
        fields.append("age = ?")
        params.append(age)
    params.append(user_id)
    
    query = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
    cur.execute(query, params)
    con.commit()
    print(f"Đã cập nhật user ID: {user_id}")

def delete_user(user_id):
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    con.commit()
    print(f"Đã xóa user ID: {user_id}")

# Thêm dữ liệu (Create)
create_user("Alice", "alice@example.com", 25)
create_user("Bob", "bob@example.com", 30)
create_user("Charlie", "charlie@example.com", 22)

# Đọc dữ liệu (Read)
read_users()
# Cập nhật dữ liệu (Update)
#update_user(1, name="Alice Smith", age=26)

# Đọc lại dữ liệu để kiểm tra cập nhật
#read_users()

# Xóa dữ liệu (Delete)
#delete_user(2)

# Đọc lại dữ liệu để kiểm tra xóa
#read_users()

# Đóng kết nối
#con.close()
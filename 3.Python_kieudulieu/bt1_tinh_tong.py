# BT1, 2
def sum(lst):
    s = 0
    for n in lst:
        s +=n
    return s    

def min_max_avg(lst):
    avg = sum(lst)/len(lst)
    return min(lst), max(lst), avg

a = [1,2,3,4,5,6,7,8,9]

print("Sum :", sum(a))

print(min_max_avg(a))


# BT 3
def sortLst(lst):
    lst.sort()
    print("Sorted: ", lst)

def sinhVienHoNguyen(lst):
    result = []
    for x in lst:
        if"Nguyen" in x:
            result.append(x)
    return result        

sinhVien = ["Truong Van Tuan Kiet", "Nguyen Nhat Chinh", "Luu Pham Anh Kiet", "Le Thanh Nhan", "Nguyen Van A", "Nguyen Van B"]

sortLst(sinhVien)

print(sinhVienHoNguyen(sinhVien))


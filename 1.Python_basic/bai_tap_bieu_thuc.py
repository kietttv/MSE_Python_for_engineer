# Viết chương trình cho phép nhập x, n và xuất ra kết quả của biểu thức:
# S(x, n) = x + (x^2/2!) + (x^3 + 3!) + ... + (x^n/n!)

import math

print("===== Bai toan bieu thuc =====")

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

s = 0

for i in range(x, n):
    if(i == 1):
        s = x
    else:
        s += math.pow(x, i) / math.factorial(i)

print("Ket Qua: ", s)
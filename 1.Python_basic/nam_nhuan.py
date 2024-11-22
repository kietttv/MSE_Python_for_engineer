print("===== Nam Nhuan =====")

n = int(input("Nhap nam: "))

if((n%4 == 0 and n%100 != 0) or n % 400 == 0):
    print("True")
else:
    print("False")

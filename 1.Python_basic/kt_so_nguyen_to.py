n = int(input("Nhap n: "))

print("===== Kiem tra so nguyen to =====")

if(n >= 2):
    flag = True
    for i in range(2, int(n ** 0.5) + 1 ):
        if (n % i == 0):
            flag = False
            break
    if(flag):
        print("True")
    else:
        print("False")    
else:
    print("False")
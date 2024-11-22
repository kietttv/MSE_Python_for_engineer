# ham k dung de qui
def tinhGiaiThua(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result  

# ham dung de qui
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)

# tinh to hop
def  tinhToHop(n, k):
    return tinhGiaiThua(n) / (tinhGiaiThua(n-k) * tinhGiaiThua(k))

# tinh to hop dung de qui 
def toHop(n, k):
    return giaiThua(n) / (giaiThua(n-k) * giaiThua(k))

n = int(input("Nhap n: "))
k = int(input("Nhap k: "))

if(n > 0):
    if(k>=0 and k<=n):
        print("C = ", round(tinhToHop(n, k), 2))
        print("(Sd de qui) C = ", round(toHop(n, k), 2))
    else:
        print("K nen la: k>=0 and k<=n") 
else:
    print("n khong nen nho hon 0")
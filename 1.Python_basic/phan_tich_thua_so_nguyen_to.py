print("===== Phan tich thua so nguyen to cua 1 so n =====")

n = int(input("Nhap n: "))

list = []  
dict = {}
    
divisor = 2
while n > 1:
    while n % divisor == 0: # chia lay du
        list.append(divisor)
        dict[divisor] = dict.get(divisor, 0) + 1
        n //= divisor #chia lay nguyen 
    divisor += 1
    
print("List:", list)
print("Dict:", dict)
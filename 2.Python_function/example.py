# tham so tuy y
def sum(*n):
    s = 0
    for i in n:
        s+=i

    return s

print(sum(1, 2, 3, 4))

def thamSoVsKhoa(a, b, c):
    print("A: ", a)
    print("B: ", b)
    print("C: ", c)

thamSoVsKhoa(c = "Teo", b = "Ti", a = "kiet")

x = lambda a: a**3
print(x(5))

y = lambda a, b, c: a + b + c
print(y(10, 12, 20))

lst = [3, 5, 8, 10, 13, 15, 16]
new_lst = list(filter(lambda a: a % 2 == 0, lst))
print(new_lst)
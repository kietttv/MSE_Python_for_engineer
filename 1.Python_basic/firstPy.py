import math

print("Hello! chao bạn")
print("Chào thế giới")
a=1
print(type(a))

a, b, c = 3, 4, 5

print(a, b, c)

myString = "Kiet dep trai"

print(myString)

d = 3

e = 3.0

print(type(d))

print(type(e))

print(d == e)

print(a + b + c)

print(a * c)

print(c/a)

myString += " python"

print(myString)

print(myString * 3)

age = int(input("Nhap age: "))

if(age > 0):
    if(age < 18):
        print(age, "Em chua 18")
    if(age >= 18):
        print( age, "Em 18+")
else:
    print("sai")      

n = int(input("Nhap 1 so: "))
if(n > 0):
    print("So duong")
    if(n%2 == 0):
        print("Chan")
    else:
        print("Le")
elif(n < 0):
    print("So am")         
else:
    print("Zero")       

s = 0
for i in range(1, 100):
  s+=i  

print(s)


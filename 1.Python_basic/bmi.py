print("======BMI Program======")

w = float(input("Nhap can nang (kg): "))
h = float(input("Nhap chieu cao (m): "))

bmi = w / (h*h)

if(bmi > 1 and bmi < 18.5):
    print("Gay")
if(bmi >= 18.5 and bmi <= 24.9):
    print("Binh Thuong")
elif(bmi >= 25 and bmi <= 29.9):
    print("Hoi Beo")
elif(bmi >= 30.0 and bmi <= 34.9):
    print("Beo Phi Cap Do 1")
elif(bmi >= 35.0 and bmi <= 39.9):
    print("Hoi Beo")
elif(bmi > 40):
    print ("Beo Phi Cap Do 4")  
else:
    print("ERROR")    
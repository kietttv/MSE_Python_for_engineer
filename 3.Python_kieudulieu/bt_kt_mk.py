import re

def ktmk(str):
    if(len(str) >= 8):
        if not(re.findall("[a-z]", str)):
            print("Mk phai co 1 ki tu thuong")
        elif not(re.findall("[a-zA-Z]", str)):
            print("Mk phai co 1 ki tu in hoa")
        elif not(re.findall("[0-9]", str)):
            print("Mk phai co 0-9")
        elif not(re.findall("[@#$]", str)):
            print("Mk phai co ki tu dat biet") 
        else:
            print("Mk manh")    
    else:
        print("Qua ngan")        

# main  

print("===== Kiem Tra Mat Khau =====")

ktmk(input("Nhap mk:"))
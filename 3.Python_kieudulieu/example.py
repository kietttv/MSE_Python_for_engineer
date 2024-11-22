chuoiNgan = 'Kiet'

chuoiDai = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Nisl tincidunt eget nullam non. Quis hendrerit dolor magna eget est lorem ipsum dolor sit'''

print(chuoiDai)

# for i in chuoiNgan:
#     print(i)

for i in range(-1, -len(chuoiNgan)-1, -1):
    print(chuoiNgan[i])    

srt = "   Lorem ipsum dolor sit amet   "

print(srt.strip())
print(srt.split())


set = {"a", "b", 2} # set - set k trÙng

list = [1, 2, 3, "abc", True ] # list

tuple = ("1.2", 1.2, 3) # tuple

car = {
    "Car 1": {
        "Name: " : "car 1",
        "Brand: " : "A"
    },
    "Car 2": {
        "Name: " : "car 2",
        "Brand: " : "B"
    },
    "Car 3": {
        "Name: " : "car 3",
        "Brand: " : "A"
    },
}

print(car)
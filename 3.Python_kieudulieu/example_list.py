a = [1,2,3,4,5,6,7,8,"9"]

print(type(a))
print(len(a))

# for x in a:
#     print(x)

print(a[2:5])

print(a[2:6:2])

# su dung de revert list cung ok
print(a[::-1])

for x in a[::-1]:
    print(x)

b = ["abcb", "hgfhah", "dhfg", "123", "@#$$"]

print(b.sort())
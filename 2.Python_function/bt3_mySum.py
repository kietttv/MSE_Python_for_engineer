def mySum(*args):
    s = 0
    for x in args:
        s = s + x
    return s

print(mySum(1,2,3,4,5,6,7,8,9))
print(mySum(-1,2,-3,4,-5,6,-7,8,-9))    
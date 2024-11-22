def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 1
while (n >= 0):
    n = int(input("Tinh so fibo thu? (am ngung): "))
    
    if(n >= 0):
        print(f'so fibo {n} la {fibonacci(n)}')

print("end")        

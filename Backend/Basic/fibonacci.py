"""def fibonacci(y):
    c = 0
    f = 1
    fibo = 0
    print(c)
    print(f)
    while fibo <= y:
        fibo = f + c
        print(fibo)
        c = f
        f = fibo
fibonacci(590)"""

def fib(n):    # escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b
    print()
fib(599)
        
        

    
    
def fib(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


print(fib(1))
print(fib(3))
print(fib(5))
print(fib(20))
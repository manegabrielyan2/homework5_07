#Fibonacci recursive
def fibonacci(n : int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
f = fibonacci(4)
print(f)

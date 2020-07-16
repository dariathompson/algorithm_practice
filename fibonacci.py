def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1, 33):
    print(fibonacci(n))
    
if __name__ == "__main__":
    assert(fibonacci(7) == 13)    
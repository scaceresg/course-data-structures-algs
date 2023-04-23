def fib_efficient(n):
    
    fib = [None] * (n + 1)
    
    fib[0] = 0
    if n > 0:
        fib[1] = 1
    if n > 1:
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]
    
    return fib[-1]

if __name__ == '__main__':
    n = int(input())
    print(fib_efficient(n))
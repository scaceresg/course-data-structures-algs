def fib_efficient(n):
    # Create an array of length n
    fib = [None] * (n + 1)
    
    # Include 0 and 1
    if n > 1:
        fib[0] = 0
        fib[1] = 1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    # For each position, sum the previous two positions
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[-1]

if __name__ == '__main__':
    input_n = int(input())
    print(fib_efficient(input_n))
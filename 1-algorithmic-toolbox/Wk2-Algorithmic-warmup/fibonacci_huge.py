def fib_huge(n, m):
    
    seen = {0: 0, 1: 1}

    for i in range(2, n + 1):
        seen[i] = seen[i - 1] + seen[i - 2]
    
    return seen[n] % m

if __name__ == '__main__':
    input_n = input()
    n, m = map(int, input_n.split())
    print(fib_huge(n, m))
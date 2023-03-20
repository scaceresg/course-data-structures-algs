def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

if __name__ == '__main__':
    input_n = int(input())
    print(fib_recursive(input_n))


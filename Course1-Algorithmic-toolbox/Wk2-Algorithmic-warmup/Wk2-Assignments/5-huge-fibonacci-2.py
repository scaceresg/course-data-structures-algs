def huge_fib_number(n, m):

  if n <= 1:
    return n

  prev, curr = 0, 1

  for i in range(n-1):
    prev, curr = curr, ((prev + curr) % m)

  return curr


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(huge_fib_number(n, m))
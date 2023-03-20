def get_fib_last_digit(n):

  if n <= 1:
    return n
  
  # modules:
  prev, curr = 0, 1

  for i in range(n-1):
    prev, curr = curr, ((prev + curr) % 10)

  return curr

if __name__ == '__main__':
    n = int(input())
    print(get_fib_last_digit(n))
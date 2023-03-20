# Defining a naive algorithm for GCD
def naive_gcd(a, b):
    best = 0
    for d in range(1, a + b):
        if a % d == 0 and b % d == 0:
            best = d
    
    return best

if __name__ == '__main__':
    a = int(input('Please, choose the first number: '))
    b = int(input('Please, choose the second number: '))

    print("GCD for {} and {} is: ".format(a, b), naive_gcd(a, b))

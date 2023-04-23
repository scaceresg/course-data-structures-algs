def gcd_efficient(a, b):

    if b == 0:
        return a
    
    a_prime = a % b

    return gcd_efficient(b, a_prime)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd_efficient(a, b))
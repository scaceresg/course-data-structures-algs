# Defining an efficient algorithm for GCD using Euclidean algorithm
def euclid_gcd(a, b):

    if b == 0:
        return a
    a_prime = a % b
    return euclid_gcd(b, a_prime)

if __name__ == '__main__':
    numbers = input()
    nums = numbers.split()
    a = int(nums[0])
    b = int(nums[1])
print(euclid_gcd(a, b))
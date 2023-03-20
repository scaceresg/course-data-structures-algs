import random

# Naive algorithm
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

# Fast algorithm
def max_pairwise_product_fast(numbers):
    n = len(numbers)

    max_index1 = -1
    for index1 in range(n):
        if max_index1 == -1 or numbers[index1] > numbers[max_index1]:
            max_index1 = index1
    
    max_index2 = -1
    for index2 in range(n):
        if (numbers[index2] != numbers[max_index1]) and \
        ((max_index2 == -1) or (numbers[index2] > numbers[max_index2])):
            max_index2 = index2
    
    return numbers[max_index1] * numbers[max_index2]

# Fast algorithm debugged
def max_pairwise_product_fast_debugged(numbers):
    n = len(numbers)

    max_index1 = -1
    for index1 in range(n):
        if max_index1 == -1 or numbers[index1] > numbers[max_index1]:
            max_index1 = index1
    
    max_index2 = -1
    for index2 in range(n):
        if (index2 != max_index1) and ((max_index2 == -1) or (numbers[index2] > numbers[max_index2])):
            max_index2 = index2
    
    # print(max_index1, max_index2)
    return numbers[max_index1] * numbers[max_index2]

# Stress testing
if __name__ == '__main__':
    # tests = 0
    # while tests < 100000:
    while True:
        n = random.randint(2, 1000)
        print("n = ", n, '\n')
        a = []
        for i in range(n):
            a.append(random.randint(1, 100000))
        for i in range(n):
            print(a[i], ' ')
        print('\n')

        res1 = max_pairwise_product(a)
        res2 = max_pairwise_product_fast_debugged(a)

        if res1 != res2:
            print("Wrong answer: ", res1, ' ', res2, '\n')
            break
        else:
            print("OK\n")
        # tests += 1

# Wrong answer: n=6, [2, 4, 10, 4, 8, 10]
# Wrong answer - Coursera video: n=5, [2, 9, 3, 1, 9]

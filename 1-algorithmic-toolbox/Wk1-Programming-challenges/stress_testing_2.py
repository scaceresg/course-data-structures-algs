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

# Checking wrong tests in Coursera video
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print("res1 = ", max_pairwise_product(input_numbers))
    print("res2 = ", max_pairwise_product_fast(input_numbers))
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
    
    print(max_index1, max_index2)
    return numbers[max_index1] * numbers[max_index2]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))

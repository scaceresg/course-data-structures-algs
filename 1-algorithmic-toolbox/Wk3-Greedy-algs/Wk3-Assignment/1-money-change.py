import math

def get_change(m):
    return math.floor(m/10) + math.floor((m % 10)/5) + (m % 5)

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
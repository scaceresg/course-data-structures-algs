def get_optimal_loot(W, weights, values):
    amounts = [0] * n
    total_val = 0
    n_iter = 0
    while n_iter < len(weights):
        if W == 0:
            return total_val
        i = get_best_item(weights, values)
        a = min(weights[i], W)
        total_val += a * (values[i]/weights[i])
        weights[i] -= a
        amounts[i] += a
        W -= a
        n_iter += 1
    return total_val

def get_best_item(weights, values):
    max_val_per_w = 0
    best_item = 0
    for i in range(len(weights)):
        if weights[i] > 0:
            if values[i]/weights[i] > max_val_per_w:
                max_val_per_w = values[i]/weights[i]
                best_item = i
    return best_item

if __name__ == '__main__':
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_loot = get_optimal_loot(capacity, weights, values)
    print(f'{opt_loot:.10f}')
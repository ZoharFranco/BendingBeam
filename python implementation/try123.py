value_idx = 0
capacity_idx = 1


def knapsck(capacity, items):
    m = [[0] * (capacity+1) for i in range(len(items))]
    m[0] = [float(0)] + [float('-inf') for c in range(capacity + 1)]

    for i in range(len(items)):
        for k in range(capacity+1):
            if k-items[i][capacity_idx] >= 0:
                m[i][k] = max(m[i-1][k], m[i-1][k-items[i][capacity_idx]] + items[i][value_idx])
            else:
                m[i][k] = m[i-1][k]
    return max([item for sublist in m for item in sublist])


print(knapsck(10, [(8, 2), (2, 1), (3, 1), (7, 2), (123, 3), (19, 8)]))

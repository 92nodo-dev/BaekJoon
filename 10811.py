def reverse_baskets(N, M, orders):
    baskets = list(range(1, N + 1))

    for order in orders:
        i, j = order
        baskets[i - 1:j] = reversed(baskets[i - 1:j])

    return baskets

N, M = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(M)]

result = reverse_baskets(N, M, orders)
print(*result)

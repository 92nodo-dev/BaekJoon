import sys
input = sys.stdin.readline

N = int(input())
max_x = -100000
max_y = -100000
min_x = 100000
min_y = 100000

for _ in range(N):
    x, y = map(int, input().split())

    max_x = max(max_x, x)
    min_x = min(min_x, x)
    max_y = max(max_y, y)
    min_y = min(min_y, y)

print(abs(max_x-min_x) * abs(max_y-min_y))

import sys

n, m = map(int, sys.stdin.readline().strip().split())
block = list(map(int, sys.stdin.readline().strip().split()))
prefix_sum = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    prefix_sum[a - 1] += c
    prefix_sum[b] -= c

for i in range(1, n + 1):
    prefix_sum[i] += prefix_sum[i - 1]

for i in range(n):
    block[i] += prefix_sum[i]
print(*block)

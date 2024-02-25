import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().strip().split())

dp = defaultdict(int)
dp[0] = 0

for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split())
    keys = list(dp.keys())
    for i in keys:
        dp[i + b] = max(dp[i + b], dp[i] + a)

answer2 = 0

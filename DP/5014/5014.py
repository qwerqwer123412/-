import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().strip().split())

q = deque()
dp = [int(1e9)] * (F + 1)
dp[S] = 0
q.append((S, 0))

while q:
    x, cost = q.popleft()
    up = x + U
    if 0 < up <= F and dp[up] > cost + 1:
        dp[up] = cost + 1
        q.append((up, cost + 1))
    down = x - D
    if 0 < down <= F and dp[down] > cost + 1:
        dp[down] = cost + 1
        q.append((down, cost + 1))
print(dp[G]) if dp[G] != int(1e9) else print("use the stairs")

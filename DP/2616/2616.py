import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().strip().split()))
couch_count = int(sys.stdin.readline().strip())

dp = [[0] * n for _ in range(4)]

for i in range(couch_count):
    dp[1][i] = dp[1][i-1] + data[i]
    dp[2][i] = dp[2][i-1] + data[i]
    dp[3][i] = dp[3][i-1] + data[i]
for i in range(1, 4):
    for j in range(couch_count,n):
        dp[i][j] = max(dp[i][j-1], (dp[i-1][j - couch_count] +  sum(data[j - couch_count + 1:j + 1])))
print(dp[-1][-1])
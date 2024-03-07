import sys

c = int(sys.stdin.readline().strip())

for _ in range(c):
    d, n = map(int, sys.stdin.readline().strip().split())
    data = list(map(lambda x: int(x) % d, sys.stdin.readline().strip().split()))
    visited = [0] * d
    answer = 0
    s = 0
    for i in data:
        s = (s + i) % d
        visited[s] += 1
        if s == 0:
            answer += 1
    for i in range(d):
        answer += (visited[i] * (visited[i] - 1)) // 2
    print(answer)

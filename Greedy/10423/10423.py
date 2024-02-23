import sys
from collections import defaultdict
import heapq

n, m, k = map(int, sys.stdin.readline().strip().split())
graph = defaultdict(list)
plant = map(int, sys.stdin.readline().strip().split())
pq = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
visited = [False] * (n + 1)
for i in plant:
    visited[i] = True
    for x, y in graph[i]:
        heapq.heappush(pq, (y, i, x))
answer = 0
count = 0
while pq:
    if count >= m:
        break
    cost, start, end = heapq.heappop(pq)

    if visited[end] and visited[start]:
        continue
    else:
        visited[start], visited[end] = True, True
        answer += cost
        count += 1
    for x, y in graph[end]:
        heapq.heappush(pq, (y, end, x))

print(answer)

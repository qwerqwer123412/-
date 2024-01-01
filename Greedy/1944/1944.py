import sys
from collections import defaultdict, deque
import heapq

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
k = m + 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 좌표 ==> 노드 번호로 변경하는 과정
mapping = defaultdict(int)
for i in range(n):
    for j in range(n):
        if board[i][j] == "S":
            mapping[(i, j)] = 1
        elif board[i][j] == "K":
            mapping[(i, j)] = k
            k -= 1

# 2차원 배열로는 크루스칼 알고리즘을 적용하기 어려워 그래프형태로 변환해주기
graph = defaultdict(list)

# 변환 방법은 간단하다..
# BruteForce로 노드들 사이 거리 구하기
# BF로 할 수 있던 이유 ==> 연산의 max가 O(N**2) ==> 많아야 62500번의 연산을 수행
# 아래는 2차원 배열 좌표를 그래프 형태로 변경하는 과정이다
for a, b in mapping:
    q = deque()
    visited = [[int(1e9)] * n for _ in range(n)]
    visited[a][b] = 0
    q.append((a, b, 0))
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 못가거나 이미 방문을 한 경우..
            if board[nx][ny] == "1" or visited[nx][ny] != int(1e9):
                continue
            else:
                if board[nx][ny] == "K" or board[nx][ny] == "S":
                    graph[mapping[(a, b)]].append((mapping[(nx, ny)], dist + 1))

                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, dist + 1))

# Kruskal 알고리즘 ==> greedy한 방법 => ranking function이 필요하다!
# ranking function ==> heap 자료구조로 구현하였다
pq = []
for i in graph:
    for a, b in graph[i]:
        heapq.heappush(pq, (b, i, a))

parent = [i for i in range(m + 2)]


# Kruskal에서 union-find쓰는 이유?
# cycle check!
# cycle이 없다면? => union
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


# pq ==> 우선 순위 queue
pq = []
for i in graph:
    for a, b in graph[i]:
        heapq.heappush(pq, (b, i, a))

answer = 0
count = 0

while pq:
    c, a, b = heapq.heappop(pq)
    if find_parent(a) == find_parent(b):
        continue
    union(a, b)
    answer += c
    count += 1
    if count == m:
        break

# count는 cycle의 종료 조건 ==> bound값으로 작용할 수 있지만..
# 모든 노드를 방문했는가에 대한 검증을 하는 변수이기도 하다
# count == m이면 모든 노드가 하나의 tree로 구성됐음을 으미
# else: 모든 노드가 하나의 tree가 아니다 ==> 1개의 MST가 구성되지 않음을 의미한다
if count == m:
    print(answer)
else:
    print(-1)

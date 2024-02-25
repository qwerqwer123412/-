import sys
from collections import deque

n, m, oil = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
x, y = map(int, sys.stdin.readline().strip().split())
x, y = x - 1, y - 1
# 처리여부 저장
visited = [False] * m
# 손님 위치, 손님이 원하는 목적지 위치 정보 저장
pos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
for i in range(m):
    pos[i][0] -= 1
    pos[i][1] -= 1
    pos[i][2] -= 1
    pos[i][3] -= 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# return값: 현재 좌표에서 각 좌표까지의 거리 구하기
def distance(a, b):
    dist = [[int(1e9)] * n for _ in range(n)]
    dist[a][b] = 0
    q = deque()
    q.append((a, b, 0))
    while q:
        a, b, d = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            # 못가는 경우 or 이미 방문한 경우
            if (not (0 <= nx < n and 0 <= ny < n)) or board[nx][ny] == 1 or dist[nx][ny] != int(1e9):
                continue
            q.append((nx, ny, d + 1))
            dist[nx][ny] = d + 1
    return dist


# 현재 위치에서 다음 손님 번호 + 거리까지 return
def find_nearest(a, b):
    dist = distance(a, b)
    candidate = [i for i in range(m) if not visited[i]]
    candidate = sorted(candidate, key=lambda x: (dist[pos[x][0]][pos[x][1]], pos[x][0], pos[x][1]))
    select = candidate[0]
    return (select, dist[pos[select][0]][pos[select][1]])

while False in visited:
    customer, d = find_nearest(x, y)
    # 연료가 부족해~
    if oil < d:
        print(-1)
        sys.exit()
    oil -= d
    start, target = (pos[customer][0], pos[customer][1]), (pos[customer][2], pos[customer][3])
    dist = distance(start[0], start[1])
    # 연료가 부족해~
    if oil < dist[target[0]][target[1]]:
        print(-1)
        sys.exit()
    oil += dist[target[0]][target[1]]
    visited[customer] = True
    x, y = target

print(oil)

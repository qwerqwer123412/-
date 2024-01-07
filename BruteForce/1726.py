import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
# 시작 좌표 + 방향
start = list(map(int, sys.stdin.readline().strip().split()))

# 종료 좌표 + 방향
end = list(map(int, sys.stdin.readline().strip().split()))

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

dp = [[[sys.maxsize for _ in range(4)] for _ in range(m)] for _ in range(n)]

dp[start[0] - 1][start[1] - 1][start[2] - 1] = 0

q = deque()
q.append((start[0] - 1, start[1] - 1, start[2] - 1, 0))


# 현재 방향에서 다음 방향으로 전환하기 위해 드는 비용 계산
def change_dir(d, next_d):
    # 같으면 4번 회전.. ==> 무시하기 위한 로직
    if d == next_d:
        return 4
    if d in [0, 1]:
        if next_d in [2, 3]:
            return 1
        else:
            return 2
    else:
        if next_d in [0, 1]:
            return 1
        else:
            return 2


while q:

    x, y, d, count = q.popleft()
    if dp[x][y][d] < count:
        continue
    for i in range(4):
        # 방향 전환 횟수
        change_count = change_dir(d, i)
        if dp[x][y][i] > count + change_count:
            dp[x][y][i] = count + change_count
            q.append((x, y, i, count + change_count))

    for _ in range(3):
        nx, ny = x + dx[d], y + dy[d]
        # 못가는 경우
        # 범위를 벗어나는 경우
        # 막힌 경우..
        if (not (0 <= nx < n and 0 <= ny < m)) or board[nx][ny] == 1:
            break
        if dp[nx][ny][d] > count + 1:
            dp[nx][ny][d] = count + 1
            q.append((nx, ny, d, count + 1))
        x, y = nx, ny

print(dp[end[0] - 1][end[1] - 1][end[2] - 1])

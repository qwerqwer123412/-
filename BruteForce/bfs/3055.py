import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip()) for _ in range(n)]
# bfs 결과 값을 저장할 배열
dp = [[sys.maxsize] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 물과 비버가 이동할 수 있는 결과를 bfs방식으로 탐색할 것이다

water_q = deque()
beaver_q = deque()
# 최종적으로 고슴도치 집에 도착할 수 있는지 확인
dest = []
for i in range(n):
    for j in range(m):
        # 물이 차있는 지역
        if board[i][j] == "*":
            water_q.append((i, j))
        elif board[i][j] == "S":
            beaver_q.append((i, j, 0))
            dp[i][j] = 0
        elif board[i][j] == "D":
            dest = (i, j)


# beaver 움직이기
def beaver(beaver_q):
    next = deque()
    for x, y, cost in beaver_q:
        if dp[x][y] < cost:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 못가는 경우
            # 범위를 벗아나는 경우
            # 물이 있는 경우
            # 돌이 잇는 경우
            if (not (0 <= nx < n and 0 <= ny < m)) or board[nx][ny] == "*" or board[nx][ny] == "X":
                continue
            if dp[nx][ny] > cost + 1:
                dp[nx][ny] = cost + 1
                next.append((nx, ny, cost + 1))
    return next


# 물이 퍼지는 action을 표현한 함수
def water(water_q):
    next = deque()
    for x, y in water_q:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 못가는 경우
            # 범위를 벗아나는 경우
            # 돌이 있는경우
            # 비버집이 있는 경우
            # 이미 물로 찬경우
            if (not (0 <= nx < n and 0 <= ny < m)) or board[nx][ny] == "X" or board[nx][ny] == "D" or board[nx][
                ny] == "*":
                continue
            board[nx][ny] = "*"
            next.append((nx, ny))

    return next


while True:

    if water_q:
        water_q = water(water_q)
    if beaver_q:
        beaver_q = beaver(beaver_q)
    # 둘 다 더이상 이동할 곳이 없으면 종료
    if not water_q and not beaver_q:
        break

print(dp[dest[0]][dest[1]]) if dp[dest[0]][dest[1]] != sys.maxsize else print("KAKTUS")
